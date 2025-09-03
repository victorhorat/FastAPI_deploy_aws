from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    user: str

@app.post("/auth/me")
def auth_me(user: User):
    """
    Recebe um usuário e retorna o mesmo junto com um 'ping-pong'.
    """
    return {"user": user.user, "ping": "pong"}

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à sua API FastAPI!"}