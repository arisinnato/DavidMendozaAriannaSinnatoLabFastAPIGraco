from sqlalchemy.orm import Session
import reseñas.models as models
import reseñas.schemas as schemas

"""def crear_un_reseña(db: Session, reseña: schemas.Reseña_a_Crear):
    db_reseña = models.Reseña(
        invencion=reseña.invencion, 
        inventor=reseña.inventor, 
        años_produccion=reseña.años_produccion, 
        producto_id=reseña.producto_id)
    db.add(db_reseña)
    db.commit()
    db.refresh(db_reseña)
    return db_reseña

def listar_todas_las_reseñas_disponibles(db: Session): 
    return db.query(models.Reseña).all()

def listar_las_reseñas_de_productos_disponibles(db: Session, id: int): 
    return db.query(models.Reseña).filter(models.Reseña.producto_id == id).all()

def buscar_un_reseña_existente(db: Session, id: int): 
    reseña = db.query(models.Reseña).filter(models.Reseña.id == id).first()
    return reseña

def modificar_una_reseña_existente(db: Session, id: int, reseña: schemas.Reseña_a_Crear): 
    lista = db.query(models.Reseña).all()
    for este in lista: 
        if este.id == id: 
            este.invencion = reseña.invencion
            este.inventor = reseña.inventor
            este.años_produccion = reseña.años_produccion
            este.producto_id = reseña.producto_id
            break
    db.commit()
    return este

def eliminar_reseña(db: Session, id: int): 
    reseña = db.query(models.Reseña).filter(models.Reseña.id == id).first()
    db.delete(reseña)
    db.commit()
    return reseña"""


def crear_un_reseña(db: Session, reseña: schemas.Reseña_a_Crear):
    db_reseña = models.Reseña(
        invencion=reseña.invencion, 
        inventor=reseña.inventor, 
        años_produccion=reseña.años_produccion, 
        producto_id=reseña.producto_id)
    db.add(db_reseña)
    db.commit()
    db.refresh(db_reseña)
    return db_reseña

def listar_todas_las_reseñas_disponibles(db: Session): 
    return db.query(models.Reseña).all()

def listar_las_reseñas_de_productos_disponibles(db: Session, id: int): 
    return db.query(models.Reseña).filter(models.Reseña.producto_id == id).all()

def buscar_un_reseña_existente(db: Session, id: int): 
    reseña = db.query(models.Reseña).filter(models.Reseña.id == id).first()
    return reseña

def modificar_una_reseña_existente(db: Session, id: int, reseña: schemas.Reseña_a_Crear): 
    lista = db.query(models.Reseña).all()
    for este in lista: 
        if este.id == id: 
            este.invencion = reseña.invencion
            este.inventor = reseña.inventor
            este.años_produccion = reseña.años_produccion
            este.producto_id = reseña.producto_id
            break
    db.commit()
    return este

def eliminar_reseña(db: Session, id: int): 
    reseña = db.query(models.Reseña).filter(models.Reseña.id == id).first()
    db.delete(reseña)
    db.commit()
    return reseña