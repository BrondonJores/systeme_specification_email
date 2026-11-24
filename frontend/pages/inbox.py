from dash import Input, Output, dash_table, html

layout = html.Div(
    [
        html.H2("Boîte de réception (5 derniers)"),
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
    ],
    className="card",
)


def register(app):
    @app.callback(
        Output("table-mails", "data"),
        Input("store-mails", "data"),
    )
    def _afficher(mails):
        return [{k: m[k] for k in ("expediteur", "sujet", "date")} for m in (mails or [])]
