from graph.state import MusicianState
from tools.payment_tools import get_pending_payments
from tools.payment_tools import get_total_pending_amount


def payment_agent(state: MusicianState):

    pending_payments = get_pending_payments()
    total_pending = get_total_pending_amount()

    if not pending_payments:
        return {
            "response": "No pending payments found."
        }

    response = f"Total Pending: ₹{total_pending}\n\n"
    response += "Pending Payments:\n\n"

    for venue, pending, status in pending_payments:
        response += f"{venue}: ₹{pending} ({status})\n"

    return {
        "response": response
    }