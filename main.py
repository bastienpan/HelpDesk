from enum import Enum

from fastapi import FastAPI, Depends, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine,text
from sqlalchemy.orm import Session
from base import SessionLocal
from models import Drink
import models, schemas, crud

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

fake_items_db = [{"item_name": "foo"}, {"item_name": "bar"}, {"item_name": "baz"}]
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/")
async def root():
    return {"message" : "Hello World"}


@app.post("/create/")
async def create_item(item : schemas.Item):
    return item

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item id" : item_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name" : model_name, "message" : "this is alexnet"}
    if model_name is ModelName.lenet:
        return {"model_name" : model_name, "message" : "this is lenet"}
    if model_name.value == "resnet":
        return {"model_name" : model_name, "message" : "this is resnet"}
    

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path" : file_path}


@app.get("/drinks/", response_model=list[schemas.Drink])
def read_drinks(response: Response, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_drinks = crud.get_drinks(db, skip = skip, limit = limit)
    response.headers["Access-Control-Expose-Headers"] = "X-Total-Count"
    response.headers["X-Total-Count"] = str(len(db_drinks))
    return db_drinks

@app.get("/drinks/{drink_id}", response_model=schemas.Drink)
def read_drink(drink_id: int, db : Session = Depends(get_db)):
    db_drink = crud.get_drink(db = db, drink_id=drink_id)
    return db_drink


