import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = f"postgresql://{os.environ.get('PIZZA_USER')}:{os.environ.get('PIZZA_PASSWORD')}" \
               f"@{os.environ.get('PIZZA_HOST')}:{os.environ.get('PIZZA_PORT')}/{os.environ.get('PIZZA_NAME')}"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
