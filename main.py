from fastapi import FastAPI
import random


app = FastAPI()

@app.get("/teste01")
async def root():
    return {"message": "Olá, Mundo!"}

@app.get("/teste1")
async def funcaoteste():
    return {"teste": "deu certo"}

