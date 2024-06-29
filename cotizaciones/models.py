from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import compras.models as compras 
import estado_de_cotizacion.models as estado_de_cotizacion 



class Cotizacion(Base): 
    __tablename__  = "cotizaciones"
    
    id = Column(Integer, primary_key=True)
    precio = Column(Float, index=True)
    compra_id = Column(Integer, ForeignKey(compras.Compra.id))
    estado_cotizacion_id = Column(Integer, ForeignKey(estado_de_cotizacion.Estado_Cotizacion.id))

    compra = relationship('Compra', back_populates='cotizaciones')
    estado_cotizacion = relationship('Estado_Cotizacion', back_populates='cotizaciones')
    factura = relationship('Factura', back_populates='cotizacion')