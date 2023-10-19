import os
from os.path import dirname, join

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()
DB_USER=os.environ.get("DB_USER")
DB_PASS=os.environ.get("DB_PASS")
DB_HOST=os.environ.get("DB_HOST")
DB_NAME=os.environ.get("DB_NAME")

SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}/{}".format(
    DB_USER,
    DB_PASS,
    DB_HOST,
    DB_NAME
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    SessionLocal()
    - 위에서 정의한 db 정보를 db에 주입
    - try tyield/finally 문을 사용해 마지막에 db를 종료해줌
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
