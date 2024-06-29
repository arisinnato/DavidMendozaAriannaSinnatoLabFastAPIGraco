from pydantic import BaseModel, field_validator
from typing import Union
from datetime import datetime
from email_validator import validate_email, EmailNotValidError

class el_Usuario_Base(BaseModel):
    cedula: str
    nombres: str
    apellidos: str
    nacimiento: datetime
    direccion: str
    correo: str
    contraseña: str
    tipo_id: int

    @field_validator('correo')
    def validacion(cls, correo): 
        try: 
            validado = validate_email(correo)
            correo = validado.email
            return correo
        except EmailNotValidError as e: 
            raise ValueError('email invalido')


class Usuario_para_Crear(el_Usuario_Base):
    pass

class Usuario(el_Usuario_Base):

    class Config:
        orm_mode = True


