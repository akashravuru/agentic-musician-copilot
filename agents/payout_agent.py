from tools.payout_tools import calculate_payout


def payout_agent(state):

    try:

        user_input = state["user_input"]

        if "for" not in user_input.lower():
            return {
                "response": "Use: Calculate payout for <venue>"
            }

        venue = user_input.split("for", 1)[1].strip()

        payout = calculate_payout(venue)

        if not payout:
            return {
                "response": f"No gig found for {venue}."
            }

        return {
            "response": f"""
Venue: {venue}

Venue Fee: ₹{payout['fee']:,.0f}
"""
        }

    except Exception as e:
        return {
            "response": f"ERROR: {str(e)}"
        }