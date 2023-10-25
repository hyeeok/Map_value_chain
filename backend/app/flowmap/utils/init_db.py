import csv
from random import randint

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.flowmap.models import Domain, Flowmap, IndustryClass


def check_industry_class_type(type: str):
    type = type.lower()
    if type == "c":
        industry_type = "classes"
    elif type == "t":
        industry_type = "themes"
    else:
        industry_type = "etc"
    return industry_type


def load_csv_to_db(filepath, db: Session):
    if db.query(IndustryClass).count() > 0:
        return
    with open(filepath, "r", encoding="UTF8") as file:
        next(file)
        node_list = []
        domain_code_data_dict = {}
        domain_code_name_list = []

        for row in csv.reader(file):
            (
                domain_code,
                domain_name,
                industry_class_type,
                industry_class_code,
                industry_class_name,
            ) = row

            domain = db.query(Domain).filter_by(code=domain_code).first()
            if not domain:
                domain_code_name_list.append((domain_code, domain_name))
                domain = Domain(code=domain_code, name=domain_name)
                db.add(domain)
                db.flush()

            industry_class = IndustryClass(
                code=industry_class_code,
                name=industry_class_name,
                type=industry_class_type,
                domain_id=domain.id,
            )
            db.add(industry_class)
            db.flush()

            industry_class_type_name = check_industry_class_type(industry_class_type)
            industry_class_list = domain_code_data_dict.setdefault(
                domain_code, {"classes": [], "themes": []}
            )[industry_class_type_name]
            industry_class_list.append(
                {
                    "industryClassId": industry_class.id,
                    "industryClassCode": industry_class_code,
                    "industryClassName": industry_class_name,
                }
            )

        for domain_code, domain_name in domain_code_name_list:
            node_data = domain_code_data_dict[domain_code]
            node = {
                "id": domain_code,
                "position": {"x": randint(0, 500), "y": randint(0, 500)},
                "data": {
                    "domainId": domain.id,
                    "domainCode": domain_code,
                    "domainName": domain_name,
                    **node_data,
                },
                "type": "custom",
            }
            node_list.append(node)

    flowmap = Flowmap(
        node=node_list,
        edge=[],
    )
    db.add(flowmap)
