import dash_bootstrap_components as dbc
from dash import html

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(html.H2("기업 정보 분석")),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            # 기업 정보를 보여주는 그래프 등을 추가
                        ]
                    )
                )
            ]
        ),
    ]
)
