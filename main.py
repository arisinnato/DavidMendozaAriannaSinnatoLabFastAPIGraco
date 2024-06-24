from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from tipo_usuarios import router as tipos_usuario
from usuarios import router as usuarios
from usuarios.router import router as usuarios_router


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="iniciar_sesion")

app.include_router(tipos_usuario.router, prefix='/tipos_usuarios')
app.include_router(usuarios.router)

app.include_router(usuarios_router, prefix="/usuarios")

@app.get('/')
def home(request: Request):
    return templates.TemplateResponse("home_no_logeado.html", {"request": request, "title": "Inicio"})