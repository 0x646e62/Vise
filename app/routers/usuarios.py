from fastapi import APIRouter, HTTPException
from typing import Optional
from ..models.usuario import (
    Usuario, 
    UsuarioCreate, 
    UsuarioUpdate, 
    UsuarioResponse, 
    UsuariosListResponse
)
from ..core.database import db

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.post("/", response_model=UsuarioResponse)
async def crear_usuario(usuario: UsuarioCreate):
    nuevo_usuario = db.crear_usuario(usuario)
    return UsuarioResponse(
        mensaje="Usuario creado exitosamente",
        usuario=nuevo_usuario
    )

@router.get("/", response_model=UsuariosListResponse)
async def listar_usuarios():
    usuarios = db.listar_usuarios()
    return UsuariosListResponse(
        usuarios=usuarios,
        total=db.contar_usuarios()
    )

@router.get("/{usuario_id}", response_model=Usuario)
async def obtener_usuario(usuario_id: int):
    usuario = db.obtener_usuario(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.put("/{usuario_id}", response_model=UsuarioResponse)
async def actualizar_usuario(usuario_id: int, usuario_data: UsuarioUpdate):
    usuario_actualizado = db.actualizar_usuario(usuario_id, usuario_data)
    if not usuario_actualizado:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return UsuarioResponse(
        mensaje="Usuario actualizado exitosamente",
        usuario=usuario_actualizado
    )

@router.delete("/{usuario_id}", response_model=UsuarioResponse)
async def eliminar_usuario(usuario_id: int):
    usuario_eliminado = db.eliminar_usuario(usuario_id)
    if not usuario_eliminado:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return UsuarioResponse(
        mensaje="Usuario eliminado exitosamente",
        usuario=usuario_eliminado
    )