from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import bcrypt

users_db = {"admin":
                {"username": "admin",
                 "hashed_password": bcrypt.hashpw(password="admin".encode(), salt=bcrypt.gensalt())
                 }
            }

app = FastAPI()


def open_html(filename):
    with open(filename) as file:
        html_response = file.read()
    return HTMLResponse(content=html_response)


@app.get("/", response_class=HTMLResponse)
def homepage():
    return open_html("homepage.html")


@app.get("/login", response_class=HTMLResponse)
def authpage():
    return open_html("authform.html")


@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    if username == users_db["admin"]["username"] and bcrypt.checkpw(password.encode(),
                                                                    users_db["admin"]["hashed_password"]):
        return open_html("correct_cred.html")
    else:
        return open_html("incorrect_cred.html")


@app.get("/appsec")
def appsec_main():
    return open_html("appsec.html")
