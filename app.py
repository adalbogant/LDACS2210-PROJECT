from dash import Dash, html, dcc, Input, Output, callback
import views.survival as survival, views.placeholder as placeholder

# Inspiration from https://github.com/plotly/dash-sample-apps/tree/main/apps/dash-financial-report 

app = Dash()
app.title = "METABRIC Dashboard"

app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/dash-metabric-dashboard/survival":
        return survival.create_layout(app)
    else:
        return placeholder.create_layout(app)



if __name__ == "__main__":  
    app.run()