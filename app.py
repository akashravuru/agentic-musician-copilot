from database.db import init_db
from graph.workflow import run_workflow

init_db()

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    result = run_workflow(user_input)

    print("\nCopilot:")
    print(result["response"])