from agent_state import AgentState
from langgraph.graph import StateGraph, START, END
from process_node import process_node
from print_node import print_node

graph = StateGraph(AgentState)

graph.add_node("process_node", process_node)
graph.add_node("print_node", print_node)

graph.add_edge(START, "process_node")
graph.add_edge("process_node", "print_node")
graph.add_edge("print_node", END)

app = graph.compile()

app.invoke({"messages":[]})