import os
import sqlite3

from database.schema import create_tables
from config import DB_PATH
from tools.memory_tools import (
    get_memory,
    save_band_profile
)


def init_db():

    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    create_tables(cursor)

    conn.commit()
    conn.close()

    if not get_memory("band_name"):
        save_band_profile()