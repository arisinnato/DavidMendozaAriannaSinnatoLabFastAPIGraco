from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import usuarios.models as usuarios
import productos.models as productos

class Calificacion(Base): 
    __tablename__  = "calificaciones"
    
    id = Column(Integer, primary_key=True)
    titulo = Column(String, index=True)
    comentario = Column(String, index=True)
    estrellas = Column(Integer, index=True)
    emoticono = Column(Integer, index=True, nullable=True)
    usuario_cedula = Column(String, ForeignKey(usuarios.Usuario.cedula))
    producto_id = Column(Integer, ForeignKey(productos.Producto.id))

    usuario = relationship('Usuario', back_populates='calificaciones')
    producto = relationship('Producto', back_populates='calificaciones')