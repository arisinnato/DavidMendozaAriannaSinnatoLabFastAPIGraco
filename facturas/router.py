from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import facturas.models as models 
import facturas.schemas as schemas
import facturas.service as service
from schemas import Respuesta

from usuarios.service import AuthHandler
auth_handler = AuthHandler()

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('', response_model=list[schemas.Factura])
def listar_facturas(db: Session = Depends(get_db)):
    return service.listar_facturas(db=db)

@router.get('/cotizacion/{id}', response_model=Respuesta[list[schemas.Factura]])
def listar_facturas_cotizacion(id: int, db: Session = Depends(get_db), info=Depends(auth_handler.auth_wrapper)):
    return service.listar_facturas_cotizaciones(db=db, id=id)

@router.post('', response_model=schemas.Factura)
def crear_factura(factura: schemas.FacturaCrear, db: Session = Depends(get_db), info=Depends(auth_handler.auth_wrapper)):
    return service.crear_factura(db=db, factura=factura)

@router.get('/{id}', response_model=schemas.Factura)
def buscar_factura(id : int, db: Session = Depends(get_db), info=Depends(auth_handler.auth_wrapper)): 
    return service.buscar_factura(db=db, id=id)
