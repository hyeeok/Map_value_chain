import dash_auth
import dash_bootstrap_components as dbc

import dash
from components import navbar
from dash import Input, Output, State, dcc, html

VALID_USERNAME_PASSWORD_PAIRS = {"admin": "dnflwlq1!"}

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
)
server = app.server
auth = dash_auth.BasicAuth(app, VALID_USERNAME_PASSWORD_PAIRS)


def serve_layout():
    return html.Div([navbar(), dbc.Container(dash.page_container, class_name="my-2")])


app.layout = serve_layout()


if __name__ == "__main__":
    app.run_server(
        debug=True,
    )
