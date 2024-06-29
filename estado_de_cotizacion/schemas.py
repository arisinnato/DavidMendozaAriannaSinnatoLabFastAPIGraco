from pydantic import BaseModel
from typing import Union

class Estado_de_Cotizacion_Base(BaseModel):
    nombre: str
    descripcion: Union[str, None] = None

class Estado_de_Cotizacion_a_Crear(Estado_de_Cotizacion_Base):
    pass

class Estado_Cotizacion(Estado_de_Cotizacion_Base):
    id: int

    class Config:
        orm_mode = True


