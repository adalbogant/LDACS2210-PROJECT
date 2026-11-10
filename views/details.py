from dash import html
from utils import Header

def create_layout(app):
    return html.Div(children=[ html.Div([Header(app)]), html.P(children="Here, write details about :" \
    "the dataset content" \
    ", the methods employed (imputation...)" \
    ", maybe authors...")])