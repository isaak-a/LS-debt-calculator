import dash
import dash_bootstrap_components as dbc


def get_dash_app(server):
    external_stylesheets = [dbc.themes.BOOTSTRAP]

    if server == None:
        app = dash.Dash(
            __name__, 
            # routes_pathname_prefix='/', 
            external_stylesheets=external_stylesheets,
            suppress_callback_exceptions=True
        )
    else:
        app = dash.Dash(
            __name__, 
            server=server,
            # routes_pathname_prefix='/',  
            external_stylesheets=external_stylesheets
        )
    
    return app