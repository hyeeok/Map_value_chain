import dash_bootstrap_components as dbc
import pandas as pd

import dash
from config.default import cal_ratio, scatter, scatter_ratio
from const.default import columns, columns_ratio, currency_dict, data_source, data_years
from dash import html

dash.register_page(__name__, path_template="/")


def layout():
    return dbc.Container(
        html.Div(
            [
                html.Img(
                    id="map", className="image", src=dash.get_asset_url("map.png")
                ),
                html.Img(
                    id="map-hover",
                    className="image hover-image",
                    src=dash.get_asset_url("map_hover.png"),
                ),
            ],
            id="image-container",
        ),
    )
