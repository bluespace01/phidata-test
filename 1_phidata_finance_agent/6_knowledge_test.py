from phi.agent import Agent
from phi.model.ollama import Ollama
from phi.tools.yfinance import YFinanceTools

from phi.vectordb.lancedb import LanceDb, SearchType
from phi.knowledge.text import TextKnowledgeBase
from phi.embedder.ollama import OllamaEmbedder
from pathlib import Path


vector_db=LanceDb(
  table_name="articles",
  uri="tmp/lancedb",
  search_type=SearchType.vector,
  embedder=OllamaEmbedder(model="mxbai-embed-large"),
)

docs_path = Path("docs")
print("Absolute path to docs:", docs_path.resolve())

knowledge_base = TextKnowledgeBase(
  path=docs_path,
  vector_db=vector_db,
  num_documents=5,
)

knowledge_base.load(recreate=True)


knowledge_agent = Agent(
  knowledge=knowledge_base,
  search_knowledge=True,
  debug_mode=True,
  show_tool_calls=True,
  markdown=True,
)

knowledge_agent.print_response(
#   message="How is MongoDB doing?", 
    message="What is MongoDB IPO date and price?", 
    markdown=True,
    stream=True,
    debug_mode=True,
)

# agent = Agent(
#   model=Ollama(id="llama3.2"),
#   tools=[
#     YFinanceTools(
#       stock_price=True, 
#       analyst_recommendations=True, 
#       stock_fundamentals=True
#     )
#   ],
#   instructions="Use tables to display data.",
#   show_tool_calls=True,
#   markdown=True,   
#   debug_mode=True,
# )

# agent.print_response(
#   message="""
#   Tell me which of MDB and ESTC is a better pick.
#   Summarize and show me in tables.
#   """,
#   stream=True
# )