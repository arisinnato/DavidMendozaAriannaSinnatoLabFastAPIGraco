from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine 
import metodo_de_pagos.models as models 
import metodo_de_pagos.schemas as schemas
import metodo_de_pagos.service as service

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('', response_model=list[schemas.Metodo_Pago])
def home(db: Session = Depends(get_db)):
    return service.listar_todos_los_metodos__de_pagos(db=db)

@router.post('', response_model=schemas.Metodo_Pago)
def crear_un_de_metodo_pago(metodo_pago: schemas.Metodo_de_Pago_a_Crear, db: Session = Depends(get_db)):
    return service.crear_un_de_metodo_pago(db=db, metodo_pago=metodo_pago)

