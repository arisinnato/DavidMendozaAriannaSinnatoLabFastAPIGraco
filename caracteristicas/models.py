from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import compras.models as compras 
import estado_de_caracteristica.models as estado_de_caracteristica 



class Caracteristica(Base): 
    __tablename__  = "caracteristicas"
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, index=True)
    explicacion = Column(String, index=True)
    encargo_id = Column(Integer, ForeignKey(compras.Compra.id))
    estado_caracteristica_id = Column(Integer, ForeignKey(estado_de_caracteristica.Estado_Caracteristica.id))

    encargo = relationship('Compra', back_populates='caracteristicas')
    estado_caracteristica = relationship('Estado_Caracteristica', back_populates='caracteristicas')