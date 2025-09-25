from fastapi import APIRouter, HTTPException
from ..models.cliente import (
    Cliente, 
    ClienteCreate, 
    ClienteUpdate, 
    ClienteResponse, 
    ClientesListResponse
)
from ..core.database import db

router = APIRouter(prefix="/clientes", tags=["clientes"])

@router.post("/", response_model=ClienteResponse)
async def crear_cliente(cliente: ClienteCreate):
    nuevo_cliente = db.crear_cliente(cliente)
    return ClienteResponse(
        mensaje="Cliente creado exitosamente",
        cliente=nuevo_cliente
    )

@router.get("/", response_model=ClientesListResponse)
async def listar_clientes():
    clientes = db.listar_clientes()
    return ClientesListResponse(
        clientes=clientes,
        total=db.contar_clientes()
    )

@router.get("/{cliente_id}", response_model=Cliente)
async def obtener_cliente(cliente_id: int):
    cliente = db.obtener_cliente(cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@router.put("/{cliente_id}", response_model=ClienteResponse)
async def actualizar_cliente(cliente_id: int, cliente_data: ClienteUpdate):
    cliente_actualizado = db.actualizar_cliente(cliente_id, cliente_data)
    if not cliente_actualizado:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    return ClienteResponse(
        mensaje="Cliente actualizado exitosamente",
        cliente=cliente_actualizado
    )

@router.delete("/{cliente_id}", response_model=ClienteResponse)
async def eliminar_cliente(cliente_id: int):
    cliente_eliminado = db.eliminar_cliente(cliente_id)
    if not cliente_eliminado:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    return ClienteResponse(
        mensaje="Cliente eliminado exitosamente",
        cliente=cliente_eliminado
    )