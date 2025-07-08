##1. importar dependencias
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

##2. configuracion de las aplicaciones 
app = FastAPI()
from data import paises
templates = Jinja2Templates(directory="vistas")

##3. logica de negocios  
@app.get("/paises", response_class=
         HTMLResponse)
def prueba(request:Request):
    return templates.TemplateResponse("paises.html",
                                {"request":request,
                                 "paises":paises
                                 })