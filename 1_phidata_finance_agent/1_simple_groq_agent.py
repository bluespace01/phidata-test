from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.ollama import Ollama
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    # model=Groq(id="llama-3.3-70b-versatil
    # model=Groq(id="llama-3.1-8b-instant"),
    model=Ollama(id="llama3.1"),
    markdown=True,
    debug=True
)

agent.print_response("Share a 2 jokes.")