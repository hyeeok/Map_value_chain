import json

from app.flowmap.schemas import FlowmapBase
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


def set_flowmap(db: Session, new_data: FlowmapBase):
    new_node_json = json.dumps(new_data.node)
    new_edge_json = json.dumps(new_data.edge)

    query = text("UPDATE flowmap SET node = :new_node, edge = :new_edge;")
    db.execute(query, {"new_node": new_node_json, "new_edge": new_edge_json})
    db.commit()

    return {"node": new_data.node, "edge": new_data.edge}


def get_industry_class_flowmap(db: Session, industryClassCode: int):
    query = text(
        """
        WITH Code AS (
            SELECT code
            FROM domain
            WHERE id = :industryClassCode
        )

        SELECT
            (
                SELECT jsonb_agg(node_data.node) AS node
                FROM (
                    SELECT jsonb_array_elements(node) AS node
                    FROM flowmap
                ) AS node_data
                WHERE node_data.node->>'id' = (SELECT code FROM Code)
        ) AS node,
        (
            SELECT jsonb_agg(edge_data.edge) AS edge
            FROM (
                SELECT jsonb_array_elements(edge) AS edge
                FROM flowmap
            ) AS edge_data
            WHERE edge_data.edge->>'id' = (SELECT code FROM Code)
        ) AS edge;
        """
    )
    result = db.execute(query, {"industryClassCode": industryClassCode}).first()


# def get_industry_class_flowmap(db: Session, industryClassCode: int):
#     query = text(
#         "SELECT node, edge FROM flowmap WHERE industry_class_id = :industryClassCode"
#     )
#     result = db.execute(query, {"industryClassCode": industryClassCode}).first()
#     return result


def get_domain_list(db: Session):
    query = text(
        """
        SELECT
            d.id, d.code, d.name,
            JSON_AGG(jsonb_build_object('id', c.id, 'code', c.code, 'name', c.name)) AS classes,
            JSON_AGG(jsonb_build_object('id', t.id, 'code', t.code, 'name', t.name)) AS themes
        FROM domain d
        INNER JOIN
            industry_class c ON d.id=c.domain_id AND c.type='C'
        INNER JOIN
            industry_class t ON d.id=t.domain_id AND t.type='T'
        GROUP BY
            d.id, d.code, d.name;
        """
    )
    result = db.execute(query).all()
    return result
