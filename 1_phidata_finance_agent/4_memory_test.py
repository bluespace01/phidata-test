from phi.agent import Agent
from phi.model.groq import Groq

agent = Agent(
    model=Groq(id="llama-3.1-8b-instant"),
    markdown=True, 
    debug_mode=True,
    monitoring=True
    )

agent.print_response("Share me the way to learn python")






