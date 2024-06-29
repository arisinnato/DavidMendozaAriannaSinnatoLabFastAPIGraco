from sqlalchemy.orm import Session
from schemas import Respuesta
import metodos_de_envio.models as models
import metodos_de_envio.schemas as schemas



"""def listar_un_metodo_de_envio(db: Session): 
    returned = db.query(models.Metodo_Envio).all()

    envios = []

    for env in returned:
        envio = schemas.Metodo_Envio(nombre=env.nombre, descripcion=env.descripcion, id=env.id) 
        envios.append(envio)

    respuesta = Respuesta[list[schemas.Metodo_Envio]](ok=True, mensaje='el metodo de envio ha sido encontrado', data=envios)
    return respuesta"""


def listar_un_metodo_de_envio(db: Session): 
    returned = db.query(models.Metodo_Envio).all()

    envios = []

    for env in returned:
        envio = schemas.Metodo_Envio(nombre=env.nombre, descripcion=env.descripcion, id=env.id) 
        envios.append(envio)

    respuesta = Respuesta[list[schemas.Metodo_Envio]](ok=True, mensaje='el metodo de envio ha sido encontrado', data=envios)
    return respuesta

def crear_un_metodo_de_envio(db: Session, metodo_envio: schemas.Metodo_de_Envio_a_Crear):
    db_metodo_envio = models.Metodo_Envio(
        nombre=metodo_envio.nombre, 
        descripcion=metodo_envio.descripcion)
    db.add(db_metodo_envio)
    db.commit()
    db.refresh(db_metodo_envio)
    return db_metodo_envio