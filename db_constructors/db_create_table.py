import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """
    Create a database connection to a SQLite database.
    :param db_file: path to database file
    :return: connection object or none
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
    :param conn: connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = "/home/deanhadzi/Desktop/panzer.db"

    sql_create_soviet_vehicles_table = """CREATE TABLE IF NOT EXISTS soviet_vehicles (
        id integer PRIMARY KEY,
        dc_id text,
        name text,
        bu integer,
        radio integer,
        pts integer,
        mot text,
        ottv integer,
        cc_sp integer,
        p_sp integer,
        r_sp integer,
        b integer,
        r integer,
        a integer,
        tr_t integer,
        tr_l integer,
        wt real,
        main_wpn text,
        fof text,
        tt integer,
        sb integer,
        st text,
        rof text,
        am integer,
        am_a integer,
        am_s integer,
        am_h integer,
        am_d integer,
        smk integer,
        il integer,
        size integer,
        bgaf integer,
        bgar integer
    );
    """

    # Create a db connection.
    conn = create_connection(database)

    # Create tables
    if conn is not None:
        # Create soviet_vehicles table.
        create_table(conn, sql_create_soviet_vehicles_table)
    else:
        print("Error, cannot create database connection.")


if __name__ == "__main__":
    main()
