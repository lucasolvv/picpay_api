from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: str

class CreateUserRequest(UserBase):
    full_name: str
    password: str
    email: EmailStr

class CreateUserResponse(UserBase):
    full_name: str 

    class Config:
        orm_mode = True

