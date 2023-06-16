import dash_bootstrap_components as dbc
import pandas as pd

import dash
from config.default import cal_ratio, scatter, scatter_ratio
from const.default import columns, columns_ratio, currency_dict, data_source, data_years
from dash import html

dash.register_page(__name__, path_template="company/<company_id>")

# load function formula data
function_data = pd.read_excel("data/기업정보 데이터 함수식.xlsx")
function_data["분류"] = function_data["분류"].fillna(method="ffill")

# make default data
xls = pd.ExcelFile("data/기업데이터수집_2차전지업체_230526.xlsx")

data = {}
for cnt in xls.sheet_names:
    df = pd.read_excel(xls, cnt)
    df.name = cnt
    df = df.loc[df.분류.isin(data_source), ["항목명", *data_years]]
    df_n_stocks = df.loc[df.항목명.isin(["발행주식수(보통주)", "발행주식수(우선주)"]), data_years].sum()
    df_n_stocks["항목명"] = "발행주식수"

    df = pd.concat([df, pd.DataFrame(df_n_stocks).T], ignore_index=True)

    # concat ratio values
    for _, row in function_data.iterrows():
        df = pd.concat(
            [
                df,
                cal_ratio(
                    df,
                    name=row["name"],
                    numerator=row["numerator"],
                    denominator=row["denominator"],
                    to_percentage=row["to_percentage"],
                ),
            ],
            ignore_index=True,
        )
    data[cnt] = df


def layout(company_id):
    return
