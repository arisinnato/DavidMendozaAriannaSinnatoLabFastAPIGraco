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

@router.get('')
def home():
    return {"message":"yolo"}

@router.post('', response_model=schemas.Estado_Compra)
def crear_estado_compra(estado_compra: schemas.Estado_CompraCrear, db: Session = Depends(get_db)):
    return service.crear_estado_compra(db=db, estado_compra=estado_compra)


