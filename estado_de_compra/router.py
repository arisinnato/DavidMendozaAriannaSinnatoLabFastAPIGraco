from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import estado_de_compra.models as models 
import estado_de_compra.schemas as schemas
import estado_de_compra.service as service

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('', response_model=list[schemas.Estado_Compra])
def listar_estados_compras(db: Session = Depends(get_db)):
    return service.listar_estado_compra(db=db)

"""@router.post('', response_model=schemas.Estado_Compra)
def crear_un_estado_de_la_compra(estado_compra: schemas.Estado_de_Compra_Crear, db: Session = Depends(get_db)):
    return service.crear_un_estado_de_la_compra(db=db, estado_compra=estado_compra)"""



@router.post('', response_model=schemas.Estado_Compra)
def crear_un_estado_de_la_compra(estado_compra: schemas.Estado_de_Compra_Crear, db: Session = Depends(get_db)):
    return service.crear_un_estado_de_la_compra(db=db, estado_compra=estado_compra)



