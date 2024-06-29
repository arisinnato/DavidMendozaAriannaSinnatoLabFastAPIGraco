from sqlalchemy.orm import Session
from schemas import Respuesta
import estado_de_cotizacion.models as models
import estado_de_cotizacion.schemas as schemas

"""def crear_un_estado_de_cotizacion(db: Session, estado_cotizacion: schemas.Estado_de_Cotizacion_a_Crear):
    db_estado_cotizacion = models.Estado_Cotizacion(
        nombre=estado_cotizacion.nombre, 
        descripcion=estado_cotizacion.descripcion)
    db.add(db_estado_cotizacion)
    db.commit()
    db.refresh(db_estado_cotizacion)
    return db_estado_cotizacion"""

def get_estado_cotizacion(db: Session, id: int):
    returned = db.query(models.Estado_Cotizacion).filter(models.Estado_Cotizacion.id == id).first()

    if returned == None:
        return Respuesta[schemas.Estado_Cotizacion](ok=False, mensaje='el estado de la cotizacion no se ha encontrado')

    estado_cotizacion = schemas.Estado_Cotizacion(nombre=returned.nombre, descripcion=returned.descripcion, id=returned.id) 
    return Respuesta[schemas.Estado_Cotizacion](ok=True, mensaje='el estado de la cotización se ha encontrado', data=estado_cotizacion)


def crear_un_estado_de_cotizacion(db: Session, estado_cotizacion: schemas.Estado_de_Cotizacion_a_Crear):
    db_estado_cotizacion = models.Estado_Cotizacion(
        nombre=estado_cotizacion.nombre, 
        descripcion=estado_cotizacion.descripcion)
    db.add(db_estado_cotizacion)
    db.commit()
    db.refresh(db_estado_cotizacion)
    return db_estado_cotizacion