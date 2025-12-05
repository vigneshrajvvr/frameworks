from agent_state import AgentState
import random

def guess_node(state: AgentState) -> AgentState:
    """Generate a smarter guess based on previous hints"""

    state["attempts"] += 1
    guessedNumber = random.randint(state["lower_bound"], state["upper_bound"])
    print(f"Attempt {state["attempts"]}: I guess the number is {guessedNumber}")
    state["guesses"].append(guessedNumber)

    return state