import sqlite3
from config import DB_PATH

def add_gig(
    venue,
    gig_date,
    fee,
    paid,
    contact_person="",
    notes=""
):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    pending = fee - paid
    payment_status = "Paid" if pending <= 0 else "Pending"

    cursor.execute("""
        INSERT INTO gigs (
            venue,
            gig_date,
            fee,
            paid,
            pending,
            payment_status,
            contact_person,
            notes
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        venue,
        gig_date,
        fee,
        paid,
        pending,
        payment_status,
        contact_person,
        notes
    ))

    conn.commit()
    conn.close()

    return f"Gig added for {venue}"