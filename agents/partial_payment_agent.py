import re

from tools.payment_tools import record_partial_payment


def partial_payment_agent(state):

    user_input = state["user_input"]

    pattern = r"received (\d+) from (.*)"

    match = re.search(
        pattern,
        user_input,
        re.IGNORECASE
    )

    if not match:

        return {
            "response":
            "Use: Received <amount> from <venue>"
        }

    amount = float(match.group(1))
    venue = match.group(2).strip()

    result = record_partial_payment(
        venue,
        amount
    )


    if not result:

        return {
            "response":
            f"No gig found for {venue}."
        }

    return {
        "response":
        f"""
Received: ₹{amount:,.0f}

Venue: {venue}

Total Paid: ₹{result['paid']:,.0f}

Pending: ₹{result['pending']:,.0f}

Status: {result['status']}
"""
    }