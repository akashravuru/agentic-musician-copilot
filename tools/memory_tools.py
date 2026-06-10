import sqlite3
from datetime import datetime
from config import DB_PATH

def save_memory(key, value):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO memory (
            key,
            value,
            updated_at
        )
        VALUES (?, ?, ?)
    """, (
        key,
        value,
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()


def get_memory(key):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT value
        FROM memory
        WHERE key = ?
    """, (key,))

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return None

def get_all_memories():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT key, value
        FROM memory
    """)

    results = cursor.fetchall()

    conn.close()

    return results

def save_band_profile():

    update_band_profile(
        band_name="Moksha",
        genre="Carnatic Progressive Rock",

        vocalist="Akash Ravuru",
        guitarist="Sathwik Kondepogu",
        bassist="Akhilesh Vishwanathan",
        drummer="Thiru Vakkalanka",
        keyboardist="Pranay Mylapally",
        flutist="Swaroop Vyakaranam",

        sound_engineer="Kushal",
        manager="Dinesh Nimmagadda"
    )

def update_band_profile(
    band_name,
    genre,
    vocalist,
    guitarist,
    bassist,
    drummer,
    keyboardist,
    flutist,
    sound_engineer,
    manager
):
    save_memory("band_name", band_name)
    save_memory("genre", genre)

    save_memory("vocalist", vocalist)
    save_memory("guitarist", guitarist)
    save_memory("bassist", bassist)
    save_memory("drummer", drummer)
    save_memory("keyboardist", keyboardist)
    save_memory("flutist", flutist)

    save_memory("sound_engineer", sound_engineer)
    save_memory("manager", manager)