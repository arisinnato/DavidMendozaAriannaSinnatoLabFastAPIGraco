from pydantic import BaseModel, field_validator
from typing import Union
class Calificacion_Base(BaseModel):
    titulo: str
    comentario: str
    estrellas: int
    emoticono: Union[str, None] = None
    usuario_cedula: str
    producto_id: int

    @field_validator('estrellas')
    def verificar_estrellas(cls, estrellas): 
        if estrellas > 10: 
            raise ValueError('las estrellas maximas son de 10')
        if estrellas < 0: 
            raise ValueError('las estrellas minimas son de 0')
        return estrellas

class Calificacion_a_Crear(Calificacion_Base):
    pass

class Calificacion(Calificacion_Base):
    id: int

    class Config:
        orm_mode = True

