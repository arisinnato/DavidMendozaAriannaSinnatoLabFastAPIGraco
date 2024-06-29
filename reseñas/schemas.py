from pydantic import BaseModel
from datetime import datetime

class Reseña_Base(BaseModel):
    invencion: datetime
    inventor: str
    años_produccion: float
    producto_id: int

class Reseña_a_Crear(Reseña_Base):
    pass

class Reseña(Reseña_Base):
    id: int

    class Config:
        orm_mode = True


