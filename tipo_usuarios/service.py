from sqlalchemy.orm import Session
from schemas import Respuesta
from une import transformar
import tipo_usuarios.models as models
import tipo_usuarios.schemas as schemas

def crear_tipo_usuario(db: Session, tipo_usuario: schemas.Tipo_UsuarioCrear):
    db_tipo_usuario = models.Tipo_Usuario(
        nombre=tipo_usuario.nombre, 
        descripcion=tipo_usuario.descripcion)
    db.add(db_tipo_usuario)
    db.commit()
    db.refresh(db_tipo_usuario)
    tipo_usuario_nuevo = schemas.Tipo_Usuario(
        id=db_tipo_usuario.id, 
        nombre=db_tipo_usuario.nombre, 
        descripcion=db_tipo_usuario.descripcion
    )
    respuesta = Respuesta[schemas.Tipo_Usuario](
        ok = True, 
        mensaje = 'Created user type', 
        data = tipo_usuario_nuevo
    )
    return respuesta

def listar_tipos_usuarios(db: Session): 
    return db.query(models.Tipo_Usuario).all()

def buscar_tipo_usuario(db: Session, id: int): 
    tipo_usuario = db.query(models.Tipo_Usuario).filter(models.Tipo_Usuario.id == id).first()
    return tipo_usuario

def eliminar_tipo_usuario(db: Session, id: int): 
    tipo_usuario = db.query(models.Tipo_Usuario).filter(models.Tipo_Usuario.id == id).first()
    db.delete(tipo_usuario)
    db.commit()
    return tipo_usuario