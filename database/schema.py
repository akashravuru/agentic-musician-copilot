def create_tables(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS gigs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        venue TEXT,
        gig_date TEXT,
        fee REAL,
        paid REAL DEFAULT 0,
        pending REAL DEFAULT 0,
        payment_status TEXT,
        contact_person TEXT,
        notes TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        key TEXT UNIQUE,
        value TEXT,
        updated_at TEXT
    )
    """)