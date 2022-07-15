from sqlalchemy import Column, Integer, String, DateTime

from db import Base
import datetime


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    create_date = Column(DateTime, default=datetime.datetime.now())
