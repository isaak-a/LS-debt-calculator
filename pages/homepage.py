# Load dash libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

# Load data libraries
import numpy as np
import pandas as pd

# Load local modules
try:
    # pylint: disable=relative-beyond-top-level
    from ..data import get_homepage_data
except:
    from data import get_homepage_data



###################################################################################################
######################################### Data Loading ############################################
###################################################################################################

school_df = get_homepage_data()


###################################################################################################
######################################### Dash Components #########################################
###################################################################################################

school_dropdown = dcc.Dropdown(
    id='school-dropdown',
    className="dropdown",
    options=[{"label":school, "value":school} for school in school_df.index],
    placeholder="Select Law School",
    searchable=True,
    clearable=True,
    multi=False
)


def get_form(label, placeholder, input_id=""):
    return dbc.FormGroup(
        [
            dbc.Label(label, className="form-label"),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon("$", addon_type="prepend"),
                    dbc.Input(
                        id=input_id,
                        placeholder=placeholder,
                        className="form-input"
                    ),
                ]
            )
        ],
        className="homepage-form"
    )


def get_form_col(label, placeholder, input_id=""):
    return dbc.Col(
        get_form(label, placeholder, input_id=input_id),
        sm=2,
        xs=11,
        className="form-col"
    )



###################################################################################################
######################################### Page Layout #############################################
###################################################################################################

layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H1(
                    "Law School Debt Calculator",
                    id="homepage-header"
                )
            )
        ),
        dbc.Row(
            dbc.Col(
                school_dropdown,
                sm=4,
                xs=11
            ),
            justify="center",
            className="homepage-row"
        ),
        dbc.Row(
            [
                html.P("3 x", className="operator"),
                html.P("(", className="parenthesis"),
                get_form_col("Tuition per Year", "XX,XXX", input_id="tuition-input"),
                html.P("+", className="operator"),
                get_form_col("Fees per Year", "X,XXX", input_id="fees-input"),
                html.P("+", className="operator"),
                get_form_col("Cost of Living per Year", "X,XXX", input_id="col-input"),
                html.P(")", className="parenthesis"),
                html.P(" -", className="operator"),
                get_form_col("Scholarships/Grants (3yr Total)", "XX,XXX", input_id="grants-input"),
            ],
            justify="center",
            align="center",
            className="homepage-row"
        ),
        dbc.Row(
            dbc.Col(
                [
                    html.P("Estimated Debt", id="debt-header"),
                    html.P("$XXX,XXX", id="debt-total")
                ],
                sm=6,
                xs=11
            ),
            justify="center",
            className="homepage-row",
            id="debt-row"
        ),
    ],
    fluid=True
)





###################################################################################################
######################################### Callbacks ###############################################
###################################################################################################

def deploy_homepage_callbacks(app):
    @app.callback(
        [Output(component_id="tuition-input", component_property="value"),
         Output("fees-input", "value"),
         Output("col-input", "value"),
         Output("grants-input", "value"),],

        [Input("school-dropdown", "value")]
    ) #pylint: disable=unused-variable
    def update_formula_auto(school):
        if school:
            tuition = school_df.loc[school, "tuition_per_year"]
            fees = school_df.loc[school, "fees_per_year"]
            col = school_df.loc[school, "col_off_campus"]
            grant = school_df.loc[school, "median_grant"]

            num_list = [tuition, fees, col, grant]

            # Format numbers with commas for output
            return_list = ["{:,.2f}".format(num) for num in num_list]

            return return_list
        else:
            return [None]*4


    @app.callback(
        [Output("debt-total", "children"),],

        [Input("tuition-input", "value"),
         Input("fees-input", "value"),
         Input("col-input", "value"),
         Input("grants-input", "value"),]
    ) #pylint: disable=unused-variable
    def update_formula_input(tuition, fees, col, grants):
        if (tuition and fees and col and grants):
            # Clean inputs
            inputs = {
                "tuition":tuition,
                "fees":fees,
                "col":col,
                "grants":grants
            }

            inputs = {k: float(v.replace(",", "")) for k, v in inputs.items()}

            debt = 3*(inputs["tuition"] + inputs["fees"] + inputs["col"]) - inputs["grants"]
            
            return ["${:,.2f}".format(debt)]
        else:
            return ["$XXX,XXX"]
