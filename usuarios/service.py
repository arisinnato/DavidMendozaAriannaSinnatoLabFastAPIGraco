from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from typing import Union
import usuarios.models as models
import usuarios.schemas as schemas
from sqlalchemy.orm import Session

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def obtener_hash(contraseña):
    return pwd_context.hash(contraseña)

def verificar_contraseña(contraseña_simple, contraseña_hasheada):
    return pwd_context.verify(contraseña_simple, contraseña_hasheada)

def registrar_usuario(db: Session, usuario: schemas.UsuarioCrear):
    hashed_password = obtener_hash(usuario.contraseña)
    db_usuario = models.Usuario(
        cedula=usuario.cedula,
        nombres=usuario.nombres,
        apellidos=usuario.apellidos,
        direccion=usuario.direccion,
        nacimiento=usuario.nacimiento,
        correo=usuario.correo,
        contraseña=hashed_password,
        tipo_id=usuario.tipo_id
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def autenticar_usuario(db: Session, cedula: str, contraseña: str):
    usuario = obtener_usuario(db, cedula)
    if not usuario:
        return False
    if not verificar_contraseña(contraseña, usuario.contraseña):
        return False
    return usuario

def crear_token_acceso(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def listar_usuarios(db: Session):
    return db.query(models.Usuario).all()

def buscar_usuario(db: Session, cedula: str):
    returned = db.query(models.Usuario).filter(models.Usuario.cedula == cedula).first()
    if returned is None:
        return {"ok": False, "mensaje": "User not found"}
    usuario = schemas.Usuario(
        cedula=returned.cedula,
        nombres=returned.nombres,
        apellidos=returned.apellidos,
        direccion=returned.direccion,
        nacimiento=returned.nacimiento,
        correo=returned.correo,
        contraseña=returned.contraseña,
        tipo_id=returned.tipo_id
    )
    return {"ok": True, "mensaje": "User found", "data": usuario}

def obtener_usuario(db: Session, cedula: str):
    return db.query(models.Usuario).filter(models.Usuario.cedula == cedula).first()

def eliminar_usuario(db: Session, cedula: str):
    usuario = obtener_usuario(db, cedula)
    if usuario:
        db.delete(usuario)
        db.commit()
        return usuario
    return None
