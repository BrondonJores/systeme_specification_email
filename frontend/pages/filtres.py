from dash import Input, Output, State, dcc, dash_table, html

from backend import filters as mail_filters

layout = html.Div(
    [
        html.H2("Filtre avancé"),
        dcc.Input(id="in-filtre-exp", placeholder="Expéditeur contient"),
        dcc.Input(id="in-filtre-sujet", placeholder="Sujet contient"),
        dcc.Input(id="in-filtre-motif", placeholder="Motif regex dans le corps"),
        html.Button("Filtrer", id="btn-filtrer"),
        dash_table.DataTable(
            id="table-filtres",
            columns=[
                {"name": "Expéditeur", "id": "expediteur"},
                {"name": "Sujet", "id": "sujet"},
                {"name": "Date", "id": "date"},
            ],
            style_cell={"textAlign": "left", "padding": "8px"},
            style_header={
                "backgroundColor": "#1f3a5f",
                "color": "white",
                "fontWeight": "bold",
            },
        ),
        html.H2("Archivage"),
        dcc.Input(id="in-categorie", placeholder="Catégorie (factures, perso...)"),
        html.Button("Archiver le 1er mail affiché", id="btn-archiver"),
        html.Div(id="out-archive"),
    ],
    className="card",
)


def register(app):
    @app.callback(
        Output("table-filtres", "data"),
        Input("btn-filtrer", "n_clicks"),
        State("store-mails", "data"),
        State("in-filtre-exp", "value"),
        State("in-filtre-sujet", "value"),
        State("in-filtre-motif", "value"),
        prevent_initial_call=True,
    )
    def _filtrer(n, mails, exp, sujet, motif):
        trouves = mail_filters.filtrer(
            mails or [],
            expediteur=exp or None,
            sujet_contient=sujet or None,
            motif=motif or None,
        )
        return [{k: m[k] for k in ("expediteur", "sujet", "date")} for m in trouves]

    @app.callback(
        Output("out-archive", "children"),
        Input("btn-archiver", "n_clicks"),
        State("table-filtres", "data"),
        State("store-mails", "data"),
        State("in-categorie", "value"),
        prevent_initial_call=True,
    )
    def _archiver(n, lignes, mails, categorie):
        if not lignes or not categorie:
            return "Filtre puis choisis une catégorie."
        sujet = lignes[0]["sujet"]
        mail = next(m for m in (mails or []) if m["sujet"] == sujet)
        chemin = mail_filters.archiver(mail, categorie)
        return f"Archivé : {chemin}"
