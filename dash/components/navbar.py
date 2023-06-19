import dash_bootstrap_components as dbc

import dash
from dash import html


def navbar():
    nav_items = [
        dbc.NavItem(dbc.NavLink(page["name"], href=page["relative_path"]))
        for page in dash.page_registry.values()
    ]

    return dbc.NavbarSimple(
        brand="Greta MVC",
        brand_href="/",
        children=[
            dbc.Nav(
                nav_items,
                navbar=True,
            ),
        ],
        sticky="top",
        id="navbar",
    )
