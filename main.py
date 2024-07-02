from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def homepage():
    with open("homepage.html", "r") as f:
        html_response = f.read()
    return html_response


@app.get("/login")
def redirect_to_login():
    return PlainTextResponse("You have been successfully redirected")

