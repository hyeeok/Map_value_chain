import dash_bootstrap_components as dbc
from dash import html

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(html.H2("로그인")),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.Label("아이디"),
                            dbc.Input(
                                type="text", placeholder="아이디를 입력하세요.", className="mb-3"
                            ),
                            html.Label("비밀번호"),
                            dbc.Input(
                                type="password",
                                placeholder="비밀번호를 입력하세요.",
                                className="mb-3",
                            ),
                            dbc.Button("로그인", color="primary", className="mr-3"),
                            dbc.Button("회원가입", color="secondary", href="/register"),
                        ]
                    )
                )
            ]
        ),
    ]
)
