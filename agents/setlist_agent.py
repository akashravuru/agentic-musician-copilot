from graph.state import MusicianState
from tools.memory_tools import get_memory
from llm import model


def setlist_agent(state):

    band_name = get_memory("band_name")
    genre = get_memory("genre")
    prompt = f"""
    You are a live performance setlist expert.

    Band: {band_name}
    Genre: {genre}

    User Request:
    {state["user_input"]}

    Create:
    1. Opening Song Type
    2. Energy Build
    3. Peak Moment
    4. Encore Strategy

    Keep it concise.
    """
    response = model.generate_content(prompt)

    return {
    "response": response.text
    }