import csv

from sqlalchemy import create_engine, text


def check_industry_type(type):
    if type == "C":
        industry_type = "class"
    elif type == "T":
        industry_type = "type"
    else:
        industry_type = ""
    return industry_type
