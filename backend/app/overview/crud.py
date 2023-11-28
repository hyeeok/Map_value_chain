from typing import Dict, List, Union

from sqlalchemy.orm import Session
from sqlalchemy.sql import text


def get_overview_list(
    category: str | None, keyword: str | None, limit: int, page: int, db: Session
):
    query_condition = ""
    params = {}

    if category or keyword:
        query_condition = f"WHERE {category} ILIKE :keyword"
        params["keyword"] = f"%{keyword}%"

    query = text(
        f"""
        SELECT corp_code, firm, bizr_no, corp_cls, stock_code,
            bsns_year, adres_1, adres_2
        FROM mvc_fake_data
        {query_condition}
        LIMIT :limit OFFSET (:page - 1) * :limit
        """
    )
    params.update({"limit": limit, "page": page})
    result = db.execute(query, params).all()

    count_query = text(
        f"""
        SELECT COUNT(*) AS total_count
        FROM mvc_fake_data
        {query_condition}
        """
    )
    total_count = db.execute(count_query, params).scalar()

    return result, total_count


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
            app_metadata.industry_class AS ic
        LEFT JOIN
            app_metadata.domain AS d ON ic.domain_id = d.id
        LEFT JOIN
            app_metadata.deps ON deps.industry_class_code = ic.code;
        """
    )
    result = db.execute(query).all()
    return result


def get_dart_corp_info(corp_code: str, db: Session):
    query = text(
        """
        SELECT stock_name, stock_code, bizr_no, jurir_no,
            corp_name, corp_name_eng, corp_cls,
            est_dt, hm_url, phn_no, adres, ceo_nm, acc_mt
        FROM source.dart_corp_info
        WHERE corp_code = :corp_code
        """
    )
    result = db.execute(query, {"corp_code": corp_code}).fetchone()
    return result


def get_openapi_outline(crno: str, db: Session):
    query = text(
        """
        SELECT enpxchglstgdt, enpxchglstgaboldt,
            enpkosdaqlstgdt, enpkosdaqlstgaboldt,
            enpkrxlstgdt, enpkrxlstgaboldt,
            smenpyn, enpempecnt, enppn1avgslryamt,
            actnaudpnnm, enpmainbiznm, audtrptopnnctt
        FROM source.openapi_corp_outline
        WHERE crno = :crno
        ORDER BY lastopegdt DESC
        LIMIT 1;
        """
    )
    result = db.execute(query, {"crno": crno}).fetchone()
    return result


def get_openapi_affiliate_list(crno: str, db: Session):
    query = text(
        """
        SELECT afilcmpynm, afilcmpycrno
        FROM source.openapi_corp_affiliate
        WHERE crno = :crno
        """
    )
    result = db.execute(query, {"crno": crno}).all()
    return result


def get_openapi_sub_company_list(crno: str, db: Session):
    query = text(
        """
        SELECT sbrdenpnm
        FROM source.openapi_subs_comp
        WHERE crno=:crno
        """
    )
    result = db.execute(query, {"crno": crno}).all()
    return result


def get_corp_cls(corp_code: str, db: Session):
    query = text(
        "select corp_cls from source.dart_corp_info where corp_code = :corp_code"
    )

    param = {"corp_code": f"{corp_code}"}
    result = db.execute(query, param).fetchone()
    return result
