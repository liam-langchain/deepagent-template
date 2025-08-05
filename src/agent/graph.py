"""LangGraph single-node graph template.

Returns a predefined response. Replace logic and configuration as needed.
"""

from deepagents import create_deep_agent
import dotenv

from src.tools.tool import internet_search
from src.prompts.prompt import research_instructions

dotenv.load_dotenv()


# Create the agent
agent = create_deep_agent(
    tools=[internet_search],
    instructions=research_instructions
)

