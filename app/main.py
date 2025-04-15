from fastapi import FastAPI
from app.routers import user_router 
from app.config.database import engine
from app.config.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router.router, prefix="/user", tags=["user"])