# Dash libraries
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Local imports
try:
    # pylint: disable=relative-beyond-top-level
    from .app import get_dash_app
    from .pages import homepage
except:
    from app import get_dash_app
    from pages import homepage


def create_app(server=None):
    dash_app = get_dash_app(server)

    dash_app.layout = homepage.layout

    dash_app.title = "Law School Debt Calculator"

    homepage.deploy_homepage_callbacks(dash_app)

    return dash_app

app = create_app()

server = app.server

if __name__ == '__main__':
    app.run_server(
        debug=True,
        dev_tools_ui=True,
        port=8050,
        host='127.0.0.1'
    )