from fastapi import FastAPI, Form, Depends, HTTPException, status, Response
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


def create_access_token(data):
    to_encode = data.copy()
    jwt_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return jwt_token


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


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
def login(response: Response, username: str = Form(...), password: str = Form(...)):
    if username == users_db["admin"]["username"] and bcrypt.checkpw(password.encode(),
                                                                    users_db["admin"]["hashed_password"]):
        print("Success")
        access_token = create_access_token(data={"sub": users_db["admin"]["username"]})
        response.headers["Authorization"] = f"Bearer {access_token}"
        return content(token=access_token)
    else:
        return False


@app.get("/content")
def content(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        token_data = username
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return f"Hi {token_data}"

