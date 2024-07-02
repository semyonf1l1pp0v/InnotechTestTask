from fastapi import FastAPI
from fastapi.responses import RedirectResponse, PlainTextResponse

app = FastAPI()


@app.get("/")
def homepage():
    return RedirectResponse("/login")


@app.get("/login")
def redirect_to_login():
    return PlainTextResponse("You have been successfully redirected")

