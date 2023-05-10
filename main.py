from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

posts = []

class Dato(BaseModel):
    id: str
    value: int
    registered_at : datetime = datetime.now()


@app.get("/")
def index():
    return "Basic API to test data reception from edge devices." 

@app.get("/datos")
def show_data():
    return posts[-1]

@app.post("/datos")
def insert_data(dato : Dato):
    posts.append(dato.dict())

    return "Received"
