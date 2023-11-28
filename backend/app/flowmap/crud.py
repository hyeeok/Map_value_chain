import json
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from app.flowmap.schemas import FlowmapCreate


def get_main_flowmap(db: Session):
    query = text(
        """
        SELECT node, edge FROM app_metadata.flowmap
        WHERE industry_class_id IS NULL
        """
    )
    result = db.execute(query).fetchone()
    return result


def put_main_flowmap(new_data: FlowmapCreate, db: Session):
    new_node_json = json.dumps(new_data.node)
    new_edge_json = json.dumps(new_data.edge)
    query = text(
        """
        UPDATE app_metadata.flowmap
        SET node = :new_node, edge = :new_edge
        WHERE industry_class_id IS NULL
        RETURNING id
        """
    )
    params = {"new_node": new_node_json, "new_edge": new_edge_json}
    try:
        result = db.execute(query, params).fetchone()
        db.commit()
        if result:
            flowmap_id = result[0]
            return flowmap_id
        else:
            return None

    except Exception as e:
        raise Exception(f"failed to update flowmap: {str(e)}")


def get_industry_class_list(db: Session):
    query = text(
        """
        SELECT
            ic.code AS industryClassCode,
            ic.name AS industryClassName,
            ic.id AS industryClassId,
            d.id AS domainId,
            d.name AS domainName,
            d.code AS domainCode
        FROM
            app_metadata.industry_class AS ic
        LEFT JOIN
            app_metadata.domain AS d ON ic.domain_id = d.id
    """
    )
    result = db.execute(query).all()
    return result


def get_flowmap(industry_class_id: int, db: Session):
    query = text(
        """
        SELECT
            (SELECT expanded_node
            FROM app_metadata.flowmap,
                LATERAL jsonb_array_elements(node) AS expanded_node
            WHERE industry_class_id IS NULL
                AND expanded_node->>'id' = (
                    SELECT code
                    FROM app_metadata.domain
                    WHERE id = (
                        SELECT domain_id
                        FROM app_metadata.industry_class
                        WHERE id = :industry_class_id
                    )
                )
            ) AS node,
            (SELECT expanded_edge
            FROM app_metadata.flowmap,
                LATERAL jsonb_array_elements(edge) AS expanded_edge
            WHERE industry_class_id IS NULL
                AND expanded_edge->>'id' = (
                    SELECT code
                    FROM app_metadata.domain
                    WHERE id = (
                        SELECT domain_id
                        FROM app_metadata.industry_class
                        WHERE id = :industry_class_id
                    )
                )
            ) AS edge;
    """
    )
    result = db.execute(query, {"industry_class_id": industry_class_id}).fetchone()
    return result


def put_flowmap(industry_class_id: int, new_data: FlowmapCreate, db: Session):
    new_node_json = json.dumps(new_data.node)
    new_edge_json = json.dumps(new_data.edge)
    query = text(
        """
        UPDATE app_metadata.flowmap
        SET node = :new_node, edge = :new_edge
        WHERE industry_class_id = :industry_class_id
        RETURNING id
        """
    )
    params = {
        "new_node": new_node_json,
        "new_edge": new_edge_json,
        "industry_class_id": industry_class_id,
    }
    try:
        result = db.execute(query, params).fetchone()
        db.commit()
        if result:
            flowmap_id = result[0]
            return flowmap_id
        else:
            return None

    except Exception as e:
        raise Exception(f"failed to update flowmap: {str(e)}")
