from agent_state import AgentState
from langchain_core.messages import HumanMessage, AIMessage

def print_node(state: AgentState) -> None:
    """Creates a text file which stores the chat history"""
    with open("chat_history.txt", "w") as file:
        file.write("Your Conversation Log:\n")

        for message in state["messages"]:
            if isinstance(message, HumanMessage):
                file.write(f"You: {message.content}\n")
            elif isinstance(message, AIMessage):
                file.write(f"AI: {message.content} \n")
            
        file.write("End of Conversation")

    print("Converstation saved to chat_history.txt")