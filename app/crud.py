# app/crud.py
from sqlalchemy.orm import Session
from . import models, pydantic_models as schemas
from .security import get_password_hash

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Add this new function
def get_analyses_by_user(db: Session, user_id: int):
    return db.query(models.Analysis).filter(models.Analysis.owner_id == user_id).all()

def create_user(db: Session, user: schemas.UserCreate):
    #... (rest of the file is the same)
    hashed_password = get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user