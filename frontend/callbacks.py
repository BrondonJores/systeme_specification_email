import plotly.graph_objects as go
from dash import Input, Output, State, ctx

from backend import filters as mail_filters
from backend.reader import lire_derniers
from backend.sender import envoyer
from backend.stats import repartition_expediteurs


def _lignes(mails):
    return [{k: m[k] for k in ("expediteur", "sujet", "date")} for m in mails]


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


def register_callbacks(app):
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

    @app.callback(
        Output("store-mails", "data"),
        Output("table-mails", "data"),
        Output("graph-camembert", "figure"),
        Output("graph-barres", "figure"),
        Output("kpi-mails", "children"),
        Output("kpi-expediteurs", "children"),
        Input("btn-refresh", "n_clicks"),
        Input("btn-filtrer", "n_clicks"),
        State("in-filtre-exp", "value"),
        State("in-filtre-sujet", "value"),
        State("in-filtre-motif", "value"),
        prevent_initial_call=True,
    )
    def _refresh_ou_filtrer(n_refresh, n_filtre, exp, sujet, motif):
        mails = lire_derniers(5)
        affiches = mails
        if ctx.triggered_id == "btn-filtrer":
            affiches = mail_filters.filtrer(
                mails,
                expediteur=exp or None,
                sujet_contient=sujet or None,
                motif=motif or None,
            )
        expediteurs = {m["expediteur"] for m in mails}
        return (
            mails,
            _lignes(affiches),
            _camembert(mails),
            _barres(mails),
            f"{len(mails)} mails lus",
            f"{len(expediteurs)} expéditeurs",
        )

    @app.callback(
        Output("out-archive", "children"),
        Input("btn-archiver", "n_clicks"),
        State("table-mails", "data"),
        State("store-mails", "data"),
        State("in-categorie", "value"),
        prevent_initial_call=True,
    )
    def _archiver(n, lignes, mails, categorie):
        if not lignes or not categorie:
            return "Actualise puis choisis une catégorie."
        sujet = lignes[0]["sujet"]
        mail = next(m for m in (mails or []) if m["sujet"] == sujet)
        chemin = mail_filters.archiver(mail, categorie)
        return f"Archivé : {chemin}"

    @app.callback(
        Output("out-alerte", "children"),
        Input("btn-alerter", "n_clicks"),
        State("store-mails", "data"),
        State("in-alerte-mot", "value"),
        State("in-alerte-dest", "value"),
        prevent_initial_call=True,
    )
    def _alerter(n, mails, mot, dest):
        nb = mail_filters.alerter_si_mot_cle(mails or [], mot, dest)
        return f"{nb} alerte(s) envoyée(s) à {dest}."
