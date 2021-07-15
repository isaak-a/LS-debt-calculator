import dash
import dash_bootstrap_components as dbc

site_description = (
    "Law School Debt Calculator - How in the hole will you "
    "be after law school? Quickly estimate your post-law "
    "school debt to make an informed decision about which school to choose. "
)

site_keywords = "law school,law school debt,law school calculator,law school data"

def get_dash_app():
    external_stylesheets = [dbc.themes.BOOTSTRAP]
    meta_tags=[
        {
            "name": "viewport", 
            "content": "width=device-width, initial-scale=1, user-scalable=no, minimum-scale=1",
            "description": site_description,
            "keywords": site_keywords
        }
    ]

    app = dash.Dash(
        __name__, 
        # routes_pathname_prefix='/', 
        external_stylesheets=external_stylesheets,
        meta_tags=meta_tags,
        suppress_callback_exceptions=True
    )
    
    return app