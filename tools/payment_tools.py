import sqlite3

from config import DB_PATH


def get_pending_payments():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT venue, pending, payment_status
        FROM gigs
        WHERE pending > 0
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_total_pending_amount():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(pending)
        FROM gigs
        WHERE pending > 0
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total or 0


def get_all_gigs():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            venue,
            gig_date,
            fee,
            payment_status
        FROM gigs
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_total_gigs():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM gigs
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


def mark_paid(venue):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE gigs
        SET
            paid = fee,
            pending = 0,
            payment_status = 'Paid'
        WHERE venue = ?
    """, (venue,))

    conn.commit()

    updated_rows = cursor.rowcount

    conn.close()

    return updated_rows