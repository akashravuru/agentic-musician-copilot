import os
import sqlite3

from database.schema import create_tables
from config import DB_PATH


def init_db():

    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    create_tables(cursor)

    conn.commit()
    conn.close()