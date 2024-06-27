from fastapi import APIRouter, Depends, Request, Form, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import cotizaciones.models as models 
import cotizaciones.schemas as schemas
import cotizaciones.service as service
from schemas import Respuesta

from exceptions import NoArtesanoException, NoClienteException, Message_Redirection_Exception
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

@router.get('', response_model=list[schemas.Cotizacion])
def listar_cotizaciones(db: Session = Depends(get_db)):
    return service.listar_cotizaciones(db=db)

@router.get('/compra/{id}', response_model=Respuesta[list[schemas.Cotizacion]])
def listar_cotizaciones(id: int, db: Session = Depends(get_db), info=Depends(auth_handler.auth_wrapper)):
    return service.listar_cotizaciones_compras(db=db, id=id)

@router.post('/aprobar/{id}', response_model=Respuesta[schemas.Cotizacion])
def aprobar_cotizacion(id: int, db: Session = Depends(get_db), info=Depends(auth_handler.auth_wrapper)):
    return service.aprobar_cotizacion(db=db, id=id)

@router.get('/solicitar/{id}')
def solicitar_cotizacion(request: Request, 
                    nombre: str = Form(...), 
                    descripcion: str = Form(...), 
                    db: Session = Depends(get_db),
                    info=Depends(auth_handler.auth_wrapper)):
    
    if info["tipo_usuario_id"] != 2: 
             raise NoClienteException()
    
@router.post('', response_model=Respuesta[schemas.Cotizacion])
def solicitar_cotizacion(cotizacion=schemas.CotizacionCrear, db: Session = Depends(get_db), info=Depends(auth_handler.auth_wrapper)):
    return service.crear_cotizacion(db=db, cotizacion=cotizacion)

@router.post('/rechazar/{id}', response_model=Respuesta[schemas.Cotizacion])
def rechazar_cotizacion(id: int, db: Session = Depends(get_db), info=Depends(auth_handler.auth_wrapper)):
    return service.rechazar_cotizacion(db=db, id=id)

@router.get('/{id}', response_model=Respuesta[schemas.Cotizacion])
def buscar_cotizacion(id : int, db: Session = Depends(get_db), info=Depends(auth_handler.auth_wrapper)): 
    return service.buscar_cotizacion(db=db, id=id)

@router.put('/{id}', response_model=schemas.Cotizacion)
def modificar_cotizacion(id : int, cotizacion: schemas.CotizacionCrear, db: Session = Depends(get_db), info=Depends(auth_handler.auth_wrapper)): 
    return service.modificar_cotizacion(db=db, id=id, cotizacion=cotizacion)

@router.delete('/{id}', response_model=schemas.Cotizacion)
def eliminar_cotizacion(id : int, db: Session = Depends(get_db)): 
    return service.eliminar_cotizacion(db=db, id=id)