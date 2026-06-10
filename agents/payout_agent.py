import json

from llm import model
from tools.payout_tools import calculate_payout


def payout_agent(state):

    prompt = f"""
    Extract the venue name from the user's request.

    User Request:
    {state["user_input"]}

    Return ONLY valid JSON.

    Example:
    {{
        "venue": "Prism"
    }}
    """

    response = model.generate_content(prompt)

    cleaned_response = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    venue_data = json.loads(cleaned_response)

    venue = venue_data["venue"]

    payout = calculate_payout(venue)

    if not payout:
        return {
            "response": f"No gig found for {venue}."
        }

    return {
        "response": f"""
Venue: {venue}

Venue Fee: ₹{payout['fee']:,.0f}

Sound Engineer (10%):
₹{payout['sound_engineer_share']:,.0f}

Band Pool:
₹{payout['band_pool']:,.0f}

Performers:
{payout['performers']}

Per Performer:
₹{payout['per_performer']:,.0f}
"""
    }