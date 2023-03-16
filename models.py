from sqlalchemy import Column, String, Integer, Numeric

from base import Base

class Drink(Base):

    __tablename__ = 'drinks'

    id=Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Numeric)

    def __init__(self, name, price):
        self.name = name
        self.price = price