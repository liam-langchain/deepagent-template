"""LangGraph single-node graph template.

Returns a predefined response. Replace logic and configuration as needed.
"""

from deepagents import create_deep_agent
import dotenv

from src.tools.tool import internet_search
from src.prompts.prompt import research_instructions, analysis_agent_prompt

dotenv.load_dotenv()


# Example subagent - shows how to create specialized agents
analysis_subagent = {
    "name": "analysis-agent",
    "description": "Specialized agent for detailed data analysis and technical deep-dives",
    "prompt": analysis_agent_prompt,
    "tools": ["internet_search"]
}

# Create the agent with all DeepAgent capabilities
agent = create_deep_agent(
    tools=[internet_search],
    instructions=research_instructions,
    subagents=[analysis_subagent],
    # model=ChatAnthropic(model="claude-3-haiku-20240307")  # Custom model example
)

