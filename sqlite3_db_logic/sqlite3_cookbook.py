"""Module that holds SQLite3 helper functions used in this app."""

import os
import sqlite3
from sqlite3 import Error

from dotenv import load_dotenv


load_dotenv()
DB_FILE = os.getenv("DB_FILEPATH")


def create_connection(db_file):
    """
    Create a database connection to a SQLite database.
    :param db_file: path to database file,
    :return: connection object or none.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """
    Create a table from the create_table_sql statement.
    :param conn: connection object,
    :param create_table_sql: a CREATE TABLE statement,
    :return:
    """
    try:
        cur = conn.cursor()
        cur.execute(create_table_sql)
    except Error as e:
        print(e)

    ### EX. create_table_sql = """CREATE TABLE IF NOT EXISTS table_name (
    # id integer PRIMARY KEY,
    # example_column text,
    # example_column2 integer);"""


def print_all_table_values(conn, table_name):
    """
    Query all rows in the table.
    :param conn: the connection object,
    :param table_name: str, table to be searched.
    :return:
    """
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_single_value(conn, table_name, target_col, cond_col, cond_value):
    """
    Query a table to retrieve a single value based on condition.
    :param conn: connection object,
    :param table_name: table to be searched,
    :param target_col: column to be searched,
    :param cond_col: column to be used as condition,
    :param cond_value: value to be matched,
    :return: result.
    """
    cur = conn.cursor()
    cur.execute(
        f"SELECT {target_col} FROM {table_name} WHERE {cond_col} = '{cond_value}'"
    )
    result = cur.fetchone()[0]

    return result


def select_whole_row(conn, table_name, cond_col, cond_value):
    """
    Query a table to retrieve a whole row based on condition.
    :param conn: connection object,
    :param table_name: table to be searched,
    :param cond_col: column to be used as condition,
    :param cond_value: value to be matched,
    :return: result.
    """
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name} WHERE {cond_col} = '{cond_value}'")
    result = cur.fetchall()[0]

    return result


if __name__ == "__main__":
    pass
