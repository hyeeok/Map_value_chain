from sqlalchemy.orm import Session
from sqlalchemy.sql import text


def get_industries(db: Session):
    query = text("SELECT * FROM industry;")
    result = db.execute(query).all()
    return result


# def get_industries(db: Session):
#     result = db.query(models.Industry, models.Domain)
