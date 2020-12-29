import dash
import dash_bootstrap_components as dbc


def get_dash_app():
    external_stylesheets = [dbc.themes.BOOTSTRAP]
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1, user-scalable=no"},
        {"name": "http-equiv", "content": "autoRotate:disabled"}
    ]

    app = dash.Dash(
        __name__, 
        # routes_pathname_prefix='/', 
        external_stylesheets=external_stylesheets,
        meta_tags=meta_tags,
        suppress_callback_exceptions=True
    )
    
    return app