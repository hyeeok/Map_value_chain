import dash_bootstrap_components as dbc
from dash import html

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(html.H2("기업 검색")),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.Label("기업명"),
                            dbc.Input(
                                type="text", placeholder="기업명을 입력하세요.", className="mb-3"
                            ),
                            dbc.Button("검색", color="primary", className="mr-3"),
                        ]
                    )
                )
            ]
        ),
    ]
)
