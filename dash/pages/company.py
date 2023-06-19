import dash_bootstrap_components as dbc
import pandas as pd

import dash
from config.default import cal_ratio, scatter, scatter_ratio
from const.default import columns, columns_ratio, currency_dict, data_source, data_years
from dash import html

dash.register_page(__name__, path_template="/company/<company_id>")

xls = pd.ExcelFile("data/기업데이터수집_2차전지업체_230526.xlsx")


def get_dict_from_xls(company_id: str, xls_df: pd.ExcelFile) -> dict:
    years = ["2018", "2019", "2020", "2021", "2022"]
    for sheet_name in xls_df.sheet_names:
        df = pd.read_excel(xls_df, sheet_name)
        business_num = df.loc[df["항목명"] == "사업자번호", years[-1]].values[0]
        if company_id == business_num:
            desc_df = df.loc[df["분류"] == "개요"][["항목명", years[-1]]]
            desc_df.rename(columns={years[-1]: "내용"}, inplace=True)
            info_df = df.loc[df["분류"] != "개요"][["분류", "항목명"] + [year for year in years]]
            info_df = info_df.set_index(["분류", "항목명"])

            data_dict = {"name": sheet_name, "desc_df": desc_df, "info_df": info_df}
            return data_dict
        else:
            continue
    print("No such company id")
    return


def layout(company_id=None):
    data_dict = get_dict_from_xls(company_id, xls)
    desc_df = data_dict["desc_df"].drop(0).fillna("")
    company_name = data_dict["name"]
    info_df = data_dict["info_df"].fillna("")

    half_rows = len(desc_df) // 2
    desc_table_1 = dbc.Table.from_dataframe(desc_df.iloc[:half_rows])
    desc_table_2 = dbc.Table.from_dataframe(desc_df.iloc[half_rows:])
    info_table = dbc.Table.from_dataframe(info_df, index=True)

    return dbc.Container(
        dbc.Stack(
            [
                html.H2(company_name),
                dbc.Stack([desc_table_1, desc_table_2], direction="horizontal", gap=3),
                info_table,
            ],
            gap=3,
        )
    )
