from dash import Input, Output, State, dcc, html

from backend.sender import envoyer

layout = html.Div(
    [
        html.H2("Envoyer un mail"),
        dcc.Input(id="in-destinataire", placeholder="Destinataire", type="email"),
        dcc.Input(id="in-nom", placeholder="Nom"),
        dcc.Input(id="in-prenom", placeholder="Prénom"),
        dcc.Textarea(id="in-message", placeholder="Message personnalisé"),
        dcc.Input(id="in-fichier", placeholder="Fichier joint (chemin, optionnel)"),
        html.Button("Envoyer", id="btn-envoyer"),
        html.Div(id="out-envoi"),
    ],
    className="card",
)


def register(app):
    @app.callback(
        Output("out-envoi", "children"),
        Input("btn-envoyer", "n_clicks"),
        State("in-destinataire", "value"),
        State("in-nom", "value"),
        State("in-prenom", "value"),
        State("in-message", "value"),
        State("in-fichier", "value"),
        prevent_initial_call=True,
    )
    def _envoyer(n, dest, nom, prenom, message, fichier):
        envoyer(dest, nom, prenom, message, fichier or None)
        return f"Mail envoyé à {dest}."
