from fastapi import FastAPI
import random


app = FastAPI()

@app.get("/esta e a segunda alteracao")
async def root():
    return {"message": "hello word"}

@app.get("/teste0002")
async def funcaoteste():
    return {"teste": True, "deu certo": "deu tudo certo novamente"}

