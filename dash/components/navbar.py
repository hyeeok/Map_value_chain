import dash_bootstrap_components as dbc

import dash
from dash import html


def navbar():
    return dbc.NavbarSimple(
        brand="Greta MVC",
        brand_href="/",
        children=[
            dbc.Nav(
                [
                    dbc.NavItem(dbc.NavLink("Domain Map", href="/domain-map")),
                    dbc.NavItem(dbc.NavLink("Ridgeline", href="/ridgeline")),
                    dbc.NavItem(dbc.NavLink("Scatter", href="/scatter")),
                ],
                navbar=True,
            ),
        ],
        sticky="top",
        id="navbar",
    )
