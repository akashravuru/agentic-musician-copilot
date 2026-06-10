from graph.state import MusicianState
from tools.payment_tools import get_pending_payments
from llm import model


def payment_followup_agent(state: MusicianState):

    pending_payments = get_pending_payments()

    if not pending_payments:
        return {
            "response": "No pending payments found."
        }

    user_input = state["user_input"].lower()

    target_venue = None

    if "for" in user_input:
        target_venue = state["user_input"].split(
            "for",
            1
        )[1].strip()

    venue = None
    pending = None

    if target_venue:

        for payment_venue, amount, status in pending_payments:

            if payment_venue.lower() == target_venue.lower():

                venue = payment_venue
                pending = amount
                break

    if venue is None:

        venue, pending, status = pending_payments[0]

    prompt = f"""
    You are the manager of the band Moksha.

    Generate ONE WhatsApp payment follow-up message.

    Venue: {venue}
    Pending Amount: ₹{pending}

    Rules:
    - Return only the message
    - No multiple options
    - No explanations
    - No headings
    - No analysis
    - Professional and friendly
    - Maximum 80 words
    """

    try:

        response = model.generate_content(prompt)

        return {
            "response": response.text.strip()
        }

    except Exception:

        return {
            "response":
            "Payment follow-up generation is temporarily unavailable. Please try again later."
        }