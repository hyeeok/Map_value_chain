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


def get_ceo_name_history_by_corp_code(corp_code: str, db: Session):
    query = text(
        """
        SELECT seq, ceo_nm, update_date
        FROM source.dart_ceo_nm_change_history
        WHERE corp_code = :corp_code
        """
    )
    result = db.execute(query, {"corp_code": corp_code}).all()
    return result


def get_corp_name_history_by_corp_code(corp_code: str, db: Session):
    query = text(
        """
        SELECT seq, corp_name, update_date
        FROM source.dart_corp_name_change_history
        WHERE corp_code = :corp_code
        """
    )
    result = db.execute(query, {"corp_code": corp_code}).all()
    return result


def get_shareholder_list_by_corp_code(corp_code: str, db: Session):
    query = text(
        """
        SELECT nm, relate, stock_knd, reprt_code,
            bsis_posesn_stock_co, bsis_posesn_stock_qota_rt,
            trmend_posesn_stock_co, trmend_posesn_stock_qota_rt, rm
        FROM source.dart_hyslr_sttus
        WHERE corp_code = :corp_code
        """
    )
    result = db.execute(query, {"corp_code": corp_code}).all()
    return result


def get_openapi_affiliate_list(crno: str, db: Session):
    query = text(
        """
        SELECT o.afilcmpynm, d.corp_code 
        FROM source.openapi_corp_affiliate o
            LEFT JOIN source.dart_corp_info d
            ON o.afilcmpycrno  = d.jurir_no
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


def get_mktcap_percent(isu_cd: str, db: Session):
    query = text(
        """
        WITH MaxDateCTE AS (
            SELECT
                EXTRACT(YEAR FROM TO_DATE(bas_dd, 'YYYYMMDD')) AS year,
                MAX(TO_DATE(bas_dd, 'YYYYMMDD')) AS max_date
            FROM
                "source".krx_openapi_stock_price
            WHERE
                isu_cd = :isu_cd
            GROUP BY
                EXTRACT(YEAR FROM TO_DATE(bas_dd, 'YYYYMMDD'))
        )
        SELECT
            kosp.krx_openapi_stock_price_id,
            kosp.isu_nm,
            kosp.mktcap,
            ROUND((CAST(kosp.mktcap AS NUMERIC) - LAG(CAST(kosp.mktcap AS NUMERIC)) OVER (PARTITION BY kosp.isu_cd ORDER BY TO_DATE(kosp.bas_dd, 'YYYYMMDD'))) / NULLIF(LAG(CAST(kosp.mktcap AS NUMERIC)) OVER (PARTITION BY kosp.isu_cd ORDER BY TO_DATE(kosp.bas_dd, 'YYYYMMDD')), 0) * 100, 1) AS mktcap_difference_percentage
        FROM
            "source".krx_openapi_stock_price kosp
            JOIN MaxDateCTE ON EXTRACT(YEAR FROM TO_DATE(kosp.bas_dd, 'YYYYMMDD')) = MaxDateCTE.year
                        AND TO_DATE(kosp.bas_dd, 'YYYYMMDD') = MaxDateCTE.max_date
        WHERE
            kosp.isu_cd = :isu_cd;
        """
    )
    params = {"isu_cd": isu_cd}
    result = db.execute(query, params).all()
    return result


def get_overview_relations():
    pass
