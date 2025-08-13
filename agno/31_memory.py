from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.openai import OpenAIChat
from agno.playground import Playground, serve_playground_app
from dotenv import load_dotenv
load_dotenv()

from agno.memory.v2.memory import Memory
from agno.memory.v2.db.sqlite import SqliteMemoryDb

memory = Memory(
    model=OpenAIChat(id="gpt-4.1-mini"),
    db=SqliteMemoryDb(table_name="user_memories", db_file="temp/agent.db"),
)

agent = Agent(
    name="Agente Pesquisador",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[TavilyTools()],
    instructions="Você é um pesquisador. Responda sempre chamando o usuário de senhor.",
    memory=memory,
    enable_agentic_memory=True,
)

app = Playground(agents=[agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("31_memory:app", reload=True)
