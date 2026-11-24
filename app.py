from dash import Dash

from frontend.pages.accueil import register as register_accueil
from frontend.pages.alerte import register as register_alerte
from frontend.pages.envoi import register as register_envoi
from frontend.pages.filtres import register as register_filtres
from frontend.pages.inbox import register as register_inbox
from frontend.router import register_router
from frontend.shell import build_shell, register_shell

app = Dash(__name__, suppress_callback_exceptions=True)
app.layout = build_shell()
register_shell(app)
register_router(app)
register_accueil(app)
register_envoi(app)
register_inbox(app)
register_filtres(app)
register_alerte(app)

if __name__ == "__main__":
    app.run(debug=True)
