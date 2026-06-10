from graph.router import route_request

from agents.planner import gig_planner
from agents.payment_agent import payment_agent
from agents.setlist_agent import setlist_agent
from agents.gig_creator_agent import gig_creator_agent
from agents.payment_followup_agent import payment_followup_agent
from agents.payout_agent import payout_agent
from agents.payment_received_agent import payment_received_agent


def run_workflow(user_input):

    state = {
        "user_input": user_input,
        "intent": None,
        "response": None
    }

    state.update(route_request(state))

    if state["intent"] == "create_gig":
        state.update(gig_creator_agent(state))

    elif state["intent"] == "gig":
        state.update(gig_planner(state))

    elif state["intent"] == "payment_received":
        state.update(payment_received_agent(state))

    elif state["intent"] == "payment_followup":
        state.update(payment_followup_agent(state))

    elif state["intent"] == "payment":
        state.update(payment_agent(state))

    elif state["intent"] == "payout":
        state.update(payout_agent(state))

    elif state["intent"] == "setlist":
        state.update(setlist_agent(state))

    else:
        state["response"] = "Sorry, I don't understand that request."

    return state