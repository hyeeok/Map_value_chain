from sqlalchemy.orm import Session
from sqlalchemy.sql import text


def get_industry_class_list(db: Session):
    query = text(
        """
        SELECT
            d.code domain_code,
            d.name domain_name,
            d.division domain_division,
            ic.code industry_class_code, 
            ic.name industry_class_name,
            ic.type industry_class_type
        FROM industry_class ic
        INNER JOIN domain d
        ON ic.domain_code = d.code
        """
    )
    result = db.execute(query).all()
    return result


def get_sub_class_list(db: Session):
    query = text(
        """
        SELECT
            ic.name AS industry_class_name,
            ic.code AS industry_class_code,
            d.name AS domain_name,
            d.code AS domain_code,
            sub_class.code AS sub_class_code,
            sub_class.name AS sub_class_name,
            sub_class.level AS sub_class_level
        FROM
            industry_class AS ic
        LEFT JOIN
            domain AS d ON ic.domain_code = d.code
        LEFT JOIN
            sub_class ON sub_class.industry_class_code = ic.code;
        """
    )
    result = db.execute(query).all()
    return result
