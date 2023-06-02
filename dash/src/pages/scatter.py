import dash
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.express as px
from dash import Input, Output, dcc, html
from sklearn.linear_model import QuantileRegressor

import plotly.graph_objects as go

from src.const.default import data_source, data_source_color, data_years, currency_dict, columns, columns_ratio
from src.lib.default import cal_ratio

# load function formula data
function_data = pd.read_excel('src/data/기업정보 데이터 함수식.xlsx')
function_data['분류'] = function_data['분류'].fillna(method='ffill')

# make default data
xls = pd.ExcelFile('src/data/기업데이터수집_2차전지업체_230526.xlsx')

data = {}
for cnt in xls.sheet_names:
    df = pd.read_excel(xls, cnt)
    df.name = cnt
    df = df.loc[
        df.분류.isin(data_source),
        ["항목명", *data_years]
    ]
    df_n_stocks = df.loc[df.항목명.isin(['발행주식수(보통주)', '발행주식수(우선주)']), data_years].sum()
    df_n_stocks['항목명'] = '발행주식수'

    df = pd.concat([df, pd.DataFrame(df_n_stocks).T], ignore_index=True)

    # concat ratio values
    for _, row in function_data.iterrows():
        df = pd.concat([df,
            cal_ratio(
                df,
                name = row['name'],
                numerator = row['numerator'],
                denominator = row['denominator'],
                to_percentage = row['to_percentage']
            )],
            ignore_index=True
        )
    data[cnt] = df


# user defined inputs (bellow values are default)
year = '2022' # data_years
x_name = '자산총계' # columns
y_name = '영업이익' # columns
quantiles = [0.05, 0.25, 0.5, 0.75, 0.95]
log_plot = True

# select data
plot_data = pd.DataFrame({
    key:value.set_index("항목명")[year] for key, value in data.items()
}).T.astype(float).reset_index()

# select data
plot_data = pd.DataFrame({
    key:value.set_index("항목명")[year] for key, value in data.items()
}).T.astype(float).reset_index()

# quantile regression
quantile_data = plot_data[[x_name, y_name]].dropna()

if quantile_data.empty:
    raise Exception("해당하는 값이 없습니다.")

quantile_data = quantile_data[quantile_data[x_name]>0]
quantile_data = quantile_data[quantile_data[y_name]>0]
quantile_data = np.log(quantile_data)

X = quantile_data.loc[:,x_name].values.reshape(-1, 1)
y = quantile_data.loc[:,y_name]


xx =  np.linspace(np.min(X), np.max(X), 100).reshape(-1, 1)

predictions = {}
for quantile in quantiles:
    qr = QuantileRegressor(quantile=quantile, alpha=0, solver="highs")
    yy = qr.fit(X, y).predict(xx)
    predictions[quantile] = yy

# plot
fig = px.scatter(
    plot_data, x=x_name, y=y_name,
    log_x=log_plot, log_y=log_plot,
    hover_name='index',
    opacity=0.4
    )

for quantile, yy in predictions.items():
    fig.add_trace(go.Scatter(x=np.exp(xx.reshape(-1)), y=np.exp(yy), name=f"Quantile: {quantile}", opacity=0.5))


fig.update_layout(title_text="2차전지 기업 - 2변수 비교 그래프")


if log_plot:
    fig.update_layout(
        xaxis=currency_dict,
        yaxis=currency_dict
    )
else:
    fig.update_layout(
        xaxis=dict(
            tickformat=',', ticksuffix='백만',
        ),
        yaxis=dict(
            tickformat=',', ticksuffix='백만',
        )
    )


year_dropdown_options = [{"label": year, "value": year} for year in data_years]
dropdown_options = [{"label": column, "value": column} for column in columns]
quantiles_dropdown_options = [0.05, 0.25, 0.5, 0.75, 0.95]

content = html.Div(
    id="fig_container",
    style={"padding": "1rem 1.5rem"},
    children=[
    dbc.Col([
        dcc.Graph(id="two_vars_comparison", figure=fig, responsive=True),
    ]),
    dbc.Col([
        html.Div(
            [
                html.Label("Year", className='dropdown-label'),
                dcc.Dropdown(
                    id="year-dropdown", options=year_dropdown_options, value="2022"
                ),
                html.Label("X축", className='dropdown-label'),
                dcc.Dropdown(
                    id="xaxis-dropdown", options=dropdown_options, value="자산총계"
                ),
                html.Label("Y축", className='dropdown-label'),
                dcc.Dropdown(
                    id="yaxis-dropdown", options=dropdown_options, value="영업이익"
                ),
                # dcc.Dropdown(
                #     id="quantiles-dropdown", options=quantiles_dropdown_options, value="True"
                # ),
                dcc.Checklist(
                    id="log-checkbox",
                    options=[{"label": "log 처리", "value": "True"}],
                    value=["True"],
                ),
            ]
        ),
    ], width=4)
    ],
)




