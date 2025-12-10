from agent_state import AgentState
from langchain_core.messages import HumanMessage
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
# from langchain_openai import ChatOpenAI
import os

load_dotenv()

HF_MODEL_ID=os.getenv("HF_MODEL_ID")
HF_API_TOKEN=os.getenv("HF_API_TOKEN")

# llm = ChatOpenAI(model="gpt-4o") Requires a paid subscription
llm = HuggingFaceEndpoint(
    repo_id=HF_MODEL_ID,
    huggingfacehub_api_token=HF_API_TOKEN,
    task="text-generation"
)

chat_model = ChatHuggingFace(llm=llm)

def process_node(state: AgentState) -> AgentState:
    """To get the openai api responses"""
    response=chat_model.invoke(state["messages"])
    print(f"\nAI: {response.content}")
    return state
