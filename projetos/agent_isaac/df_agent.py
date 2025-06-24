from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
import pandas as pd
from langchain.agents.agent_types import AgentType
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

df = pd.read_csv("df_rent.csv")

agent = create_pandas_dataframe_agent(
    ChatOpenAI(model='gpt-4o-mini'),
    df, verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
)

agent.invoke({'input':"Quantas linhas tem no meu conjunto de dados?"})