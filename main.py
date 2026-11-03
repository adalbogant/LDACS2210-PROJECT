import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from lifelines import KaplanMeierFitter
from dash import Dash, html, dcc, Input, Output, callback

df = pd.read_csv("data/METABRIC.csv", low_memory=False)

# Kaplan Meier curves are a common way to visualise survival data
# Also drop values for now since I just want to get a working layout that displays an actual graph
df2 = df.dropna(subset=["overall_survival_months", "nottingham_prognostic_index", "death_from_cancer"])
df2 = df2.copy()

# Define the thresholds to draw the different group of curves (found at https://link.springer.com/article/10.1007/s12253-008-9067-3)
def npi_grouping(npi):
    if npi <= 2.4:
        return "Excellent"
    elif npi <= 3.4:
        return "Good"
    elif npi <= 4.4:
        return "Moderate I"
    elif npi <= 5.4:
        return "Moderate II"
    elif npi <= 6.4:
        return "Poor"
    return "Very Poor"

# Create the filter column based on npi values
df2["npi_group"] = df2["nottingham_prognostic_index"].apply(npi_grouping)
df2["overall_survival_years"] = df2["overall_survival_months"]/12

# Green to Red color palette https://loading.io/color/feature/RdYlGn-6/
colors = {
    "Excellent":  "#1a9850",
    "Good":       "#91cf60",
    "Moderate I": "#d9ef8b",
    "Moderate II":"#fee08b",
    "Poor":       "#fc8d59",
    "Very Poor":  "#d73027",
}

fig = go.Figure()

kaplan_meier = KaplanMeierFitter()

for group, color in colors.items():
    mask = df2["npi_group"] == group
    time = df2.loc[mask, "overall_survival_years"]
    event = df2.loc[mask, "death_from_cancer"] == "Died of Disease"
    
    if len(time) == 0:
        continue
    
    kaplan_meier.fit(durations=time, event_observed=event, label=group)
    
    fig.add_trace(go.Scatter(
        x=kaplan_meier.timeline,
        y=kaplan_meier.survival_function_[group],
        mode="lines",
        name=group,
        line=dict(color=color)
    ))
    
fig.update_layout(
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
        figure=fig
    ),
])

app.run()