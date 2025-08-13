from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from agno.playground import Playground, serve_playground_app

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

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[
        TavilyTools(),
        celsius_to_fh,
    ],
    instructions="Use suas ferramentas para pesquisar sobre o GPT-5 da OpenAI",
    debug_mode=True
)

app = Playground(agents=[agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("13_playground:app", reload=True)

#agent.print_response("Qual a temperatura atual em Catalão-GO?")