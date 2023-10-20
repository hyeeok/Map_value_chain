from sqlalchemy.orm import Session
from sqlalchemy.sql import text


def get_industry_class_list(db: Session):
    query = text("select * from industry_class;")
    result = db.execute(query).all()
    return result


def get_flowmap_list(db: Session):
    query = text("select node, edge, industry_class_id from flowmap;")
    result = db.execute(query).all()
    return result
