import pandas as pd
import psycopg2

import os


def get_db_conn():
    conn_string = os.environ["DATABASE_URL"]
    return psycopg2.connect(conn_string)

def get_homepage_data():
    db_conn = get_db_conn()

    query = """
        SELECT *
        FROM debt_calc_user.school_stats
    """

    return pd.read_sql(query, db_conn).set_index("school")