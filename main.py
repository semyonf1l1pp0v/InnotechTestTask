from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import bcrypt

users_db = {"admin":
                {"username": "admin",
                 "hashed_password": bcrypt.hashpw(password="admin".encode(), salt=bcrypt.gensalt())
                 }
            }

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def homepage():
    with open("homepage.html") as file:
        html_response = file.read()
    return html_response


@app.get("/login", response_class=HTMLResponse)
def authpage():
    with open("authform.html") as file:
        html_response = file.read()
    return html_response


@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    if username == users_db["admin"]["username"] and bcrypt.checkpw(password.encode(),
                                                                    users_db["admin"]["hashed_password"]):
        pass
    else:
        with open("homepage.html") as file:
            html_response = file.read()
        return HTMLResponse(content=html_response)


@app.get("/appsec")
def appsec_main():
    return "Appsec here"
