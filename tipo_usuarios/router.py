from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import Respuesta
from database import SessionLocal, engine
import tipo_usuarios.models as models 
import tipo_usuarios.schemas as schemas
import tipo_usuarios.service as service

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('', response_model=list[schemas.Tipo_Usuario])
def listar_tipos_usuarios(db: Session = Depends(get_db)):
    return service.listar_tipos_usuarios(db=db)

@router.post('', response_model=Respuesta[schemas.Tipo_Usuario])
def crear_tipo_usuario(tipo_usuario: schemas.Tipo_UsuarioCrear, db: Session = Depends(get_db)):
    return service.crear_tipo_usuario(db=db, tipo_usuario=tipo_usuario)

@router.get('/{id}', response_model=schemas.Tipo_Usuario)
def buscar_tipo_usuario(id : int, db: Session = Depends(get_db)): 
    return service.buscar_tipo_usuario(db=db, id=id)

@router.delete('/{id}', response_model=schemas.Tipo_Usuario)
def eliminar_tipo_usuario(id : int, db: Session = Depends(get_db)): 
    return service.eliminar_tipo_usuario(db=db, id=id)