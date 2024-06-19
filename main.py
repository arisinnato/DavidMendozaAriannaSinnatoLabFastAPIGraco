from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from tipo_usuarios import router as tipos_usuario
from usuarios import router as usuarios


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="iniciar_sesion")

app.include_router(tipos_usuario.router, prefix='/tipos_usuarios')
app.include_router(usuarios.router)



@app.get('/')
def home():
    return {"message": "Hello"}