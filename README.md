# DeepAgent Template

A comprehensive template for building **Deep Agents** using the [DeepAgents](https://github.com/hwchase17/deepagents) library and [LangGraph Studio](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/).

This template showcases all key DeepAgent capabilities:
- 🔧 **Custom Tools** - Internet search with Tavily
- 🤖 **Subagents** - Specialized agents for different tasks  
- 📁 **File System** - Built-in file operations
- 📋 **Planning Tool** - Task organization and tracking
- 🎨 **LangGraph Studio** - Visual debugging and development

<div align="center">
  <img src="./static/studio_ui.png" alt="Graph view in LangGraph studio UI" width="75%" />
</div>

## Features

### Core DeepAgent Capabilities
- **Planning Tool**: Automatically breaks down complex tasks into manageable steps
- **File System**: Create, read, edit, and manage files within the agent's context
- **Subagents**: Delegate specialized tasks to focused sub-agents
- **Custom Tools**: Extensible tool system for domain-specific functionality
- **LangGraph Integration**: Full compatibility with LangGraph Studio for visual debugging

### Template Structure
```
src/
├── agent/
│   └── graph.py          # Main agent definition
├── tools/
│   └── tool.py           # Custom tools (internet search)
└── prompts/
    └── prompt.py         # Agent prompts and instructions
```

## Quick Start

1. **Install dependencies**
```bash
uv add deepagents tavily-python
pip install -e . "langgraph-cli[inmem]"
```

2. **Set up environment**
```bash
cp .env.example .env
# Add your API keys to .env
```

3. **Start LangGraph Studio**
```bash
langgraph dev
```

4. **Open Studio UI**: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024

## Configuration

### Environment Variables
Create a `.env` file with:
```bash
# Required for internet search
TAVILY_API_KEY=your_tavily_key

# Optional: LangSmith tracing
LANGSMITH_API_KEY=lsv2_your_key
LANGCHAIN_TRACING_V2=true

# Optional: Other LLM providers
ANTHROPIC_API_KEY=your_anthropic_key
OPENAI_API_KEY=your_openai_key
```

### Custom Model
To use a different model, uncomment and modify in `graph.py`:
```python
from langchain_anthropic import ChatAnthropic

agent = create_deep_agent(
    tools=[internet_search],
    instructions=research_instructions,
    subagents=[analysis_subagent],
    model=ChatAnthropic(model="claude-3-haiku-20240307")
)
```

## Customization

### Adding Tools
1. Create your tool function in `src/tools/tool.py`
2. Add it to the tools list in `graph.py`

### Adding Subagents
1. Define the subagent prompt in `src/prompts/prompt.py`
2. Create the subagent config in `graph.py`:
```python
my_subagent = {
    "name": "my-agent",
    "description": "What this agent does",
    "prompt": my_agent_prompt,
    "tools": ["tool_name"]  # Optional: restrict tools
}
```

### Modifying Instructions
Edit `src/prompts/prompt.py` to customize the main agent's behavior and capabilities.

## Development

### File System Usage
The agent has access to a virtual file system. Example usage:
```python
# In your agent interactions:
# - write_file("research.md", "# My Research\n...")
# - read_file("data.json")
# - edit_file("report.txt", old_content, new_content)
```

### Subagent Usage
Call specialized subagents for focused tasks:
```python
# The agent can call: "analysis-agent" for detailed technical analysis
```

### LangGraph Studio
- **Visual Debugging**: See your agent's decision process step-by-step
- **Hot Reload**: Changes to your code are automatically applied
- **State Management**: Edit past states and rerun from any point
- **Thread Management**: Create new conversations with the `+` button

## Example Usage

The template includes a research agent that demonstrates:

1. **Planning**: Breaking down research tasks
2. **Search**: Using Tavily for web research  
3. **Analysis**: Calling subagents for detailed analysis
4. **File Management**: Organizing findings in files
5. **Reporting**: Compiling results into structured reports

Try asking: *"Research the latest developments in AI agents and create a comprehensive report"*

## Resources

- [DeepAgents Documentation](https://github.com/hwchase17/deepagents)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangGraph Studio Guide](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/)
- [Tavily Search API](https://tavily.com/)

## License

MIT