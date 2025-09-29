


from fastapi import APIRouter, HTTPException
from ..models.cliente import ClientRequest, ClientResponse
from ..core.database import db

router = APIRouter()

# POST /clientes
@router.post("/clientes", response_model=ClientResponse)
async def register_client(client: ClientRequest):
    client_dict = db.register_client(client)
    apto = client_dict["cardType"] == "Platinum" and client_dict["monthlyIncome"] >= 1000
    status = "Registered"
    if apto:
        message = f"Cliente apto para tarjeta {client_dict['cardType']}"
    else:
        message = f"Cliente NO apto para tarjeta {client_dict['cardType']}"
    return ClientResponse(
        clientId=client_dict["clientId"],
        name=client_dict["name"],
        cardType=client_dict["cardType"],
        status=status,
        message=message
    )

# GET /clientes
@router.get("/clientes")
async def list_clients():
    return db.list_clients()

# GET /clientes/{cliente_id}
@router.get("/clientes/{cliente_id}")
async def get_client(cliente_id: int):
    client = db.get_client(cliente_id)
    if not client:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return client

# PUT /clientes/{cliente_id}
@router.put("/clientes/{cliente_id}", response_model=ClientResponse)
async def update_client(cliente_id: int, client: ClientRequest):
    updated = db.update_client(cliente_id, client)
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

# DELETE /clientes/{cliente_id}
@router.delete("/clientes/{cliente_id}")
async def delete_client(cliente_id: int):
    deleted = db.delete_client(cliente_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return {"detail": "Cliente eliminado"}