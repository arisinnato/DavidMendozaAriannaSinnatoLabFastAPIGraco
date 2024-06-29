from pydantic import BaseModel
from typing import Union

class Metodo_de_Pago_Base(BaseModel):
    nombre: str
    descripcion: Union[str, None] = None

class Metodo_de_Pago_a_Crear(Metodo_de_Pago_Base):
    pass

class Metodo_Pago(Metodo_de_Pago_Base):
    id: int

    class Config:
        orm_mode = True


