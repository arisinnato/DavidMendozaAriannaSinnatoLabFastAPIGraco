from pydantic import BaseModel
from typing import Union

class Metodo_Envio_Base(BaseModel):
    nombre: str
    descripcion: Union[str, None] = None

class Metodo_de_Envio_a_Crear(Metodo_Envio_Base):
    pass

class Metodo_Envio(Metodo_Envio_Base):
    id: int

    class Config:
        orm_mode = True


