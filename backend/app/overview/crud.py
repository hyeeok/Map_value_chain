from typing import Dict, List, Union

from sqlalchemy.orm import Session
from sqlalchemy.sql import text


def get_overview_list(
    category: str | None, keyword: str | None, limit: int, page: int, db: Session
):
    query_condition = ""
    params = {}

    if keyword:
        if category == "stock_name":
            query_condition = f"""
            WHERE stock_name ILIKE :keyword
            OR corp_name ILIKE :keyword
            OR corp_name_eng ILIKE :keyword
            """
        else:
            query_condition = f"WHERE {category} ILIKE :keyword"
        params["keyword"] = f"%{keyword}%"

    query = text(
        f"""
        SELECT corp_code, stock_name, stock_code,
            bizr_no, corp_cls, ceo_nm, est_dt, adres, hm_url
        FROM source.dart_corp_info
        {query_condition}
        LIMIT :limit OFFSET (:page - 1) * :limit
        """
    )
    params.update({"limit": limit, "page": page})
    result = db.execute(query, params).all()

    count_query = text(
        f"""
        SELECT COUNT(*) AS total_count
        FROM source.dart_corp_info
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


# TODO: relations corp_code 삽입용
def get_relations(db: Session):
    query = text("SELECT * FROM public.relation")
    result = db.execute(query).all()
    return result


# TODO: relations corp_code 삽입용
def get_corp_code_by_corp_name(corp_name: str, db: Session):
    corp_name = corp_name.replace("㈜", "")
    params = {"corp_name": f"%{corp_name}%"}
    query = text(
        """
        SELECT corp_code FROM source.dart_corp_info
        WHERE corp_name ILIKE :corp_name
        """
    )
    result = db.execute(query, params).fetchone()
    return result


# TODO: relations corp_code 삽입용
def patch_corp_code_by_corp_name(
    corp_name: str,
    corp_code: str,
    vendor_corp_name: str,
    vendor_corp_code: str,
    db: Session,
):
    corp_name = corp_name.replace("(주)", "")
    vendor_corp_name = vendor_corp_name.replace("(주)", "")
    params = {
        "corp_name": f"%{corp_name}%",
        "corp_code": corp_code,
        "vendor_corp_name": f"%{vendor_corp_name}%",
        "vendor_corp_code": vendor_corp_code,
    }
    query = text(
        """
        UPDATE public.relation
        SET corp_code = :corp_code, vendor_corp_code = :vendor_corp_code
        WHERE corp_name ILIKE :corp_name
        AND vendor_corp_name ILIKE :vendor_corp_name
        """
    )
    try:
        db.execute(query, params)
        db.commit()
        print("succeed:", corp_name, corp_code, vendor_corp_name, vendor_corp_code)

    except Exception as e:
        print("sql error", repr(e))
        db.rollback()
        raise e


def get_vendor_corp_list(corp_code: str, vendor_class: str | None, db: Session):
    query_condition = ""
    params = {"corp_code": corp_code}
    if vendor_class:
        query_condition = f"AND vendor_class=:vendor_class"
        params.update({"vendor_class": vendor_class})
    query = text(
        f"""
        SELECT *
        FROM (
            SELECT *, ROW_NUMBER() OVER(
                PARTITION BY vendor_corp_name
                ORDER BY update_date DESC
            ) AS rn
            FROM public.relation
            WHERE corp_code = :corp_code
            {query_condition}
        ) AS subquery
        WHERE rn = 1
        """
    )
    result = db.execute(query, params).all()
    return result


def get_naver_stock_price(stcd: str, db: Session):
    query = text(
        """
        SELECT close_price
        FROM source.naver_stock_price
        WHERE stock_code = :stcd
        AND base_date IN (
            SELECT MAX(base_date)
            FROM source.naver_stock_price
            WHERE stock_code = :stcd
            GROUP BY SUBSTRING(base_date, 1, 4)
        );
        """
    )

    result = db.execute(query, {"stcd": stcd}).fetchone()
    return result


def get_krx_corp_info(stcd: str, db: Session):
    query = text(
        """
        SELECT parval, list_shrs
        FROM source.krx_corp_info
        WHERE isu_srt_cd = :stcd
        """
    )
    result = db.execute(query, {"stcd": stcd}).fetchone()
    return result


# def get_dart_balance_sheet(stcd: str, db: Session):
#     query = text(
#         """
#         select currency, thstrm_amount from source.dart_balance_sheet where stock_code = :stcd
#         """
#     )
#     result = db.execute(query, {"stcd": stcd}).fetchone()
#     return result


def get_overview_relations():
    pass
