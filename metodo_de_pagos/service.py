from sqlalchemy.orm import Session
from schemas import Respuesta
import metodo_de_pagos.models as models
import metodo_de_pagos.schemas as schemas



"""def listar_todos_los_metodos__de_pagos(db: Session): 
    returned = db.query(models.Metodo_Pago).all()

    pagos = []

    for pag in returned:
        pago = schemas.Metodo_Pago(nombre=pag.nombre, descripcion=pag.descripcion, id=pag.id) 
        pagos.append(pago)

    respuesta = Respuesta[list[schemas.Metodo_Pago]](ok=True, mensaje='Métodos de pago encontrado', data=pagos)
    return respuesta"""

def listar_todos_los_metodos__de_pagos(db: Session): 
    returned = db.query(models.Metodo_Pago).all()

    pagos = []

    for pag in returned:
        pago = schemas.Metodo_Pago(nombre=pag.nombre, descripcion=pag.descripcion, id=pag.id) 
        pagos.append(pago)

    respuesta = Respuesta[list[schemas.Metodo_Pago]](ok=True, mensaje='Métodos de pago encontrado', data=pagos)
    return respuesta


def crear_un_de_metodo_pago(db: Session, metodo_pago: schemas.Metodo_de_Pago_a_Crear):
    db_metodo_pago = models.Metodo_Pago(
        nombre=metodo_pago.nombre, 
        descripcion=metodo_pago.descripcion)
    db.add(db_metodo_pago)
    db.commit()
    db.refresh(db_metodo_pago)
    return db_metodo_pago