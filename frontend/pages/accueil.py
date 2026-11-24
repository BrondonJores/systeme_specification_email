import plotly.graph_objects as go
from dash import Input, Output, dcc, html

from backend.stats import repartition_expediteurs


def _camembert(mails):
    if not mails:
        return {}
    labels, valeurs = repartition_expediteurs(mails)
    fig = go.Figure(go.Pie(labels=labels, values=valeurs))
    fig.update_layout(title="Répartition par expéditeur")
    return fig


def _barres(mails):
    if not mails:
        return {}
    labels, valeurs = repartition_expediteurs(mails)
    fig = go.Figure(go.Bar(x=labels, y=valeurs))
    fig.update_layout(title="Top expéditeurs")
    return fig


layout = html.Div(
    [
        html.Div(
            [
                html.Div("-", id="kpi-mails", className="kpi"),
                html.Div("-", id="kpi-expediteurs", className="kpi"),
            ],
            className="kpi-row",
        ),
        html.Div(
            [
                html.H2("Dashboard"),
                html.Div(
                    [
                        dcc.Graph(id="graph-camembert"),
                        dcc.Graph(id="graph-barres"),
                    ],
                    className="graph-row",
                ),
            ],
            className="card",
        ),
    ]
)


def register(app):
    @app.callback(
        Output("kpi-mails", "children"),
        Output("kpi-expediteurs", "children"),
        Output("graph-camembert", "figure"),
        Output("graph-barres", "figure"),
        Input("store-mails", "data"),
    )
    def _afficher(mails):
        mails = mails or []
        expediteurs = {m["expediteur"] for m in mails}
        return (
            f"{len(mails)} mails lus",
            f"{len(expediteurs)} expéditeurs",
            _camembert(mails),
            _barres(mails),
        )
