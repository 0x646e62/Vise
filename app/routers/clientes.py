



from fastapi import APIRouter, HTTPException
from ..models.cliente import ClientRequest, ClientResponse
from ..models.purchase import PurchaseRequest, PurchaseResponse
from ..core.database import db

router = APIRouter()

# POST /clientes
@router.post("/client", response_model=ClientResponse)
async def register_client(client: ClientRequest):
    client_dict = db.register_client(client)
    apto = client_dict["cardType"] == "Platinum" and client_dict["monthlyIncome"] >= 1000
    if apto:
        status = "Registered"
        message = f"Cliente apto para tarjeta {client_dict['cardType']}"
    else:
        status = "Rejected"
        message = f"Cliente NO apto para tarjeta {client_dict['cardType']}"
    return ClientResponse(
        clientId=client_dict["clientId"],
        name=client_dict["name"],
        cardType=client_dict["cardType"],
        status=status,
        message=message
    )

# GET /client
@router.get("/client")
async def list_clients():
    return db.list_clients()

# GET /client/{client_id}
@router.get("/client/{client_id}")
async def get_client(client_id: int):
    client = db.get_client(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return client

# PUT /client/{client_id}
@router.put("/client/{client_id}", response_model=ClientResponse)
async def update_client(client_id: int, client: ClientRequest):
    updated = db.update_client(client_id, client)
    if not updated:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    # Recalcular aptitud
    apto = updated["cardType"] == "Platinum" and updated["monthlyIncome"] >= 1000
    status = "Registered"
    if apto:
        message = f"Cliente apto para tarjeta {updated['cardType']}"
    else:
        message = f"Cliente NO apto para tarjeta {updated['cardType']}"
    return ClientResponse(
        clientId=updated["clientId"],
        name=updated["name"],
        cardType=updated["cardType"],
        status=status,
        message=message
    )


# DELETE /client/{client_id}
@router.delete("/client/{client_id}")
async def delete_client(client_id: int):
    deleted = db.delete_client(client_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return {"detail": "Cliente eliminado"}


# POST /purchase
@router.post("/purchase", response_model=PurchaseResponse)
async def process_purchase(purchase: PurchaseRequest):
    client = db.get_client(purchase.clientId)
    if not client:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    # Lógica de beneficios
    from datetime import datetime
    day_of_week = datetime.strptime(purchase.purchaseDate, "%Y-%m-%d").weekday()  # 0=Mon, 6=Sun
    discount = 0
    benefit = ""
    card = client["cardType"].lower()
    amount = purchase.amount
    country = purchase.purchaseCountry
    is_foreign = country.lower() != client["country"].lower()

    # Classic: sin beneficios
    if card == "classic":
        status = "Approved"
        benefit = "Sin beneficio"
    # Gold
    elif card == "gold":
        if is_foreign:
            discount = int(amount * 0.05)
            benefit = "5% descuento internacional"
        elif day_of_week == 0 and amount > 100:
            discount = int(amount * 0.15)
            benefit = "15% lunes >100usd"
        else:
            benefit = "Sin beneficio"
        status = "Approved"
    # Platinum
    elif card == "platinum":
        if is_foreign:
            discount = int(amount * 0.05)
            benefit = "5% descuento internacional"
        elif day_of_week in [0,1,2] and amount > 100:
            discount = int(amount * 0.20)
            benefit = "20% lun-mie >100usd"
        elif day_of_week == 5 and amount > 200:
            discount = int(amount * 0.30)
            benefit = "30% sabado >200usd"
        else:
            benefit = "Sin beneficio"
        status = "Approved"
    # Black
    elif card == "black":
        if is_foreign:
            discount = int(amount * 0.05)
            benefit = "5% descuento internacional"
        elif day_of_week in [0,1,2] and amount > 100:
            discount = int(amount * 0.25)
            benefit = "25% lun-mie >100usd"
        elif day_of_week == 5 and amount > 200:
            discount = int(amount * 0.35)
            benefit = "35% sabado >200usd"
        else:
            benefit = "Sin beneficio"
        status = "Approved"
    # White
    elif card == "white":
        if is_foreign:
            discount = int(amount * 0.05)
            benefit = "5% descuento internacional"
        elif day_of_week in [0,1,2,3,4] and amount > 100:
            discount = int(amount * 0.25)
            benefit = "25% lun-vie >100usd"
        elif day_of_week in [5,6] and amount > 200:
            discount = int(amount * 0.35)
            benefit = "35% sab-dom >200usd"
        else:
            benefit = "Sin beneficio"
        status = "Approved"
    else:
        status = "Rejected"
        benefit = "Tipo de tarjeta no válido"

    final_amount = int(amount - discount)
    purchase_info = {
        "amount": amount,
        "currency": purchase.currency,
        "purchaseDate": purchase.purchaseDate,
        "purchaseCountry": purchase.purchaseCountry,
        "discountApplied": discount,
        "finalAmount": final_amount,
        "benefit": benefit
    }
    return PurchaseResponse(status=status, purchase=purchase_info)
