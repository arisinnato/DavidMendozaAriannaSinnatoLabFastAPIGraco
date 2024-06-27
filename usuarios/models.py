<<<<<<< HEAD
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
=======
"""from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import tipos_usuario.models as tipos_usuario
>>>>>>> 3de6dc9 (Avances David)

class Usuario(Base): 
    __tablename__  = "usuarios"
    
    cedula = Column(String, primary_key=True)
    nombres = Column(String, index=True)
    apellidos = Column(String, index=True)
    nacimiento = Column(DateTime, index=True)
    direccion = Column(String, index=True)
    correo = Column(String, index=True)
    contraseña = Column(String, index=True)
<<<<<<< HEAD
    tipo_id = Column(Integer, ForeignKey("tipos_usuarios.id"))

    tipo = relationship('Tipo_Usuario', back_populates='usuarios')
    #productos = relationship('Producto', back_populates='usuario')
    #calificaciones = relationship('Calificacion', back_populates='usuario')
    #compras = relationship('Compra', back_populates='cliente')
=======
    tipo_id = Column(Integer, ForeignKey(tipos_usuario.Tipo_Usuario.id))

    tipo = relationship('Tipo_Usuario', back_populates='usuarios')
    productos = relationship("producto", back_populates="usuarios")
    calificaciones = relationship('Calificacion', back_populates='usuario')
    compras = relationship('Compra', back_populates='cliente')"""

#########################################################################################

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base 
import tipos_usuario.models as tipos_usuario

class Usuario(Base): 
    __tablename__  = "usuarios"
    
    cedula = Column(String, primary_key=True)
    nombres = Column(String, index=True)
    apellidos = Column(String, index=True)
    nacimiento = Column(DateTime, index=True)
    direccion = Column(String, index=True)
    correo = Column(String, index=True)
    contraseña = Column(String, index=True)
    tipo_id = Column(Integer, ForeignKey(tipos_usuario.Tipo_Usuario.id))

    tipo = relationship('Tipo_Usuario', back_populates='usuarios')
    productos = relationship('Producto', back_populates='usuario')
    calificaciones = relationship('Calificacion', back_populates='usuario')
    compras = relationship('Compra', back_populates='cliente')


>>>>>>> 3de6dc9 (Avances David)
