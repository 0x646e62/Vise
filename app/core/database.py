from datetime import datetime
from typing import Dict, Optional
from ..models.cliente import Cliente, ClienteCreate, ClienteUpdate

class DatabaseManager:
    
    def __init__(self):
        self._clientes: Dict[int, dict] = {}
        self._next_id = 1
    
    def crear_cliente(self, cliente_data: ClienteCreate) -> Cliente:
        cliente_dict = {
            "id": self._next_id,
            "nombre": cliente_data.nombre,
            "edad": cliente_data.edad,
            "activo": cliente_data.activo,
            "creado_en": datetime.now(),
            "actualizado_en": None
        }
        
        self._clientes[self._next_id] = cliente_dict
        self._next_id += 1
        
        return Cliente(**cliente_dict)
    
    def obtener_cliente(self, cliente_id: int) -> Optional[Cliente]:
        cliente_dict = self._clientes.get(cliente_id)
        if cliente_dict:
            return Cliente(**cliente_dict)
        return None
    
    def listar_clientes(self) -> list[Cliente]:
        return [Cliente(**cliente_dict) for cliente_dict in self._clientes.values()]
    
    def actualizar_cliente(self, cliente_id: int, cliente_data: ClienteUpdate) -> Optional[Cliente]:
        if cliente_id not in self._clientes:
            return None
        
        cliente_dict = self._clientes[cliente_id]
        
        update_data = cliente_data.model_dump(exclude_unset=True)
        cliente_dict.update(update_data)
        cliente_dict["actualizado_en"] = datetime.now()
        
        return Cliente(**cliente_dict)
    
    def eliminar_cliente(self, cliente_id: int) -> Optional[Cliente]:
        cliente_dict = self._clientes.pop(cliente_id, None)
        if cliente_dict:
            return Cliente(**cliente_dict)
        return None
    
    def contar_clientes(self) -> int:
        return len(self._clientes)

db = DatabaseManager()