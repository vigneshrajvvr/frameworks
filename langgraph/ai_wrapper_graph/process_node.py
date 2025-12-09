from langchain_openai import ChatOpenAI
from agent_state import AgentState
from langchain_core.messages import HumanMessage

def process_node(state: AgentState) -> AgentState:
    """To get the openai api responses"""
    llm = ChatOpenAI(model="gpt-4o")
    user_input = input("Enter:")
    response=llm.invoke({"message": [HumanMessage(content=user_input)]})
    print(f"\nAI: {response.content}")
    return state
