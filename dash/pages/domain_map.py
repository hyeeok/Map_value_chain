import dash_bootstrap_components as dbc
import pandas as pd

import dash
from dash import dcc, html

dash.register_page(__name__)

domain_map_df = pd.read_csv("data/domain_map.csv")

xls = pd.ExcelFile("data/기업데이터수집_2차전지업체_230526.xlsx")


def get_business_num_dict(xls_df: pd.ExcelFile) -> dict:
    business_num_dict = {}
    years = ["2018", "2019", "2020", "2021", "2022"]
    for sheet_name in xls_df.sheet_names:
        df = pd.read_excel(xls_df, sheet_name)
        business_num = df.loc[df["항목명"] == "사업자번호", years[-1]].values[0]
        company_name = df.loc[df["항목명"] == "기업", years[-1]].values[0]
        business_num_dict[company_name] = business_num
    return business_num_dict


business_num_dict = get_business_num_dict(xls)


nested_dicts = {}
for _, row in domain_map_df.iterrows():
    category = row["category"]
    division = row["division"]
    sub = f'({row["sub"]})' if not pd.isnull(row["sub"]) else ""
    name = row["name"] if not pd.isnull(row["name"]) else ""
    percent = row["percent"] if not pd.isnull(row["percent"]) else "?"

    category_dict = nested_dicts.setdefault(category, [])
    division_dict = next(
        (
            item
            for item in category_dict
            if item["division"] == division and item["sub"] == sub
        ),
        None,
    )
    if not division_dict:
        division_dict = {"division": division, "sub": sub, "contents": []}
        category_dict.append(division_dict)

    division_dict["contents"].append({"name": name, "percent": percent})


def generate_division_checklist(division_list):
    division_checklist = []
    for division in division_list:
        content_list = division["contents"]
        # options = generate_content_options(content_list)
        options = [
            {
                "label": dcc.Link(
                    f'{content["name"]} : {content["percent"]}%',
                    href="company/" + business_num_dict[content["name"]]
                    if content["name"] in business_num_dict.keys()
                    else content["name"],
                    style={"color": "#333"},
                ),
                "value": f'{division["division"]}-{content["name"]}',
            }
            for content in content_list
        ]
        division_card = dbc.Card(
            [
                dbc.CardHeader(division["division"] + division["sub"]),
                dbc.CardBody(
                    dbc.Checklist(options, label_style={"fontSize": "14px"}),
                    style={"padding": "12px"},
                ),
            ],
        )
        division_checklist.append(division_card)
    return division_checklist


def generate_category_checklist(nested_dicts):
    category_checklist = []
    for nested_dict in nested_dicts:
        division_list = nested_dicts[nested_dict]
        division_checklist = generate_division_checklist(division_list)
        category_card = dbc.Card(
            [
                dbc.CardHeader(str(nested_dict)),
                dbc.CardBody(
                    dbc.Stack(division_checklist, gap=2),
                    style={"padding": "12px"},
                ),
            ],
        )
        category_checklist.append(category_card)
    return category_checklist


category_checklist = generate_category_checklist(nested_dicts)

layout = html.Div(dbc.Form(dbc.CardGroup(category_checklist)))
