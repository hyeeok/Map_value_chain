from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import Dict, List, Union


def get_company_basic(term: str, category: str, db: Session):
    query = text(
        f"""
        SELECT name, registration_number, corporate_type, stock_code, 
            subsidiary_mock, ceo_name, establishment_date, region, website
        FROM company
        WHERE {category} ILIKE :term;
        """
    )
    param = {"term": f"%{term}%"}
    result = db.execute(query, param).all()
    return result


def get_company_items_by_category(
    term: str, category: str, db: Session
) -> List[Dict[str, Union[int, str]]]:
    query = text(
        f"SELECT id, {category}, name FROM company WHERE {category} ILIKE :term"
    )
    param = {"term": f"%{term}%"}
    result = db.execute(query, param).fetchall()

    if category == "name":
        items = [{"id": row[0], "name": row[1]} for row in result]
    else:
        items = [{"id": row[0], category: row[1], "name": row[2]} for row in result]

    return items


def get_deps(db: Session):
    query = text(
        """
        SELECT 
            ic.id AS industryClassId,
            ic.name AS industryClassName,
            ic.code AS industryClassCode,
            d.id AS domainId,
            d.name AS domainName,
            d.code AS domainCode,
            deps.id AS subClassId,
            deps.code AS subClassCode,
            deps.name AS subClassName,
            deps.level AS subClassLevel
        FROM 
            industry_class AS ic
        LEFT JOIN 
            domain AS d ON ic.domain_id = d.id
        LEFT JOIN   
            deps ON deps.industry_class_code = ic.code;
        """
    )
    result = db.execute(query).all()
    return result
