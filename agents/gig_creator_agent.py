from graph.state import MusicianState
from tools.gig_tools import add_gig
import re


def gig_creator_agent(state):

    user_input = state["user_input"]

    pattern = r"add gig at (.*?) on (.*?) for (\d+)"

    match = re.search(
        pattern,
        user_input,
        re.IGNORECASE
    )

    if not match:
        return {
            "response":
            "Please use: Add gig at <venue> on <date> for <fee>"
        }

    venue = match.group(1).strip()
    gig_date = match.group(2).strip()
    fee = float(match.group(3))

    result = add_gig(
        venue=venue,
        gig_date=gig_date,
        fee=fee,
        paid=0,
        contact_person="",
        notes=""
    )

    return {
        "response": result
    }