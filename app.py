import dash
import dash_bootstrap_components as dbc


def get_dash_app():
    external_stylesheets = [dbc.themes.BOOTSTRAP]

    app = dash.Dash(
        __name__, 
        # routes_pathname_prefix='/', 
        external_stylesheets=external_stylesheets,
        suppress_callback_exceptions=True
    )
    
    return app