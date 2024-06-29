from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import metodos_de_envio.models as models 
import metodos_de_envio.schemas as schemas
import metodos_de_envio.service as service

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""@router.get('', response_model=list[schemas.Metodo_Envio])
def listar_un_metodo_de_envio(db: Session = Depends(get_db)):
    return service.listar_un_metodo_de_envio(db=db)

@router.post('', response_model=schemas.Metodo_Envio)
def crear_un_metodo_de_envio(metodo_envio: schemas.Metodo_de_Envio_a_Crear, db: Session = Depends(get_db)):
    return service.crear_un_metodo_de_envio(db=db, metodo_envio=metodo_envio)
"""


@router.get('', response_model=list[schemas.Metodo_Envio])
def listar_un_metodo_de_envio(db: Session = Depends(get_db)):
    return service.listar_un_metodo_de_envio(db=db)

@router.post('', response_model=schemas.Metodo_Envio)
def crear_un_metodo_de_envio(metodo_envio: schemas.Metodo_de_Envio_a_Crear, db: Session = Depends(get_db)):
    return service.crear_un_metodo_de_envio(db=db, metodo_envio=metodo_envio)