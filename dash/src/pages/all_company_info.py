import dash
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.express as px
from dash import Input, Output, dcc, html

from src.const.all_company_info import data_category, select_axis

# data load
data_key = pd.read_csv("src/data/krx_corp.csv", encoding="cp949")
data = pd.read_csv("src/data/cfs_22_date_KRW_filter.csv")


# 전처리
def convert_text(text):
    split_text = text.split("_")
    if len(split_text) > 3:
        return split_text[4]
    return text


data.columns = (convert_text(cnt) for cnt in data.columns)
data.drop(["rcept_no", "reprt_code", "bsns_year"], axis=1, inplace=True)
data = (
    data.applymap(lambda cnt: str(cnt).replace(",", ""))
    .applymap(lambda cnt: np.nan if cnt == "-" else cnt)
    .astype(float)
)
data = pd.merge(
    data,
    data_key,
    left_on="stock_code",
    right_on="종목코드",
    how="left",
    suffixes=("", "_krx"),
)


# make plot-data
plot_data = data.loc[
    :,
    [
        "종목명",
        "유동자산",
        "비유동자산",
        "자산총계",
        "유동부채",
        "비유동부채",
        "부채총계",
        "자본금",
        "이익잉여금",
        "자본총계",
        "매출액",
        "영업이익",
        "법인세차감전 순이익",
        "당기순이익",
    ],
]
plot_data["2차전지"] = plot_data.종목명.isin(data_category)
fig = px.scatter(
    plot_data,
    x="자본총계",
    y="당기순이익",
    log_x=True,
    log_y=True,
    color="2차전지",
    hover_name="종목명",
    opacity=0.4,
)


dropdown_options = [{"label": axis, "value": axis} for axis in select_axis]

content = html.Div(
    id="all_company_info_container",
    style={"padding": "1rem 1.5rem"},
    children=[
        dbc.Col(
            [
                dcc.Graph(id="cfs_22_date_KRW_filtered", figure=fig, responsive=True),
            ]
        ),
        dbc.Col(
            [
                html.Div(
                    [
                        html.Label("X축", className="dropdown-label"),
                        dbc.Select(
                            id="xaxis-dropdown", options=dropdown_options, value="자본총계"
                        ),
                        dbc.Checklist(
                            id="xaxis-log-checkbox",
                            options=[{"label": "log 처리", "value": "True"}],
                            value=["True"],
                        ),
                    ]
                ),
                html.Div(
                    [
                        html.Label("Y축", className="dropdown-label"),
                        dbc.Select(
                            id="yaxis-dropdown", options=dropdown_options, value="당기순이익"
                        ),
                        dbc.Checklist(
                            id="yaxis-log-checkbox",
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
    ]
)  # 전체 기업 정보를 보여주는 그래프


@dash.callback(
    Output("cfs_22_date_KRW_filtered", "figure"),
    [
        Input("xaxis-dropdown", "value"),
        Input("yaxis-dropdown", "value"),
        Input("xaxis-log-checkbox", "value"),
        Input("yaxis-log-checkbox", "value"),
    ],
    prevent_initial_call=True,
)
def update_graph(xaxis_value, yaxis_value, xaxis_log, yaxis_log):
    log_x = True if xaxis_log else False
    log_y = True if yaxis_log else False
    fig = px.scatter(
        plot_data,
        x=xaxis_value,
        y=yaxis_value,
        log_x=log_x,
        log_y=log_y,
        color="2차전지",
        hover_name="종목명",
        opacity=0.4,
    )
    return fig
