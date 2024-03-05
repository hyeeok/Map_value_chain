from collections import defaultdict
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

def get_industry_class_info_list(db: Session):

    query = text(
        """
        SELECT
                (SELECT c.MVC_DOMAIN_NAME
                FROM ANALYTICS.DIM_MVC_INDUSTRY_CLASS c
                WHERE a.MVC_INDUSTRY_CLASS_CODE = c.MVC_INDUSTRY_CLASS_CODE
                ) MVC_DOMAIN_NAME
                , (SELECT c.MVC_INDUSTRY_CLASS_NAME
                FROM ANALYTICS.DIM_MVC_INDUSTRY_CLASS c
                WHERE a.MVC_INDUSTRY_CLASS_CODE = c.MVC_INDUSTRY_CLASS_CODE
                ) MVC_INDUSTRY_CLASS_NAME
                , b.CORP_CLS
                , COUNT(b.CORP_CLS) AS  CORP_CLS_cnt
        FROM ANALYTICS.DIM_MVC_CORP_INDUSTRY_CLASS a
        LEFT OUTER JOIN ANALYTICS.DIM_CORP_MASTER b
            ON a.CORP_CODE = b.CORP_CODE
        WHERE 1=1
        AND a.CLASS_SYSTEM_TYPE = 'NVSI'
        GROUP BY
                a.CLASS_SYSTEM_TYPE
                , a.MVC_INDUSTRY_CLASS_CODE
                , b.CORP_CLS
        ORDER BY 1, 2
        """
    )

    result = db.execute(query).fetchall()

    formatted_result = []
    total_cnt = 0

    for row in result:
        domainName = row[0]
        industryClassName = row[1]
        # subMajorClassName = row[2]
        # subMinorClassName = row[3]
        corpCls = row[2]
        corpClsCnt = row[3]

        total_cnt += corpClsCnt 

        data_entry = {
            "domainName": domainName,
            "industryClassName": industryClassName,
            # "subMajorClassName": subMajorClassName,
            # "subMinorClassName": subMinorClassName,
            "cnt": {
                "TOTAL": 0,
                "Y": 0,
                "K": 0,
                "N": 0,
                "비상장외감": 0,
                "비외감": 0
            },
            "rate": {
                "TOTAL": 0,
                "Y": 0,
                "K": 0,
                "N": 0,
                "비상장외감": 0,
                "비외감": 0
            },
        }

        existing_entry = next((entry for entry in formatted_result if entry["domainName"] == domainName and entry["industryClassName"] == industryClassName), None)
        # existing_entry = next((entry for entry in formatted_result if entry["domainName"] == domainName 
        #                                                             and entry["industryClassName"] == industryClassName
        #                                                             and entry["subMajorClassName"] == subMajorClassName
        #                                                             and entry["subMinorClassName"] == subMinorClassName), None)
        if existing_entry:
            existing_entry["cnt"][corpCls] = corpClsCnt
            existing_entry["cnt"]["TOTAL"] += corpClsCnt  
        else:
            data_entry["cnt"][corpCls] = corpClsCnt
            data_entry["cnt"]["TOTAL"] = corpClsCnt  
            formatted_result.append(data_entry)

    for entry in formatted_result:
        for key in entry["cnt"]:
            entry["rate"][key] = round(entry["cnt"][key] / total_cnt, 6) if total_cnt > 0 else 0.0

    return formatted_result