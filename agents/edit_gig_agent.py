import re

from tools.gig_tools import update_gig_fee


def edit_gig_agent(state):

    user_input = state["user_input"]

    pattern = r"update (.*?) fee to (\d+)"

    match = re.search(
        pattern,
        user_input,
        re.IGNORECASE
    )

    if not match:

        return {
            "response":
            "Use: Update <venue> fee to <amount>"
        }

    venue = match.group(1).strip()
    new_fee = float(match.group(2))

    result = update_gig_fee(
        venue,
        new_fee
    )

    return {
        "response": result
    }