from sqlalchemy.orm import Session
from app.schemas.user_schema import CreateUserRequest, CreateUserResponse
from app.models.user import User
from app.repositories import user_repo
from passlib import bcrypt 

def create_user(db: Session, user: CreateUserRequest) -> CreateUserResponse:
    
    hashed_password = bcrypt.hash(user.password)
    user.password = hashed_password

    new_user = User(**user.model_dump())
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return CreateUserResponse.model_validate(new_user)  # Use from_orm for Pydantic model conversion