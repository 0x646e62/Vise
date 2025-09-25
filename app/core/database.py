from datetime import datetime
from typing import Dict, Optional
from ..models.usuario import Usuario, UsuarioCreate, UsuarioUpdate

class DatabaseManager:
    
    def __init__(self):
        self._usuarios: Dict[int, dict] = {}
        self._next_id = 1
    
    def crear_usuario(self, usuario_data: UsuarioCreate) -> Usuario:
        usuario_dict = {
            "id": self._next_id,
            "nombre": usuario_data.nombre,
            "edad": usuario_data.edad,
            "activo": usuario_data.activo,
            "creado_en": datetime.now(),
            "actualizado_en": None
        }
        
        self._usuarios[self._next_id] = usuario_dict
        self._next_id += 1
        
        return Usuario(**usuario_dict)
    
    def obtener_usuario(self, usuario_id: int) -> Optional[Usuario]:
        usuario_dict = self._usuarios.get(usuario_id)
        if usuario_dict:
            return Usuario(**usuario_dict)
        return None
    
    def listar_usuarios(self) -> list[Usuario]:
        return [Usuario(**usuario_dict) for usuario_dict in self._usuarios.values()]
    
    def actualizar_usuario(self, usuario_id: int, usuario_data: UsuarioUpdate) -> Optional[Usuario]:
        if usuario_id not in self._usuarios:
            return None
        
        usuario_dict = self._usuarios[usuario_id]
        
        update_data = usuario_data.model_dump(exclude_unset=True)
        usuario_dict.update(update_data)
        usuario_dict["actualizado_en"] = datetime.now()
        
        return Usuario(**usuario_dict)
    
    def eliminar_usuario(self, usuario_id: int) -> Optional[Usuario]:
        usuario_dict = self._usuarios.pop(usuario_id, None)
        if usuario_dict:
            return Usuario(**usuario_dict)
        return None
    
    def contar_usuarios(self) -> int:
        return len(self._usuarios)

db = DatabaseManager()