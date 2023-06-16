import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import QuantileRegressor

import dash
from const.default import (
    column_dict,
    company_col,
    currency_dict,
    data_source_color,
    log_currency_dict,
)


def cal_ratio(
    df,
    name: str,
    numerator: str,
    denominator: str = np.nan,  # If np.nan, use the previous numerator value
    to_percentage: bool = False,
    data_years: list = ["2018", "2019", "2020", "2021", "2022"],
) -> pd.DataFrame:
    if denominator is np.nan:
        result = df.loc[df.항목명 == numerator, data_years]
        denominator = result.copy()
        denominator.columns = [str(int(cnt) + 1) for cnt in data_years]
        result = result / denominator.replace(0, np.nan)  # prevent ZeroDivisionError
        result = result[data_years]
    else:
        result = pd.DataFrame(
            df.loc[df.항목명 == numerator, data_years].values
            / df.loc[df.항목명 == denominator, data_years]
            .replace(0, np.nan)
            .values,  # prevent ZeroDivisionError,
            columns=data_years,
        )

    if to_percentage:
        result *= 100

    if result.empty:
        result = pd.DataFrame({column: [np.nan] for column in result.columns})

    result["항목명"] = name

    return result


def scatter(
    data,
    year="2022",
    x_name="자산총계",
    y_name="영업이익",
    quantiles=[0.05, 0.25, 0.5, 0.75, 0.95],
    log_plot=True,
):
    # select data
    plot_data = (
        pd.DataFrame({key: value.set_index("항목명")[year] for key, value in data.items()})
        .T.astype(float)
        .reset_index()
    )

    # quantile regression
    quantile_data = plot_data[[x_name, y_name]].dropna()

    if quantile_data.empty:
        raise Exception("해당하는 값이 없습니다.")

    quantile_data = quantile_data[quantile_data[x_name] > 0]
    quantile_data = quantile_data[quantile_data[y_name] > 0]
    quantile_data = np.log(quantile_data)

    X = quantile_data.loc[:, x_name].values.reshape(-1, 1)
    y = quantile_data.loc[:, y_name]

    xx = np.linspace(np.min(X), np.max(X), 100).reshape(-1, 1)

    predictions = {}
    for quantile in quantiles:
        qr = QuantileRegressor(quantile=quantile, alpha=0, solver="highs")
        yy = qr.fit(X, y).predict(xx)
        predictions[quantile] = yy

    # plot
    fig = px.scatter(
        plot_data,
        x=x_name,
        y=y_name,
        log_x=log_plot,
        log_y=log_plot,
        hover_name="index",
        opacity=0.4,
    )

    for quantile, yy in predictions.items():
        fig.add_trace(
            go.Scatter(
                x=np.exp(xx.reshape(-1)),
                y=np.exp(yy),
                name=f"Quantile: {quantile}",
                opacity=0.5,
            )
        )

    fig.update_layout(title_text="2차전지 기업 - 2변수 비교 그래프")

    if log_plot:
        fig.update_layout(xaxis=currency_dict, yaxis=currency_dict)
    else:
        fig.update_layout(
            xaxis=dict(
                tickformat=",",
                ticksuffix="백만",
            ),
            yaxis=dict(
                tickformat=",",
                ticksuffix="백만",
            ),
        )

    return fig


def scatter_ratio(data, year="2022", x_name="자산총계", y_name="영업이익", log_plot=True):
    # select data
    plot_data = (
        pd.DataFrame({key: value.set_index("항목명")[year] for key, value in data.items()})
        .T.astype(float)
        .reset_index()
    )

    if plot_data[[x_name, y_name]].dropna().empty:
        raise Exception("해당하는 값이 없습니다.")

    # plot
    fig = px.scatter(
        plot_data,
        x=x_name,
        y=y_name,
        log_x=log_plot,
        log_y=log_plot,
        hover_name="index",
        opacity=0.4,
    )

    fig.update_layout(title_text="2차전지 기업 - 2개의 비율 변수 비교 그래프")

    return fig


def ridgeline(
    data,
    year="2022",
    company_name1="엘지에너지솔루션(연결)",
    company_name2="삼성SDI(연결)",
    column_dict_to_show=column_dict,
    log_plot=True,
):
    # select data
    plot_data = pd.DataFrame(
        {key: value.set_index("항목명")[year] for key, value in data.items()}
    ).T.astype(float)

    if log_plot:
        plot_data = np.log(plot_data)  # .fillna(0)
        #  errors can be disregarded
    else:
        pass

    # plot
    fig = go.Figure()

    # lines of total company
    for data_source, cols in column_dict_to_show.items():
        for cnt in cols:
            fig.add_trace(
                go.Violin(
                    x=plot_data[cnt],
                    name=cnt,
                    line_color=data_source_color[data_source],
                    showlegend=False,
                )
            )

    fig.update_traces(orientation="h", side="positive", width=3, points=False)
    fig.update_layout(xaxis_showgrid=False, xaxis_zeroline=False, yaxis_showgrid=True)

    # points of company
    for cnt, name in enumerate([company_name1, company_name2]):
        temp_plot_data = plot_data.loc[
            name, [col for columns in column_dict_to_show.values() for col in columns]
        ]
        fig.add_trace(
            go.Scatter(
                x=temp_plot_data,
                y=temp_plot_data.index,
                mode="markers",
                name=name,
                marker=dict(symbol="cross", color=company_col[cnt]),
            )
        )

    # layout
    fig.update_layout(title_text="2차전지 기업 - 여러변수 비교 그래프")

    if log_plot:
        fig.update_layout(xaxis=log_currency_dict)
    else:
        fig.update_layout(
            xaxis=dict(
                tickformat=",",
                ticksuffix="백만",
            )
        )

    # fig.update_layout(height=1000)

    return fig


def ridgeline_ratio(
    data,
    year="2022",
    company_name1="엘지에너지솔루션(연결)",
    company_name2="삼성SDI(연결)",
    column_dict_to_show=column_dict,
    log_plot=True,
):
    plot_data = pd.DataFrame(
        {key: value.set_index("항목명")[year] for key, value in data.items()}
    ).T.astype(float)

    if log_plot:
        plot_data = np.log(plot_data)  # .fillna(0)
        #  errors can be disregarded
    else:
        pass

    # plot
    fig = go.Figure()

    # lines of total company
    for data_source, cols in column_dict_to_show.items():
        for cnt in cols:
            fig.add_trace(
                go.Violin(
                    x=plot_data[cnt],
                    name=cnt,
                    line_color=data_source_color[data_source],
                    showlegend=False,
                )
            )

    fig.update_traces(orientation="h", side="positive", width=3, points=False)
    fig.update_layout(xaxis_showgrid=False, xaxis_zeroline=False, yaxis_showgrid=True)

    # points of company
    for cnt, name in enumerate([company_name1, company_name2]):
        temp_plot_data = plot_data.loc[
            name, [col for columns in column_dict_to_show.values() for col in columns]
        ]
        fig.add_trace(
            go.Scatter(
                x=temp_plot_data,
                y=temp_plot_data.index,
                mode="markers",
                name=name,
                marker=dict(symbol="cross", color=company_col[cnt]),
            )
        )

    # layout
    fig.update_layout(title_text="2차전지 기업 - 여러 비율 변수 비교 그래프")

    return fig
