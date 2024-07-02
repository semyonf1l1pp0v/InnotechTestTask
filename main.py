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

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"


def check_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password, hashed_password)


def authenticate_user(username, plain_password, hashed_password):
    if username == users_db["admin"]["username"] and check_password(plain_password, hashed_password):
        return users_db["admin"]["username"]
    else:
        return False


def create_access_token(data):
    to_encode = data.copy()
    jwt_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return jwt_token


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
