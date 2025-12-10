from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage
from agent_state import AgentState
from dotenv import load_dotenv
from process_node import process_node

graph = StateGraph(AgentState)

graph.add_node("process_node", process_node)
graph.add_edge(START, "process_node")
graph.add_edge("process_node", END)

graph = graph.compile()

user_input = input("Enter:")
graph.invoke({
    "messages": [HumanMessage(content=user_input)]
})

