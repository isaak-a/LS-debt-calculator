import logging

from app import get_dash_app
import pages.homepage as hp


def create_app():
    dash_app = get_dash_app()

    dash_app.layout = hp.layout
    dash_app.title = "Law School Debt Calculator"

    hp.deploy_homepage_callbacks(dash_app)

    return dash_app

app = create_app()

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.logger.info("Loaded Gunicorn logger and handlers")

server = app.server

if __name__ == '__main__':
    logging.basicConfig(level='INFO')
    app.run_server(
        debug=True,
        dev_tools_ui=True,
        port=8050,
        host='localhost'
    )
