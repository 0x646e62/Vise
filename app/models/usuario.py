from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class UsuarioBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50)
    edad: int = Field(..., ge=0, le=120)
    activo: bool = Field(True)

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(UsuarioBase):
    nombre: Optional[str] = Field(None, min_length=2, max_length=50)
    edad: Optional[int] = Field(None, ge=0, le=120)
    activo: Optional[bool] = None

class Usuario(UsuarioBase):
    id: int
    creado_en: datetime
    actualizado_en: Optional[datetime] = None

    class Config:
        from_attributes = True

class UsuarioResponse(BaseModel):
    mensaje: str
    usuario: Usuario

class UsuariosListResponse(BaseModel):
    usuarios: list[Usuario]
    total: int