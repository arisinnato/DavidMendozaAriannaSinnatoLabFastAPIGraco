from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Estado_Compra(Base): 
    __tablename__  = "estados_compras"
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, index=True)
    descripcion = Column(String, index=True)

    compras = relationship('Compra', back_populates='estado_compra')