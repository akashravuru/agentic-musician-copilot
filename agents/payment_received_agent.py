from tools.payment_tools import mark_paid


def payment_received_agent(state):

    user_input = state["user_input"]

    venue = None

    if "from" in user_input.lower():
        venue = user_input.split("from", 1)[1].strip()

    elif "has paid" in user_input.lower():
        venue = user_input.lower().replace("has paid", "").strip()

    elif "paid us" in user_input.lower():
        venue = user_input.lower().replace("paid us", "").strip()

    elif "cleared payment" in user_input.lower():
        venue = user_input.lower().replace("cleared payment", "").strip()

    elif "settled payment" in user_input.lower():
        venue = user_input.lower().replace("settled payment", "").strip()

    if not venue:
        return {
            "response": "Could not identify the venue."
        }

    updated_rows = mark_paid(venue.title())

    if updated_rows == 0:
        return {
            "response": f"No pending gig found for {venue.title()}."
        }

    return {
        "response": f"Payment received. {venue.title()} marked as Paid."
    }