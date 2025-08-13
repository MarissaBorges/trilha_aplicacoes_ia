from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from agno.playground import Playground, serve_playground_app
from agno.storage.sqlite import SqliteStorage
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.document.reader.pdf_reader import PDFReader
from agno.vectordb.chroma import ChromaDb
load_dotenv()

vector_db = ChromaDb(collection="pdf_agent", path="temp/chromadb")

knowledge = PDFKnowledgeBase(
    path="GlobalEVOutlook2025.pdf",
    vector_db=vector_db,
    reader=PDFReader(chunk=True)
)

db = SqliteStorage(table_name="pdf_session", db_file="temp/chromadb/agent.db")

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    name="Agente de PDF",
    add_history_to_messages=True,
    num_history_runs=3,
    storage=db,
    knowledge=knowledge
)

app = Playground(agents=[agent]).get_app()

if __name__ == "__main__":
    # knowledge.load(recreate=True)
    serve_playground_app("22_rag_agent:app", reload=True)