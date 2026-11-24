from dash import Input, Output, dcc, html

from backend.reader import lire_derniers


def build_shell():
    return html.Div(
        [
            html.Div(
                [
                    html.H1("Dashboard e-mails"),
                    html.P("Envoi, réception, filtres et alertes en Python"),
                    html.Button("Actualiser les mails", id="btn-refresh"),
                    html.Div("-", id="out-refresh"),
                ],
                className="header",
            ),
            html.Nav(
                [
                    dcc.Link("Accueil", href="/"),
                    dcc.Link("Envoi", href="/envoi"),
                    dcc.Link("Boîte de réception", href="/inbox"),
                    dcc.Link("Filtres", href="/filtres"),
                    dcc.Link("Alertes", href="/alerte"),
                ],
                className="navbar",
            ),
            dcc.Location(id="url"),
            dcc.Store(id="store-mails"),
            html.Div(id="page-content"),
        ]
    )


def register_shell(app):
    @app.callback(
        Output("store-mails", "data"),
        Output("out-refresh", "children"),
        Input("btn-refresh", "n_clicks"),
        prevent_initial_call=True,
    )
    def _refresh(n):
        mails = lire_derniers(5)
        return mails, f"{len(mails)} mails chargés."
