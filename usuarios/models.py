from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Usuario(Base): 
    __tablename__  = "usuarios"
    
    cedula = Column(String, primary_key=True)
    nombres = Column(String, index=True)
    apellidos = Column(String, index=True)
    nacimiento = Column(DateTime, index=True)
    direccion = Column(String, index=True)
    correo = Column(String, index=True)
    contraseña = Column(String, index=True)
    tipo_id = Column(Integer, ForeignKey("tipos_usuarios.id"))

    tipo = relationship('Tipo_Usuario', back_populates='usuarios')
    #productos = relationship('Producto', back_populates='usuario')
    #calificaciones = relationship('Calificacion', back_populates='usuario')
    #compras = relationship('Compra', back_populates='cliente')