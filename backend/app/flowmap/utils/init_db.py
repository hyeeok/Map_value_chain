import csv
from random import randint

from app.flowmap.models import Domain, Flowmap, IndustryClass
from sqlalchemy import text
from sqlalchemy.orm import Session


def check_industry_type(type):
    if type == "C":
        industry_type = "class"
    elif type == "T":
        industry_type = "type"
    else:
        industry_type = ""
    return industry_type


def load_csv_to_db(filepath, db: Session):
    if db.query(IndustryClass).count() > 0:
        return

    nodes = []
    with open(filepath, "r", encoding="UTF8") as file:
        next(file)
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
                domain = Domain(code=domain_code, name=domain_name)
                db.add(domain)
                db.flush()

                node = {
                    'id': domain_code,
                    'position':{'x': randint(0, 500), 'y': randint(0, 500)},
                    'data': {'domainName': domain_name},
                    'type': 'custom'
                }
                nodes.append(node)

            industry_class = IndustryClass(
                code=industry_class_code,
                name=industry_class_name,
                type=industry_class_type,
                domain_id=domain.id,
            )
            db.add(industry_class)

    flowmap = Flowmap(
        node = nodes,
        edge = [],
    )
    db.add(flowmap)
