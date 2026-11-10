from dash import html, dcc

# Inspiration from https://github.com/plotly/dash-sample-apps/tree/main/apps/dash-financial-report 
# TODO : change later

def Header(app):
    # Br : break line
    return html.Div([get_header(app), html.Br([]), get_menu()])

def get_header(app):
    header = html.Div([
        html.H2(app.title)
    ], className="header-row")
    return header


# def get_header(app):
#     header = html.Div(
#         [
#             html.Div(
#                 [
#                     html.A(
#                         html.Img(
#                             src=app.get_asset_url("dash-financial-logo.png"),
#                             className="logo",
#                         ),
#                         href="https://plotly.com/dash",
#                     ),
#                     html.A(
#                         html.Button(
#                             "Enterprise Demo",
#                             id="learn-more-button",
#                             style={"margin-left": "-10px"},
#                         ),
#                         href="https://plotly.com/get-demo/",
#                     ),
#                     html.A(
#                         html.Button("Source Code", id="learn-more-button"),
#                         href="https://github.com/plotly/dash-sample-apps/tree/main/apps/dash-financial-report",
#                     ),
#                 ],
#                 className="row",
#             ),
#             html.Div(
#                 [
#                     html.Div(
#                         [html.H5("Calibre Financial Index Fund Investor Shares")],
#                         className="seven columns main-title",
#                     ),
#                     html.Div(
#                         [
#                             dcc.Link(
#                                 "Full View",
#                                 href="/dash-financial-report/full-view",
#                                 className="full-view-link",
#                             )
#                         ],
#                         className="five columns",
#                     ),
#                 ],
#                 className="twelve columns",
#                 style={"padding-left": "0"},
#             ),
#         ],
#         className="row",
#     )
#     return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href="/dash-metabric-dashboard/",
                className="tab first",
            ),
            dcc.Link(
                "Survival",
                href="/dash-metabric-dashboard/survival",
                className="tab",
            ),
            dcc.Link(
                "Clinical profile",
                href="/dash-metabric-dashboard/clinical-profile",
                className="tab"
            ),
            dcc.Link(
                "Details",
                href="/dash-metabric-dashboard/details",
                className="tab"
            )
        ],
        className="row all-tabs",
    )
    return menu
