from sqlalchemy import Column, Integer, Float, String, BLOB, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import usuarios.models as usuarios
import tipos_producto.models as tipos_producto
import categorias.models as categorias

class Producto(Base): 
    __tablename__  = "productos"
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, index=True)
    descripcion = Column(String, index=True)
    altura_cm = Column(Float, index=True)
    anchura_cm = Column(Float, index=True)
    profundidad_cm = Column(Float, index=True)
    imagen = Column(BLOB, index=True)
    peso_gramo = Column(Float, index=True)
    usuario_cedula = Column(String, ForeignKey(usuarios.Usuario.cedula))
    tipo_producto_id = Column(Integer, ForeignKey(tipos_producto.Tipo_Producto.id))


    usuario = relationship("Usuario", back_populates= "productos")
    tipo_producto = relationship('Tipo_Producto', back_populates='productos')
    calificaciones = relationship('Calificacion', back_populates='producto')
    compras = relationship('Compra', back_populates='producto')
    categoria_id = Column(Integer, ForeignKey(categorias.Categoria.id))

    usuario = relationship('Usuario', back_populates='productos')
    tipo_producto = relationship('Tipo_Producto', back_populates='productos')
    categoria = relationship('Categoria', back_populates='productos')
    calificaciones = relationship('Calificacion', back_populates='producto')
    reseñas = relationship('Reseña', back_populates='producto')
    compras = relationship('Compra', back_populates='producto')
