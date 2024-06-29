from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import cotizaciones.models as cotizaciones 
import metodos_de_envio.models as metodos_de_envio 
import metodo_de_pagos.models as metodo_de_pagos 




class Factura(Base): 
    __tablename__  = "facturas"
    
    id = Column(Integer, primary_key=True)
    fecha_entrega = Column(DateTime, index=True)
    cotizacion_id = Column(Integer, ForeignKey(cotizaciones.Cotizacion.id))
    metodo_pago_id = Column(Integer, ForeignKey(metodo_de_pagos.Metodo_Pago.id))
    metodo_envio_id = Column(Integer, ForeignKey(metodos_de_envio.Metodo_Envio.id))

    cotizacion = relationship('Cotizacion', back_populates='factura')
    metodo_pago = relationship('Metodo_Pago', back_populates='facturas')
    metodo_envio = relationship('Metodo_Envio', back_populates='facturas')