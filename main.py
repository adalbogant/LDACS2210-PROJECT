import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from lifelines import KaplanMeierFitter
from preprocessing.impute_missing_data import load_imputed_data
from dash import Dash, html, dcc, Input, Output, callback

FILEPATH = "data/METABRIC.csv"

# Kaplan Meier curves are a common way to visualise survival data
# Also drop values for now since I just want to get a working layout that displays an actual graph
df = load_imputed_data(FILEPATH)
df = df.copy() # To avoid warnings about fragmentation

# Define the thresholds to draw the different group of curves (found at https://link.springer.com/article/10.1007/s12253-008-9067-3)
def npi_grouping(npi):
    if npi <= 2.4:
        return "Excellent (< 2.4)"
    elif npi <= 3.4:
        return "Good (< 3.4)"
    elif npi <= 4.4:
        return "Moderate I (< 4.4)"
    elif npi <= 5.4:
        return "Moderate II (< 5.4)"
    elif npi <= 6.4:
        return "Poor (< 6.4)"
    return "Very Poor (> 6.4)"

# Create the filter column based on npi values
df["npi_group"] = df["nottingham_prognostic_index"].apply(npi_grouping)
df["overall_survival_years"] = df["overall_survival_months"]/12

# Green to Red color palette https://loading.io/color/feature/RdYlGn-6/
# TODO : find a way to have customisable palette, as this one is not accessible for protanopia and deuteranopia
# (see https://davidmathlogic.com/colorblind/#%231A9850-%2391CF60-%23D9EF8B-%23FEE08B-%23FC8D59-%23D73027)
colors = {
    "Excellent (< 2.4)":  "#1a9850",
    "Good (< 3.4)":       "#91cf60",
    "Moderate I (< 4.4)": "#d9ef8b",
    "Moderate II (< 5.4)":"#fee08b",
    "Poor (< 6.4)":       "#fc8d59",
    "Very Poor (> 6.4)":  "#d73027",
}

graph_x_axis = df["death_from_cancer"]
graph_y_axis = df["overall_survival_months"]

fig_general = px.histogram(x=graph_x_axis, labels=graph_y_axis)

fig_km = go.Figure()

kaplan_meier = KaplanMeierFitter()

for group, color in colors.items():
    mask = df["npi_group"] == group
    time = df.loc[mask, "overall_survival_years"]
    event = df.loc[mask, "death_from_cancer"] == "Died of Disease"
    
    if len(time) == 0:
        continue
    
    kaplan_meier.fit(durations=time, event_observed=event, label=group)
    
    fig_km.add_trace(go.Scatter(
        x=kaplan_meier.timeline,
        y=kaplan_meier.survival_function_[group],
        mode="lines",
        name=group,
        line=dict(color=color)
    ))
    
fig_km.update_layout(
    title="Kaplan-Meier curves for survival per NPI group",
    xaxis_title="Time (years)",
    yaxis_title="Probability of survival",
    yaxis=dict(range=[0, 1])
)

app = Dash()

app.layout = html.Div(children=[
    html.H2(children="Kaplan-Meier : Survival with respect to Nottingham Prognostic Index"),
    dcc.Graph(
        id="km-nottingham",
        figure=fig_km
    ),
    
    html.H2(children="Scatterplot Comparison graph"),
    dcc.Graph(
        id="generic-scatter",
        figure=fig_general
    )
])

app.run()