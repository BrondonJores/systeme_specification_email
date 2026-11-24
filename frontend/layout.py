from dash import dcc, dash_table, html


def build_layout():
    return html.Div(
        [
            html.Div(
                [
                    html.H1("Dashboard e-mails"),
                    html.P("Envoi, réception, filtres et alertes en Python"),
                ],
                className="header",
            ),
            html.Nav(
                [
                    html.A("Envoi", href="#envoi"),
                    html.A("Boîte de réception", href="#inbox"),
                    html.A("Filtres", href="#filtres"),
                    html.A("Alertes", href="#alerte"),
                ],
                className="navbar",
            ),
            html.Div(
                [
                    html.Div("-", id="kpi-mails", className="kpi"),
                    html.Div("-", id="kpi-expediteurs", className="kpi"),
                ],
                className="kpi-row",
            ),
            dcc.Store(id="store-mails"),
            html.Div(
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
                id="envoi",
                className="card",
            ),
            html.Div(
                [
                    html.H2("Boîte de réception (5 derniers)"),
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
                    html.Div(
                        [
                            dcc.Graph(id="graph-camembert"),
                            dcc.Graph(id="graph-barres"),
                        ],
                        className="graph-row",
                    ),
                ],
                id="inbox",
                className="card",
            ),
            html.Div(
                [
                    html.H2("Filtre avancé"),
                    dcc.Input(id="in-filtre-exp", placeholder="Expéditeur contient"),
                    dcc.Input(id="in-filtre-sujet", placeholder="Sujet contient"),
                    dcc.Input(id="in-filtre-motif", placeholder="Motif regex dans le corps"),
                    html.Button("Filtrer", id="btn-filtrer"),
                    html.H2("Archivage"),
                    dcc.Input(id="in-categorie", placeholder="Catégorie (factures, perso...)"),
                    html.Button("Archiver le 1er mail affiché", id="btn-archiver"),
                    html.Div(id="out-archive"),
                ],
                id="filtres",
                className="card",
            ),
            html.Div(
                [
                    html.H2("Alerte mot-clé"),
                    dcc.Input(id="in-alerte-mot", placeholder="Mot-clé à surveiller"),
                    dcc.Input(id="in-alerte-dest", placeholder="E-mail d'alerte", type="email"),
                    html.Button("Surveiller", id="btn-alerter"),
                    html.Div(id="out-alerte"),
                ],
                id="alerte",
                className="card",
            ),
        ]
    )
