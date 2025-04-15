from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.config.base import Base
import datetime

class User(Base):
    __tablename__= "User"

    ID = Column(Integer, primary_key=True, index=True)
    FULL_NAME = Column(String, unique=True, index=True)
    EMAIL = Column(String, unique=True, index=True)
    PASSWORD_HASH = Column(String)
    ROLE = Column(String)
    CREATED_AT = Column(DateTime, default=datetime.utcnow)
    UPDATED_AT = Column(DateTime)

