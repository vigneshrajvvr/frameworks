import random
from agent_state import AgentState

def setup_node(state: AgentState) -> AgentState:
    """Initialize the game with a random target number"""
    state["player_name"] = f"Welcome, {state["player_name"]}!"
    state["target_value"] = random.randint(1, 20)
    print(f"DEBUG: Target number is {state["target_value"]}")
    state["guesses"] = []
    state["attempts"] = 0
    state["hint"] = "Game started! Try to guess the number."
    state["lower_bound"] = 1
    state["higher_bound"] = 20
    print(f"{state["player_name"]} The game has begun. I'm thinking of a number between 1 and 20.")
    return state