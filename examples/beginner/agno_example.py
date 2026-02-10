"""Research Assistant Agent with Web Search

A Bindu agent that performs research using DuckDuckGo web search.
Provides comprehensive, well-researched answers on any topic.

Features:
- Web search via DuckDuckGo
- Research and summarization capabilities
- OpenRouter integration with gpt-oss-120b

Usage:
    python agno_example.py

Environment:
    Requires OPENROUTER_API_KEY in .env file
"""

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from bindu.penguin.bindufy import bindufy
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.openrouter import OpenRouter

# Define your agent
agent = Agent(
    instructions="You are a research assistant that finds and summarizes information.",
    model=OpenRouter(id="openai/gpt-oss-120b"),
    tools=[DuckDuckGoTools()],
)

# Configuration
# Note: Infrastructure configs (storage, scheduler, sentry, API keys) are now
# automatically loaded from environment variables. See .env.example for details.
config = {
    "author": "your.email@example.com",
    "name": "research_agent",
    "description": "A research assistant agent",
    "deployment": {
        "url": "http://localhost:3773",
        "expose": True,
        "cors_origins": ["http://localhost:5173"]
    },
    "skills": ["skills/question-answering", "skills/pdf-processing"],
    
    # Negotiation API keys loaded from: OPENROUTER_API_KEY, MEM0_API_KEY, EXA_API_KEY
}


# Handler function
def handler(messages: list[dict[str, str]]):
    """Process messages and return agent response.

    Args:
        messages: List of message dictionaries containing conversation history

    Returns:
        Agent response result
    """
    result = agent.run(input=messages)
    return result


# Bindu-fy it
bindufy(config, handler)