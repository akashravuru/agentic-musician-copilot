from graph.state import MusicianState
from llm import model
from tools.memory_tools import get_memory
import json
from tools.gig_tools import add_gig

def gig_creator_agent(state):

    band_name = get_memory("band_name")

    prompt = f"""
    Extract the following information from the user request.

    Return ONLY valid JSON.

    Fields:

    venue
    gig_date
    fee

    Band:
    {band_name}

    User Request:
    {state["user_input"]}
    """

    response = model.generate_content(prompt)
    
    cleaned_response = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    gig_data = json.loads(cleaned_response)
    result = add_gig(
        venue=gig_data["venue"],
        gig_date=gig_data["gig_date"],
        fee=gig_data["fee"],
        paid=0,
        contact_person="",
        notes=""
    )

    return {
        "response": result
    }
    