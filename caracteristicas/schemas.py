from pydantic import BaseModel
from typing import Union

class Caracteristica_Base(BaseModel):
    nombre: str
    explicacion: str
    encargo_id: int
    estado_caracteristica_id: Union[int, None] = None

class Caracteristica_a_Crear(Caracteristica_Base):
    pass

class Caracteristica(Caracteristica_Base):
    id: int

    class Config:
        orm_mode = True

