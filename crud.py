from sqlalchemy.orm import Session

import models, schemas

def get_drinks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Drink).offset(skip).limit(limit).all()

def get_drink(db: Session, drink_id: int):
    return db.query(models.Drink).filter(models.Drink.id == drink_id).first()