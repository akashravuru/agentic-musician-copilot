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

    payment_status = (
        "Paid"
        if pending <= 0
        else "Pending"
    )

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


def update_gig_fee(venue, new_fee):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT paid
        FROM gigs
        WHERE venue = ?
        ORDER BY id DESC
        LIMIT 1
    """, (venue,))

    result = cursor.fetchone()

    if not result:
        conn.close()
        return f"No gig found for {venue}"

    paid = result[0]

    pending = new_fee - paid

    payment_status = (
        "Paid"
        if pending <= 0
        else "Pending"
    )

    cursor.execute("""
        UPDATE gigs
        SET
            fee = ?,
            pending = ?,
            payment_status = ?
        WHERE id = (
            SELECT id
            FROM gigs
            WHERE venue = ?
            ORDER BY id DESC
            LIMIT 1
        )
    """, (
        new_fee,
        pending,
        payment_status,
        venue
    ))

    conn.commit()
    conn.close()

    return f"{venue} fee updated to ₹{new_fee:,.0f}"