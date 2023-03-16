from base import SessionLocal, engine, Base
from models import Drink

Base.metadata.create_all(engine)

session = SessionLocal()

fuze_tea = Drink("Fuze Tea", 1.50)
ice_tea = Drink("Ice Tea", 1.65)

session.add(fuze_tea)
session.add(ice_tea)

session.commit()
session.close()