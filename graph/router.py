from graph.state import MusicianState


def route_request(state: MusicianState):

    user_input = state["user_input"].lower()

    

    if (
        "has paid" in user_input
        or "paid us" in user_input
        or "payment received" in user_input
        or "received payment" in user_input
        or "cleared payment" in user_input
        or "settled payment" in user_input
    ):
        return {"intent": "payment_received"}
    elif "received" in user_input and any(
        char.isdigit() for char in user_input
    ):
        return {"intent": "partial_payment"}

    elif "follow-up" in user_input or "follow up" in user_input:
        return {"intent": "payment_followup"}
    
    elif "update" in user_input and "fee" in user_input:
        return {"intent": "edit_gig"}

    elif "payout" in user_input or "split" in user_input:
        return {"intent": "payout"}

    elif "payment" in user_input or "owe" in user_input:
        return {"intent": "payment"}

    elif "setlist" in user_input:
        return {"intent": "setlist"}
    
    elif "add" in user_input and "gig" in user_input:
        return {"intent": "create_gig"}
    
    elif "delete gig" in user_input:
        return {"intent": "delete_gig"}

    elif "gig" in user_input:
        return {"intent": "gig"}s

    return {"intent": "unknown"}