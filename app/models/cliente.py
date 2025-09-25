from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ClienteBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50)
    edad: int = Field(..., ge=0, le=120)
    activo: bool = Field(True)

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(ClienteBase):
    nombre: Optional[str] = Field(None, min_length=2, max_length=50)
    edad: Optional[int] = Field(None, ge=0, le=120)
    activo: Optional[bool] = None

class Cliente(ClienteBase):
    id: int
    creado_en: datetime
    actualizado_en: Optional[datetime] = None

    class Config:
        from_attributes = True

class ClienteResponse(BaseModel):
    mensaje: str
    cliente: Cliente

class ClientesListResponse(BaseModel):
    clientes: list[Cliente]
    total: int