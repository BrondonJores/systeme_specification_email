from dash import Input, Output

from frontend.pages.accueil import layout as accueil
from frontend.pages.alerte import layout as alerte
from frontend.pages.envoi import layout as envoi
from frontend.pages.filtres import layout as filtres
from frontend.pages.inbox import layout as inbox

PAGES = {
    "/": accueil,
    "/envoi": envoi,
    "/inbox": inbox,
    "/filtres": filtres,
    "/alerte": alerte,
}


def register_router(app):
    @app.callback(
        Output("page-content", "children"),
        Input("url", "pathname"),
    )
    def _route(path):
        return PAGES.get(path, accueil)
