from phi.agent import Agent
from phi.tools.yfinance import YFinanceTools
from phi.storage.agent.sqlite import SqlAgentStorage

from phi.agent import AgentMemory
from phi.memory.db.sqlite import SqliteMemoryDb

from phi.model.ollama import Ollama
from phi.model.groq import Groq


agent = Agent(
  #model=Ollama(id="llama3.2"),
  #model=Groq(id="llama-3.1-8b-instant"),
  model=Groq(id="llama-3.3-70b-versatile"),

  tools=[YFinanceTools(
    stock_price=True, 
    analyst_recommendations=True, 
    stock_fundamentals=True
  )],

  instructions="Use tables to display data.",
  show_tool_calls=True, 
  markdown=True,
  add_history_to_messages=True,
  debug_mode=True,

  storage=SqlAgentStorage(
    table_name="agent_sessions", db_file="tmp/agent_storage.db"
  ),
  memory=AgentMemory(
    db=SqliteMemoryDb(
      table_name="agent_memory", 
      db_file="tmp/agent_memory.db",
    ),
    create_user_memories=True, 
    update_user_memories_after_run=True,
  ),
  user_id="john_billings",
)

agent.print_response(
  message="""
  My name is Mark and I have the following holdings:
  10,000 of SNOW
  2,000 of MDB
  4,500 of DDOG
  """,
  stream=True
)


agent.print_response(
  message="""
  What's the current stock value of my portfolio?
  """,
  stream=True
)

