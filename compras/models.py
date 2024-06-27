from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import tipo_compra.models as tipo_compra 
import usuarios.models as usuarios
import productos.models as productos
import estado_de_compra.models as estado_de_compra

class Compra(Base): 
    __tablename__  = "compras"
    
    id = Column(Integer, primary_key=True)
    cantidad = Column(Integer, index=True)
    fecha = Column(DateTime, index=True)
    cliente_cedula = Column(String, ForeignKey(usuarios.Usuario.cedula))
    producto_id = Column(Integer, ForeignKey(productos.Producto.id))
    tipo_compra_id = Column(Integer, ForeignKey(tipo_compra.Tipo_Compra.id))
    estado_compra_id = Column(Integer, ForeignKey(estado_de_compra.Estado_Compra.id))

    cliente = relationship('Usuario', back_populates='compras')
    producto = relationship('Producto', back_populates='compras')
    tipo_compra = relationship('Tipo_Compra', back_populates='compras')
    estado_compra = relationship('Estado_Compra', back_populates='compras')

    # caracteristicas = relationship('Caracteristica', back_populates='encargo')
    # cotizaciones = relationship('Cotizacion', back_populates='compra')

    caracteristicas = relationship('Caracteristica', back_populates='encargo')
    cotizaciones = relationship('Cotizacion', back_populates='compra')
