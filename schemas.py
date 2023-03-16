from pydantic import BaseModel

class DrinkBase(BaseModel):
    name: str
    price: float

class DrinkCreate(DrinkBase):
    pass

class Drink(DrinkBase):
    id: int

    class Config:
        orm_mode = True


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

