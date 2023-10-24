import json
from sqlalchemy.orm import Session
from sqlalchemy.sql import text


def get_industry_class_list(db: Session):
    query = text(
        """
        SELECT industry_class.*, domain.name AS domain_name, domain.code AS domain_code 
        FROM industry_class LEFT JOIN domain 
        ON industry_class.domain_id = domain.id;
        """
    )
    result = db.execute(query).all()
    return result


def get_flowmap(db: Session):
    query = text("SELECT node, edge FROM flowmap;")
    result = db.execute(query).all()
    return {"node": result[0][0], "edge": result[0][1]}


# def set_flowmap(db: Session, new_node: json, new_edge: json, domainId: int):
#     query = text(
#         "UPDATE flowmap SET node = :new_node, edge = :new_edge WHERE domain_id = :domainId;"
#     )


# def get_industry_class_flowmap(db: Session, industryClassCode: int):
#     query = text(
#         "SELECT node, edge FROM flowmap WHERE industry_class_id = :industryClassCode"
#     )
#     result = db.execute(query, {"industryClassCode": industryClassCode}).first()
#     return result
