import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv("DB_URL") or ""
SQLALCHEMY_DEV_DATABASE_URL = os.getenv("DEV_DB_URL") or ""

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

print(SQLALCHEMY_DATABASE_URL)
print(SQLALCHEMY_DEV_DATABASE_URL)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


def get_db(database_url: str):
    engine = create_engine(database_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_mvc_db():
    yield from get_db(SQLALCHEMY_DATABASE_URL)


def get_dev_db():
    yield from get_db(SQLALCHEMY_DEV_DATABASE_URL)
