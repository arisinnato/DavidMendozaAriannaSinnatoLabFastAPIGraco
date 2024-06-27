from pydantic import BaseModel, field_validator
from typing import Union
from datetime import datetime
from email_validator import validate_email, EmailNotValidError

<<<<<<< HEAD


=======
>>>>>>> 3de6dc9 (Avances David)
class UsuarioBase(BaseModel):
    cedula: str
    nombres: str
    apellidos: str
    nacimiento: datetime
    direccion: str
    correo: str
    contraseña: str
    tipo_id: int

<<<<<<< HEAD

=======
>>>>>>> 3de6dc9 (Avances David)
    @field_validator('correo')
    def validacion(cls, correo): 
        try: 
            validado = validate_email(correo)
            correo = validado.email
            return correo
        except EmailNotValidError as e: 
<<<<<<< HEAD
            raise ValueError('El email no es válido')
=======
            raise ValueError('email')
>>>>>>> 3de6dc9 (Avances David)


class UsuarioCrear(UsuarioBase):
    pass

class Usuario(UsuarioBase):

    class Config:
<<<<<<< HEAD
        orm_mode = True


=======
        orm_mode = True
>>>>>>> 3de6dc9 (Avances David)
