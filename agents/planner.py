from graph.state import MusicianState
from llm import model
from tools.memory_tools import get_memory

def gig_planner(state):

    band_name = get_memory("band_name")
    genre = get_memory("genre")

    prompt = f"""
    You are a professional live music operations manager.

    Band: {band_name}
    Genre: {genre}

    User Request:
    {state["user_input"]}

    Create:

    1. Rehearsal Plan
    2. Equipment Checklist
    3. Promotion Checklist

    Keep it practical and concise.
    """

    response = model.generate_content(prompt)

    return {
        "response": response.text
    }