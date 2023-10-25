import json
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from app.flowmap.schemas import FlowmapBase


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


def set_flowmap(db: Session, new_data: FlowmapBase):
    new_node_json = json.dumps(new_data.node)
    new_edge_json = json.dumps(new_data.edge)

    query = text("UPDATE flowmap SET node = :new_node, edge = :new_edge;")
    db.execute(query, {"new_node": new_node_json, "new_edge": new_edge_json})
    db.commit()

    return {"node": new_data.node, "edge": new_data.edge}


# def get_industry_class_flowmap(db: Session, industryClassCode: int):
#     query = text(
#         "SELECT node, edge FROM flowmap WHERE industry_class_id = :industryClassCode"
#     )
#     result = db.execute(query, {"industryClassCode": industryClassCode}).first()
#     return result
