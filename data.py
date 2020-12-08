import pandas as pd
import psycopg2

from dotenv import find_dotenv, dotenv_values


def get_db_conn():
    dotenv_dict = dotenv_values(stream=find_dotenv())

    user = "postgres"
    password = dotenv_dict["PG_PASSWORD"]

    return psycopg2.connect(
        host="localhost",
        database="law-school-data",
        user=user,
        password=password
    )

def get_homepage_data():
    db_conn = get_db_conn()

    query = """
        SELECT *
        FROM debt_calc_user.school_stats
    """

    return pd.read_sql(query, db_conn).set_index("school")