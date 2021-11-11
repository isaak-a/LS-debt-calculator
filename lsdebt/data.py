import logging
import os

import pandas as pd
import psycopg2


log = logging.getLogger('app.db')


def get_db_conn():
    conn_string = os.environ["DATABASE_URL"]

    log.info("Connecting to PostGres")
    connect = psycopg2.connect(conn_string)
    
    return connect


def get_homepage_data():
    db_conn = get_db_conn()

    log.info("Fetching homepage data")
    query = """
        SELECT *
        FROM debt_calc_user.school_stats
    """
    return pd.read_sql(query, db_conn).set_index("school")
