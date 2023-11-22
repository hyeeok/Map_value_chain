from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import Dict, List, Union


def get_company_overview(term: str, category: str, db: Session):
    query = text(
        f"""
        SELECT corp_code, firm, bizr_no, corp_cls, stock_code, 
            bsns_year, adres_1, adres_2
        FROM mvc_fake_data
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
        f"SELECT DISTINCT corp_code, {category}, firm FROM mvc_fake_data WHERE {category} ILIKE :term"
    )
    param = {"term": f"%{term}%"}
    result = db.execute(query, param).fetchall()

    if category == "firm":
        items = [{"corp_code": row[0], "firm": row[1]} for row in result]
    else:
        items = [
            {"corp_code": row[0], category: row[1], "firm": row[2]} for row in result
        ]

    return items


# def get_deps(db: Session):
#     query = text(
#         """
#         SELECT
#             ic.id AS industryClassId,
#             ic.name AS industryClassName,
#             ic.code AS industryClassCode,
#             d.id AS domainId,
#             d.name AS domainName,
#             d.code AS domainCode,
#             deps.id AS subClassId,
#             deps.code AS subClassCode,
#             deps.name AS subClassName,
#             deps.level AS subClassLevel
#         FROM
#             industry_class AS ic
#         LEFT JOIN
#             domain AS d ON ic.domain_id = d.id
#         LEFT JOIN
#             deps ON deps.industry_class_code = ic.code;
#         """
#     )
#     result = db.execute(query).all()
#     return result


def get_dart_corp_info(corp_code: str, db: Session):
    query = text(
        """
        SELECT
            stock_name,
            bizr_no,
            jurir_no,
            stock_code,
            corp_cls,
            corp_name,
            corp_name_eng,
            ceo_nm,
            est_dt,
            acc_mt   
        FROM
            source.dart_corp_info
        WHERE
            corp_code = :corp_code;
        """
    )
    param = {"corp_code": f"{corp_code}"}
    result = db.execute(query, param).fetchone()
    return result


def get_openapi_outline_data(crno: str, db: Session):
    query = text(
        """
        SELECT
            enpkosdaqlstgdt,
            enpxchglstgdt,
            enpkosdaqlstgaboldt,
            enpkrxlstgdt,
            enpkrxlstgaboldt,
            enpempecnt,
            empeavgcnwktermctt,
            enppn1avgslryamt,
            actnaudpnnm,
            audtrptopnnctt,
            enpmainbiznm
        FROM
            source.openapi_corp_outline
        WHERE
            crno = :crno;
        """
    )

    param = {"crno": f"{crno}"}
    result = db.execute(query, param).all()
    return result


def get_openapi_affiliate_data(crno: str, db: Session):
    query = text(
        """
        SELECT
            afilcmpynm 
        FROM
            source.openapi_corp_affiliate
        WHERE
            crno = :crno;
        """
    )

    param = {"crno": f"{crno}"}
    result = db.execute(query, param).all()
    return result
