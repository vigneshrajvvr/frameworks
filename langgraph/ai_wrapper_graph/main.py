from langgraph.graph import StateGraph, START, END
from agent_state import AgentState
from dotenv import load_dotenv
from process_node import process_node

load_dotenv()
graph = StateGraph(AgentState)

graph.add_node("process_node", process_node)
graph.add_edge(START, "process_node")
graph.add_edge("process_node", END)

graph = graph.compile()

graph.invoke({"messages": ["Hello!"]})

