from sqlalchemy.orm import Session
from sqlalchemy.sql import text


def get_industry_class_list(db: Session):
    query = text(
        """
        SELECT
            d.code domain_code,
            d.name domain_name,
            d.seq domain_seq,
            d.division domain_division,
            ic.code industry_class_code, 
            ic.name industry_class_name,
            ic.type industry_class_type,
            ic.seq_list industry_class_seq_list,
            ic.seq_grid industry_class_seq_grid
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
            subclass_major.name AS subclass_major_name,
            subclass_major.seq_list AS subclass_major_seqlist,
            subclass_minor.code AS subclass_minor_code,
            subclass_minor.name AS subclass_minor_name,
            subclass_minor.subclass_major_code as subclass_minor_majorcode,
            subclass_minor.seq_list as subclass_minor_seqlist,
            subclass_minor.seq_grid as subclass_minor_seqgrid
        FROM
            industry_class AS ic
        LEFT JOIN
            domain AS d ON ic.domain_code = d.code
        LEFT JOIN
            subclass_major ON subclass_major.industry_class_code = ic.code
        LEFT JOIN
            subclass_minor ON subclass_minor.industry_class_code = ic.code;
        """
    )
    result = db.execute(query).all()
    return result
