from fastapi import FastAPI, Request, Response, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from controller.user import User

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
def user(request: Request):
    return RedirectResponse(url = "/") 
    #template.TemplateResponse("user.html", {"request": request})

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

    return RedirectResponse(url="/", status_code=302)