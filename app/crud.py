from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, data: schemas.UserCreate):
    user = models.User(name=data.name, email=data.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_users(db: Session):
    return db.query(models.User).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user

def update_user(db: Session, user_id: int, data: schemas.UserUpdate):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        return None

    if data.name is not None:
        user.name = data.name

    if data.email is not None:
        user.email = data.email

    db.commit()
    db.refresh(user)
    return user
