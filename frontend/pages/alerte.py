from dash import Input, Output, State, dcc, html

from backend import filters as mail_filters

layout = html.Div(
    [
        html.H2("Alerte mot-clé"),
        dcc.Input(id="in-alerte-mot", placeholder="Mot-clé à surveiller"),
        dcc.Input(id="in-alerte-dest", placeholder="E-mail d'alerte", type="email"),
        html.Button("Surveiller", id="btn-alerter"),
        html.Div(id="out-alerte"),
    ],
    className="card",
)


def register(app):
    @app.callback(
        Output("out-alerte", "children"),
        Input("btn-alerter", "n_clicks"),
        State("store-mails", "data"),
        State("in-alerte-mot", "value"),
        State("in-alerte-dest", "value"),
        prevent_initial_call=True,
    )
    def _alerter(n, mails, mot, dest):
        try:
            nb = mail_filters.alerter_si_mot_cle(mails or [], mot, dest)
        except Exception as e:
            return f"Echec : {e}"
        return f"{nb} alerte(s) envoyée(s) à {dest}."
