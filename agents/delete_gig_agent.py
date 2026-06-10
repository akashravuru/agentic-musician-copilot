from tools.gig_tools import delete_gig


def delete_gig_agent(state):

    user_input = state["user_input"]

    if "delete" not in user_input.lower():

        return {
            "response":
            "Use: Delete gig <venue>"
        }

    venue = (
        user_input
        .replace("Delete gig", "")
        .replace("delete gig", "")
        .strip()
    )

    deleted_rows = delete_gig(venue)

    if deleted_rows == 0:

        return {
            "response":
            f"No gig found for {venue}."
        }

    return {
        "response":
        f"Deleted latest gig for {venue}."
    }