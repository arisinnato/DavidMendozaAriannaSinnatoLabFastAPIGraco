from pydantic import BaseModel
from typing import Union

class Estado_de_Compra_Base(BaseModel):
    nombre: str
    descripcion: Union[str, None] = None

class Estado_de_Compra_Crear(Estado_de_Compra_Base):
    pass

class Estado_Compra(Estado_de_Compra_Base):
    id: int

    class Config:
        orm_mode = True


