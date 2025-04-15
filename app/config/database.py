from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  if DATABASE_URL.startswith("sqlite") else {},
)

Session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = Session_local()
    try:
        yield db
    finally:
        db.close()