from dash import html
from utils import Header

def create_layout(app):
    return html.Div(children=[ html.Div([Header(app)]), html.H2(children="YOU'VE BEEN PLACEHOLDED")])