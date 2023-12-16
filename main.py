from fastapi import FastAPI, Request, Response, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from controller.user import User
from lib.check_password import check_user, check_user_id
from model.handle_db import HandleDB


app  = FastAPI()    # Instancia de FastAPI
template = Jinja2Templates(directory="./view")  # Instancia de Jinja2Templates


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
def root(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
def register(request: Request):
    return template.TemplateResponse("register.html", {"request": request})

@app.get("/user", response_class=HTMLResponse)
def user(request: Request):
    return RedirectResponse(url = "/", status_code=302) 

#Leer   
@app.post("/user", response_class=HTMLResponse)
def user(request: Request, username: str = Form(), password_user: str = Form()):
    verify_user = check_user(username, password_user)
    if verify_user:
        return template.TemplateResponse("user.html", {"request": request, "data_user": verify_user})
    return RedirectResponse(url = "/", status_code=302)
   
#Crear
@app.post("/create_user")
def data_processing(firstname: str = Form(), lastname: str = Form(), username: str = Form(), password_user: str = Form()):
    
    data_user = {
        "firstname": firstname,
        "lastname": lastname,
        "username": username,
        "password_user": password_user
    }
    db = User(data_user)
    db.create_user()
    return RedirectResponse(url="/", status_code=302)

#Eliminar
@app.post("/delete_user")
def delete_user(user_id: str = Form(...), current_password: str = Form(...)):
    # Verificar la contraseña antes de eliminar al usuario
    verify_user = check_user_id(user_id, current_password)
    if verify_user:
        db = HandleDB()
        db.delete_user_by_id(user_id)
        return RedirectResponse(url="/")
    return "invalid password"

#Actualizar
@app.post("/update_password")
def update_password(user_id: str = Form(...), current_password: str = Form(...), new_password: str = Form(...)):
    verify_user = check_user_id(user_id, current_password)
    if verify_user:
        db = HandleDB()
        db.update_password_for_user(user_id, new_password)
        return RedirectResponse(url="/")    
    return "invalid password"
    