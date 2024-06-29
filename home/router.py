from fastapi import Request, Depends, APIRouter
from database import SessionLocal 
from fastapi.templating import Jinja2Templates
from usuarios.service import listar_artesanos, AuthHandler
from productos.service import get_productos_por_artesano
from sqlalchemy.orm import Session

auth_handler = AuthHandler()

router = APIRouter()

templates = Jinja2Templates(directory="../templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/home')
def homes(request: Request, db: Session = Depends(get_db), info=Depends(auth_handler.auth_wrapper)):
        print(info)
        if info["tipo_usuario_id"] == 1: 
            lista = get_productos_por_artesano(db=db, cedula_artesano=info['cedula'])
            print(lista)
            lista_imagenes = []
            for esto in lista.data: 
                real = bytes(esto.imagen).decode()
                lista_imagenes.append(real)
            return templates.TemplateResponse('/homes/artesanos.html', 
                                              {'request': request, 
                                               "info": info, 
                                               'lista': lista.data, 
                                               'imagenes': lista_imagenes})
        elif info["tipo_usuario_id"] == 2: 
            lista = listar_artesanos(db=db)
            return templates.TemplateResponse('/homes/clientes.html', 
                                              {'request': request, 
                                               "info": info, 
                                               'lista': lista})
        else: 
            return {'yoloso': info}