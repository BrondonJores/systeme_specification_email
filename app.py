from dash import Dash

from frontend.callbacks import register_callbacks
from frontend.layout import build_layout

app = Dash(__name__)
app.layout = build_layout()
register_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)
