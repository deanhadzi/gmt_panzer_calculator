import os
import sys

from dotenv import load_dotenv

sys.path.insert(1, "sqlite3_db_logic")
from sqlite3_cookbook import create_connection, select_whole_row
from vehicle_class import Tank


load_dotenv()
DB_FILE = os.getenv("DB_FILEPATH")


def create_tank(tank_name):
    """
    Create a tank instance.
    :param tank_name: str, tank name as spelled on the data card.
    :returns: tank instance.
    """
    conn = create_connection(DB_FILE)

    # Create an empty list to hold all of data.
    tank_data = []
    # Create a list of db names and index position of the data slice
    # we need from those tables.
    tank_data_dbs = [
        ("veh_unit_id", 1),
        ("veh_gen_info", 3),
        ("veh_weapon_data", 3),
        ("veh_def_info", 3),
        ("veh_notes", 3),
    ]

    # Iterate through database matching by tank name.
    for item in tank_data_dbs:
        query = select_whole_row(conn, item[0], "veh_name", f"{tank_name}")[item[1]:]
        tank_data.append(query)

    # Offensive info is the only exception as we are searching by weapon name
    # instead of vehicle name.
    off_info = select_whole_row(conn, "veh_off_info", "wpn_name", f"{tank_data[2][0]}")[2:]
    # Insert off_info into correct position.
    tank_data.insert(3, off_info)

    # Create Tank instance.
    tank = Tank(*tank_data)

    return tank
