from sqlalchemy.orm import Session
from sqlalchemy.sql import text


def get_industry_class_list(db: Session):
    query = text("select * from industry_class;")
    result = db.execute(query).all()
    return result


def get_flowmap(db: Session):
    query = text("select * from flowmap where industry_class_id is null;")
    result = db.execute(query).fetchone()
    print(result)
    return result