# user defined inputs (bellow values are default)
year = '2022' # data_years

x_name = '자기자본비율' # columns_ratio
y_name = '비유동부채비율' # columns_ratio

log_plot = False


# select data
plot_data = pd.DataFrame({
    key:value.set_index("항목명")[year] for key, value in data.items()
}).T.astype(float).reset_index()

if plot_data[[x_name, y_name]].dropna().empty:
    raise Exception("해당하는 값이 없습니다.")

# plot
fig2 = px.scatter(
    plot_data, x=x_name, y=y_name,
    log_x=log_plot, log_y=log_plot,
    hover_name='index',
    opacity=0.4
    )

fig2.update_layout(title_text="2차전지 기업 - 2개의 비율 변수 비교 그래프")


dropdown_options2 = [{"label": column_ratio, "value": column_ratio} for column_ratio in columns_ratio]

content2 = html.Div(
    id="fig_container",
    style={"padding": "1rem 1.5rem"},
    children=[
    dbc.Col([
        dcc.Graph(id="two_vars_ratio_comparison", figure=fig2, responsive=True),
    ]),
    dbc.Col([
        html.Div(
            [
                html.Label("Year", className='dropdown-label'),
                dcc.Dropdown(
                    id="year-dropdown2", options=year_dropdown_options, value="2022"
                ),
                html.Label("X축", className='dropdown-label'),
                dcc.Dropdown(
                    id="xaxis-dropdown2", options=dropdown_options2, value="자기자본비율"
                ),
                html.Label("Y축", className='dropdown-label'),
                dcc.Dropdown(
                    id="yaxis-dropdown2", options=dropdown_options2, value="비유동부채비율"
                ),
                dcc.Checklist(
                    id="log-checkbox2",
                    options=[{"label": "log 처리", "value": "True"}],
                    value=["True"],
                ),
            ]
        ),
    ], width=4)
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
        content2
    ]
)


@dash.callback(
    Output("two_vars_comparison", "figure"),
    [
        Input("year-dropdown", "value"),
        Input("xaxis-dropdown", "value"),
        Input("yaxis-dropdown", "value"),
        # Input("quantiles-dropdown", "value"),
        Input("log-checkbox", "value"),
    ],
    prevent_initial_call=True,
)
def update_graph(year_value, xaxis_value, yaxis_value, log,):
    log = True if log else False
    plot_data = pd.DataFrame({
        key:value.set_index("항목명")[year_value] for key, value in data.items()
    }).T.astype(float).reset_index()

    # select data
    plot_data = pd.DataFrame({
        key:value.set_index("항목명")[year_value] for key, value in data.items()
    }).T.astype(float).reset_index()

    # quantile regression
    quantile_data = plot_data[[xaxis_value, yaxis_value]].dropna()

    if quantile_data.empty:
        raise Exception("해당하는 값이 없습니다.")

    quantile_data = quantile_data[quantile_data[xaxis_value]>0]
    quantile_data = quantile_data[quantile_data[yaxis_value]>0]
    quantile_data = np.log(quantile_data)

    X = quantile_data.loc[:,xaxis_value].values.reshape(-1, 1)
    y = quantile_data.loc[:,yaxis_value]


    xx =  np.linspace(np.min(X), np.max(X), 100).reshape(-1, 1)

    predictions = {}
    for quantile in quantiles:
        qr = QuantileRegressor(quantile=quantile, alpha=0, solver="highs")
        yy = qr.fit(X, y).predict(xx)
        predictions[quantile] = yy

    fig = px.scatter(
        plot_data,
        x=xaxis_value,
        y=yaxis_value,
        log_x=log,
        log_y=log,
        opacity=0.4,
    )
    for quantile, yy in predictions.items():
        fig.add_trace(go.Scatter(x=np.exp(xx.reshape(-1)), y=np.exp(yy), name=f"Quantile: {quantile}", opacity=0.5))
    return fig

@dash.callback(
    Output("two_vars_ratio_comparison", "figure"),
    [
        Input("year-dropdown2", "value"),
        Input("xaxis-dropdown2", "value"),
        Input("yaxis-dropdown2", "value"),
        Input("log-checkbox2", "value"),
    ],
    prevent_initial_call=True,
)
def update_graph(year_value, xaxis_value, yaxis_value, log,):
    log = True if log else False
    plot_data = pd.DataFrame({
        key:value.set_index("항목명")[year_value] for key, value in data.items()
    }).T.astype(float).reset_index()

    if plot_data[[x_name, y_name]].dropna().empty:
        raise Exception("해당하는 값이 없습니다.")


    fig = px.scatter(
        plot_data,
        x=xaxis_value,
        y=yaxis_value,
        log_x=log,
        log_y=log,
        opacity=0.4,
    )
    return fig
