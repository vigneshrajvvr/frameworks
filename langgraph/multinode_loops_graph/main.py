from langgraph.graph import StateGraph, START, END
from agent_state import AgentState
from setup_node import setup_node
from guess_node import guess_node
from should_continue import should_continue

graph = StateGraph(AgentState)

graph.add_node("setup_node", setup_node)
graph.add_node("guess_node", guess_node)

graph.add_edge(START, "setup_node")
graph.add_edge("setup_node", "guess_node")

graph.add_conditional_edges(
    "guess_node",
    should_continue,
    {
        "end": END,
        "continue": "guess_node"
    }
)

app = graph.compile()

result = app.invoke({"player_name": "Player1", "guesses": [], "attempts": 0, "lower_bound": 1, "upper_bound": 20, "target_value": 0})

print(result)