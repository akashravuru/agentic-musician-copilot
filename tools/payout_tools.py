import sqlite3

from config import (
    DB_PATH,
    DEFAULT_PERFORMERS,
    SOUND_ENGINEER_PERCENT
)


def calculate_payout(venue):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT fee
    FROM gigs
    WHERE venue = ?
    ORDER BY id DESC
    LIMIT 1
    """, (venue,))

    result = cursor.fetchone()

    conn.close()

    if not result:
        return None

    fee = result[0]

    sound_engineer_share = fee * SOUND_ENGINEER_PERCENT

    band_pool = fee - sound_engineer_share

    per_performer = band_pool / DEFAULT_PERFORMERS

    return {
        "venue": venue,
        "fee": fee,
        "sound_engineer_share": sound_engineer_share,
        "band_pool": band_pool,
        "performers": DEFAULT_PERFORMERS,
        "per_performer": per_performer
    }