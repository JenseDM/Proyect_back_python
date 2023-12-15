from fastapi import FastAPI, Request, Response, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from controller.user import User
from lib.check_password import check_user
from model.handle_db import HandleDB

app  = FastAPI()
template = Jinja2Templates(directory="./view")

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
def root(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

@app.get("/signup", response_class=HTMLResponse)
def signup(request: Request):
    return template.TemplateResponse("signup.html", {"request": request})

@app.get("/user", response_class=HTMLResponse)
def user(request: Request):
    return RedirectResponse(url = "/") 
    #template.TemplateResponse("user.html", {"request": request})
@app.post("/user", response_class=HTMLResponse)
def user(request: Request, username: str = Form(), password_user: str = Form()):
    verify_user = check_user(username, password_user)
    if verify_user:
        return template.TemplateResponse("user.html", {"request": request, "data_user": verify_user})
    return RedirectResponse(url = "/")
   
#endpoint para procesar los datos del formulario e insertarlos en la base de datos (insert)
@app.post("/data-processing")
def data_processing(firstname: str = Form(), lastname: str = Form(), username: str = Form(), password_user: str = Form()):
    
    data_user = {
        "firstname": firstname,
        "lastname": lastname,
        "username": username,
        "password_user": password_user
    }
    db = User(data_user)
    db.create_user()
    return RedirectResponse(url="/signup", status_code=302)

#se simula un metodo delete ya que los formularios solo soportan get y post
@app.post("/delete_user")
def delete_user(user_id: str = Form(...)):
    db = HandleDB()
    db.delete_user_by_id(user_id)
    return RedirectResponse(url="/")  

#se simula un metodo put ya que los formularios solo soportan get y post
@app.post("/update_password")
def update_password(user_id: str = Form(...), new_password: str = Form(...)):
    db = HandleDB()
    db.update_password_for_user(user_id, new_password)
    return RedirectResponse(url="/")    