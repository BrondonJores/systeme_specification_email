"""Mise en page Dash (aucune logique mail ici, que du visuel)."""
from dash import dcc, dash_table, html


def build_layout():
    return html.Div(
        [
            html.Div(html.H1("Dashboard e-mails"), className="header"),
            dcc.Store(id="store-mails"),
            # Bloc 1 : envoi personnalisé
            html.Div(
                [
                    html.H2("1. Envoyer un mail"),
                    dcc.Input(id="in-destinataire", placeholder="Destinataire", type="email"),
                    dcc.Input(id="in-nom", placeholder="Nom"),
                    dcc.Input(id="in-prenom", placeholder="Prénom"),
                    dcc.Textarea(id="in-message", placeholder="Message personnalisé"),
                    dcc.Input(id="in-fichier", placeholder="Fichier joint (chemin, optionnel)"),
                    html.Button("Envoyer", id="btn-envoyer"),
                    html.Div(id="out-envoi"),
                ],
                className="card",
            ),
            # Bloc 2 : réception + camembert
            html.Div(
                [
                    html.H2("2. Boîte de réception (5 derniers)"),
                    html.Button("Actualiser", id="btn-refresh"),
                    dash_table.DataTable(
                        id="table-mails",
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
                        style_data_conditional=[
                            {"if": {"row_index": "odd"}, "backgroundColor": "#f4f6f9"}
                        ],
                    ),
                    dcc.Graph(id="graph-camembert"),
                ],
                className="card",
            ),
            # Bloc 3 : filtre + archivage
            html.Div(
                [
                    html.H2("3. Filtre avancé"),
                    dcc.Input(id="in-filtre-exp", placeholder="Expéditeur contient"),
                    dcc.Input(id="in-filtre-sujet", placeholder="Sujet contient"),
                    dcc.Input(id="in-filtre-motif", placeholder="Motif regex dans le corps"),
                    html.Button("Filtrer", id="btn-filtrer"),
                    html.H2("4. Archivage"),
                    dcc.Input(id="in-categorie", placeholder="Catégorie (factures, perso...)"),
                    html.Button("Archiver le 1er mail affiché", id="btn-archiver"),
                    html.Div(id="out-archive"),
                ],
                className="card",
            ),
            # Bloc 4 : alerte
            html.Div(
                [
                    html.H2("5. Alerte mot-clé"),
                    dcc.Input(id="in-alerte-mot", placeholder="Mot-clé à surveiller"),
                    dcc.Input(id="in-alerte-dest", placeholder="E-mail d'alerte", type="email"),
                    html.Button("Surveiller", id="btn-alerter"),
                    html.Div(id="out-alerte"),
                ],
                className="card",
            ),
        ]
    )
