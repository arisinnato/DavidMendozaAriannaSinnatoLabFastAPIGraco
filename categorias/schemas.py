from pydantic import BaseModel
from typing import Union

class Categoria_Base(BaseModel):
    nombre: str
    descripcion: Union[str, None] = None

class Categoria_a_Crear(Categoria_Base):
    pass

class Categoria(Categoria_Base):
    id: int

    class Config:
        orm_mode = True

