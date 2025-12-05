from agent_state import AgentState

def should_continue(state: AgentState) -> AgentState:
    latest_guess = state["guesses"][-1]

    if latest_guess == state["target_value"]:
        print("GAME OVER: Number found!")
        return "end"
    elif state["attempts"] >= 7:
        print(f"GAME OVER: Maximum attempts reached! The number was {state["target_value"]}")
        return "end"
    else:
        print(f"CONTINUING: {state["attempts"]}/7 attempts used")
        return "continue"        