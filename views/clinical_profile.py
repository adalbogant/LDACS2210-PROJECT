
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from preprocessing.impute_missing_data import write_imputed_data
from dash import Dash, html, dcc, Input, Output, callback
from utils import Header, COLOR_PRIMARY_DARK, COLOR_SECONDARY_DARK

FILEPATH = "data/METABRIC.csv"
FILEPATH_IMPUTED = "data/METABRIC_imputed.csv"

#### IMPORT DATASET WITH IMPUTED VALUES ####
try:
    df = pd.read_csv(FILEPATH_IMPUTED, low_memory=False)
except FileNotFoundError:
    write_imputed_data(FILEPATH, FILEPATH_IMPUTED)
    df = pd.read_csv(FILEPATH_IMPUTED)
df = df.copy() # To avoid warnings about fragmentation

#### AGE HISTOGRAM ####
fig_age_histogram = px.histogram(
    df,
    x="age_at_diagnosis",
    title="Distribution of age at diagnosis",
    labels={"age_at_diagnosis": "Age at diagnosis (years)"},
    color_discrete_sequence=[COLOR_SECONDARY_DARK]
)
fig_age_histogram.update_layout(
    yaxis_title="Number of patients"
)


#### BAR CHART PAM50 TYPES ####
fig_pam50_histogram = px.histogram(df, x="pam50_+_claudin-low_subtype", title="Distribution of PAM50 and Claudin-low subtype",
                                   color_discrete_sequence=COLOR_SECONDARY_DARK)
fig_pam50_histogram.update_layout(
    yaxis_title="Number of patients"
)


def create_layout(app):
    return html.Div(children=[ 
        html.Div([Header(app)]), 
        html.H5("Clinical profile"),
        dcc.Graph(
                    id="age_histogram", 
                    figure=fig_age_histogram,
                ),
        dcc.Graph(
            id="pam50_histogram",
            figure=fig_pam50_histogram,
        ),
    ])