from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from agno.playground import Playground, serve_playground_app
from agno.storage.sqlite import SqliteStorage

load_dotenv()

def celsius_to_fh(celsius: float) -> float:
    """
    Converte a temperatura de Celsius para Fahrenheit

    Args:
        celsius (float): A temperatura em Celsius
    Returns:
        float: A temperatura em Fahrenheit
    """
    return (celsius * 9/5) + 32

db = SqliteStorage(table_name="agent_session", db_file="temp/agent.db")

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[
        TavilyTools(),
        celsius_to_fh,
    ],
    debug_mode=True,
    add_history_to_messages=True,
    num_history_runs=3,
    storage=db
)

app = Playground(agents=[agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("21_storage:app", reload=True)

# agent.print_response("Qual a temperatura atual em Catalão-GO?")