from phi.agent import Agent
from phi.tools.serpapi_tools import SerpApiTools
# from phi.model.groq import Groq
# from phi.tools.googlesearch import GoogleSearch
import os

os.environ["SERP_API_KEY"] = "SERP_API_KEY"
os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"


# agent = Agent(tools=[GoogleSearch()])
agent = Agent(tools=[SerpApiTools()])
agent.print_response("Whats happening in the USA? Give me direct links as well (The links should start from https://)", markdown=True)
