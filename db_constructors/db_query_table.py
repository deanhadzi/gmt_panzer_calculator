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

def select_all_vehicles(conn):
    """
    Query all rows in the vehicles table.
    :param conn: the connection object
    :return:
    """

    cur = conn.cursor()
    cur.execute("SELECT * FROM soviet_vehicles")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():
    database = "/home/deanhadzi/Desktop/panzer.db"

    # Create a database connection
    conn = create_connection(database)

    with conn:
        select_all_vehicles(conn)

if __name__ == '__main__':
    main()