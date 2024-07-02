from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

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

