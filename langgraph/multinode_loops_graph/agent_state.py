from typing import TypedDict, List

class AgentState(TypedDict):
    player_name: str
    guesses: List[str]
    attempts: int
    lower_bound: int
    upper_bound: int
    target_value: int
