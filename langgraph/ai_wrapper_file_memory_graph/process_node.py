from agent_state import AgentState
from langchain_core.messages import HumanMessage, AIMessage
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_ID=os.getenv("HF_MODEL_ID")
API_TOKEN=os.getenv("HF_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id=MODEL_ID,
    huggingfacehub_api_token=API_TOKEN,
    task="text-generation"
)

chat_bot=ChatHuggingFace(llm=llm)

def process_node(state: AgentState) -> AgentState:
    """Wraps the Human and AI conversations"""
    user_input=input("Human: ")

    while user_input != "exit":
        state["messages"].append(HumanMessage(content=user_input))
        response=chat_bot.invoke(
            state["messages"]
        )
        print(f"AI Message: {response.content}")
        state["messages"].append(AIMessage(content=response.content))
        user_input=input("Human: ")
