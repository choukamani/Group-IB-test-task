from langchain.agents import initialize_agent, AgentType
from agent.model_loader import load_model
from agent.tools import tools

llm = load_model()

agent = initialize_agent(tools=tools, llm=llm, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,handle_parsing_errors=True, verbose=True)

def ask_agent(question: str):
    return agent.run(question)
