from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import estado_de_caracteristica.models as models 
import estado_de_caracteristica.schemas as schemas
import estado_de_caracteristica.service as service

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
    return {"message":"yolooooooooo"}

@router.post('', response_model=schemas.Estado_Caracteristica)
def crear_estado_caracteristica(estado_caracteristica: schemas.Estado_CaracteristicaCrear, db: Session = Depends(get_db)):
    return service.crear_estado_caracteristica(db=db, estado_caracteristica=estado_caracteristica)


