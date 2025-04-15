from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.repositories import user_repo
from app.schemas import user_schema
from app.services import user_service

router = APIRouter(prefix="/users", tags=["Users"])



@router.get("/")
def list_users(db: Session = Depends(get_db)):
    return user_repo.get_all_users(db)

@router.get("hello")
def hello_world():
    return {"message": "Hello World!"}

@router.post('/create-user', response_model=user_schema.CreateUserResponse)
def create_user(user: user_schema.CreateUserRequest, db: Session = Depends(get_db)):
    """
    Create a new user.
    """
    return user_service.create_user(db, user)