from sqlalchemy.orm import Session
import estado_de_compra.models as models
import estado_de_compra.schemas as schemas

def crear_estado_compra(db: Session, estado_compra: schemas.Estado_CompraCrear):
    db_estado_compra = models.Estado_Compra(
        nombre=estado_compra.nombre, 
        descripcion=estado_compra.descripcion)
    db.add(db_estado_compra)
    db.commit()
    db.refresh(db_estado_compra)
    return db_estado_compra