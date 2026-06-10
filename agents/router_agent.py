import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

def classify_intent(user_input):

    prompt = f"""
    Classify the user's request into exactly one category.

    Categories:
    - payment
    - setlist
    - gig

    User Request:
    {user_input}

    Return only the category name.
    """

    response = model.generate_content(prompt)

    return response.text.strip().lower()