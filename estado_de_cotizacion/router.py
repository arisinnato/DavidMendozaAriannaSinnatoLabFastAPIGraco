from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine #!aaaaaaa
import estado_de_cotizacion.models as models 
import estado_de_cotizacion.schemas as schemas
import estado_de_cotizacion.service as service

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
    return {"message":"yolooooo"}

@router.post('', response_model=schemas.Estado_Cotizacion)
def crear_estado_cotizacion(estado_cotizacion: schemas.Estado_CotizacionCrear, db: Session = Depends(get_db)):
    return service.crear_estado_cotizacion(db=db, estado_cotizacion=estado_cotizacion)


