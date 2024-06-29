from pydantic import BaseModel
from typing import Union

class el_Tipo_de_Usuario_Base(BaseModel):
    nombre: str
    descripcion: Union[str, None] = None

class el_Tipo_de_Usuario_ha_Crear(el_Tipo_de_Usuario_Base):
    pass

class Tipo_Usuario(el_Tipo_de_Usuario_Base):
    id: int

    class Config:
        orm_mode = True


