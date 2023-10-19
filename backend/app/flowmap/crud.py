from sqlalchemy.orm import Session
from sqlalchemy.sql import text


def get_industry_class_list(db: Session):
    query = text("select * from industry_class;")
    result = db.execute(query).all()
    return result


def insert_domain(domain_code: str, domain_name: str, db: Session):
    query = text(
        """
        INSERT INTO domain (code, name)
        VALUES (:code, :name)
        RETURNING id
        """
    )
    result = db.execute(query, {"code": domain_code, "name": domain_name}).fetchone()
    print(result)
    return result


def get_domain_id_by_domain_code(domain_code: str, db: Session):
    query = text(
        """"
        SELECT id FROM domain
        WHERE code=:code
        """
    )
    result = db.execute(query, {"code": domain_code}).fetchone()
    print(result)
    return result


def insert_industry_class(db: Session):
    return
