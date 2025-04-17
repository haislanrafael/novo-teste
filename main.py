from fastapi import FastAPI
import random


app = FastAPI()

@app.get("/teste0003")
async def root():
    return {"message": "Olá, Mundo!"}

@app.get("/teste0003")
async def funcaoteste():
    return {"teste": "testando novamente"}



