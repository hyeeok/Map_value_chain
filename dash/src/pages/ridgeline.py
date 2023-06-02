import dash
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.express as px
from dash import Input, Output, dcc, html
from sklearn.linear_model import QuantileRegressor

import plotly.graph_objects as go

from src.const.default import (
    data_source,
    data_source_color,
    data_years,
    currency_dict,
    columns,
    columns_ratio,
    column_ratio_dict,
    column_dict,
    company_col,
    log_currency_dict,
)
from src.config.default import cal_ratio, ridgeline, ridgeline_ratio

# load function formula data
function_data = pd.read_excel("src/data/기업정보 데이터 함수식.xlsx")
function_data["분류"] = function_data["분류"].fillna(method="ffill")

# make default data
xls = pd.ExcelFile("src/data/기업데이터수집_2차전지업체_230526.xlsx")

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


# user defined inputs (bellow values are default)
company_name1 = "엘지에너지솔루션(연결)"  # columns
company_name2 = "삼성SDI(연결)"  # columns

fig = ridgeline(
    data,
    year="2022",
    company_name1="엘지에너지솔루션(연결)",
    company_name2="삼성SDI(연결)",
    column_dict_to_show=column_dict,
    log_plot=True,
)


year_dropdown_options = [{"label": year, "value": year} for year in data_years]
dropdown_options = [{"label": column, "value": column} for column in columns]
column_dict_dropdown_options = [
    {"label": column, "value": column} for column in column_dict.keys()
] + [{"label": "All", "value": "all"}]

content = html.Div(
    id="fig_container",
    style={"padding": "1rem 1.5rem"},
    children=[
        dbc.Col(
            [
                dcc.Graph(id="ridgeline_comparison", figure=fig, responsive=True),
            ]
        ),
        dbc.Col(
            [
                html.Div(
                    [
                        html.Label("Year", className="dropdown-label"),
                        dbc.Select(
                            id="year-dropdown",
                            options=year_dropdown_options,
                            value="2022",
                        ),
                        # html.Label("회사1", className='dropdown-label'),
                        # dcc.Dropdown(
                        #     id="company1-dropdown", options=dropdown_options, value="엘지에너지솔루션(연결)"
                        # ),
                        # html.Label("회사2", className='dropdown-label'),
                        # dcc.Dropdown(
                        #     id="company2-dropdown", options=dropdown_options, value="삼성SDI(연결)"
                        # ),
                        dbc.Select(
                            id="column-dict-dropdown",
                            options=column_dict_dropdown_options,
                            value=["all"],
                        ),
                        dbc.Checklist(
                            id="log-checkbox",
                            options=[{"label": "log 처리", "value": "True"}],
                            value=["True"],
                        ),
                    ]
                ),
            ],
            width=4,
        ),
    ],
)


# user defined inputs (bellow values are default)
fig_ratio = ridgeline_ratio(
    data,
    year="2022",
    company_name1="엘지에너지솔루션(연결)",
    company_name2="삼성SDI(연결)",
    column_dict_to_show=column_ratio_dict,
    log_plot=False,
)


year_dropdown_options2 = [{"label": year, "value": year} for year in data_years]
dropdown_options2 = [{"label": column, "value": column} for column in columns]
column_dict_dropdown_options2 = [
    {"label": column, "value": column} for column in column_dict.keys()
] + [{"label": "All", "value": "all"}]

content2 = html.Div(
    id="fig_container",
    style={"padding": "1rem 1.5rem"},
    children=[
        dbc.Col(
            [
                dcc.Graph(
                    id="ridgeline_ratio_comparison", figure=fig_ratio, responsive=True
                ),
            ]
        ),
        dbc.Col(
            [
                html.Div(
                    [
                        html.Label("Year", className="dropdown-label"),
                        dbc.Select(
                            id="year-dropdown2",
                            options=year_dropdown_options,
                            value="2022",
                        ),
                        # html.Label("회사1", className='dropdown-label'),
                        # dcc.Dropdown(
                        #     id="company1-dropdown2", options=dropdown_options, value="엘지에너지솔루션(연결)"
                        # ),
                        # html.Label("회사2", className='dropdown-label'),
                        # dcc.Dropdown(
                        #     id="company2-dropdown2", options=dropdown_options, value="삼성SDI(연결)"
                        # ),
                        dbc.Select(
                            id="column-dict-dropdown2",
                            options=column_dict_dropdown_options2,
                            value=["all"],
                        ),
                        dbc.Select(
                            id="log-checkbox2",
                            options=[{"label": "log 처리", "value": "True"}],
                            value=["True"],
                        ),
                    ]
                ),
            ],
            width=4,
        ),
    ],
)


layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(html.H2("전체 기업 정보 분석")),
            ]
        ),
        content,
        content2,
    ]
)


@dash.callback(
    Output("ridgeline_comparison", "figure"),
    [
        Input("year-dropdown", "value"),
        # Input("company1-dropdown", "value"),
        # Input("company2-dropdown", "value"),
        Input("column-dict-dropdown", "value"),
        Input("log-checkbox", "value"),
    ],
    prevent_initial_call=True,
)
# def update_graph(year, company_name1, company_name2, column_dict_key, log,):
def update_graph(
    year,
    column_dict_key,
    log,
):
    log = True if log else False
    if column_dict_key == "all" or isinstance(column_dict_key, list):
        column_dict_to_show = column_dict
    else:
        column_dict_to_show = {column_dict_key: column_dict[column_dict_key]}
    fig = ridgeline(data, year, company_name1, company_name2, column_dict_to_show, log)
    return fig


@dash.callback(
    Output("ridgeline_ratio_comparison", "figure"),
    [
        Input("year-dropdown2", "value"),
        # Input("company1-dropdown2", "value"),
        # Input("company2-dropdown2", "value"),
        Input("column-dict-dropdown2", "value"),
        Input("log-checkbox2", "value"),
    ],
    prevent_initial_call=True,
)
# def update_graph(year,  company_name1, company_name2, column_dict_key, log,):
def update_graph(
    year,
    column_dict_key,
    log,
):
    log = True if log else False

    if column_dict_key == "all" or isinstance(column_dict_key, list):
        column_ratio_dict_to_show = column_ratio_dict
    else:
        column_ratio_dict_to_show = {column_dict_key: column_dict[column_dict_key]}
    fig = ridgeline_ratio(
        data, year, company_name1, company_name2, column_ratio_dict_to_show, log
    )
    return fig
