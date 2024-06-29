from pydantic import BaseModel
from typing import Union

class Estado_de_Caracteristica_Base(BaseModel):
    nombre: str
    descripcion: Union[str, None] = None

class Estado_de_Caracteristica_a_Crear(Estado_de_Caracteristica_Base):
    pass

class Estado_Caracteristica(Estado_de_Caracteristica_Base):
    id: int

    class Config:
        orm_mode = True


