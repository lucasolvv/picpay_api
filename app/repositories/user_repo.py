from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import CreateUserRequest, CreateUserResponse
from app.config.database import get_db

def create_user(user: CreateUserRequest, db: Session) -> CreateUserResponse:
    db_user = User(
        username=user.username,
        full_name=user.full_name,
        email=user.email,
        password=user.password,  # Ensure to hash the password in a real application
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return CreateUserResponse.from_orm(db_user)


