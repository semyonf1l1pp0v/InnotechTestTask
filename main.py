from fastapi import FastAPI, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordBearer
import jwt
import bcrypt

users_db = {"admin":
                {"username": "admin",
                 "hashed_password": bcrypt.hashpw(password="admin".encode(), salt=bcrypt.gensalt())
                 }
            }


def check_password():
    pass


def create_access_token():
    pass


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def homepage():
    with open("homepage.html", "r") as f:
        html_response = f.read()
    return html_response


@app.get("/login", response_class=HTMLResponse)
def authpage():
    with open("authform.html", "r") as f:
        html_response = f.read()
    return html_response


@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    if username == 'admin' and password == 'admin':
        return "Hell yeah"
    else:
        return "Not hell yeah"
