"""
This is an agent using Google ADK with Gemini model and Google Search tool.
It includes a helper function to display styled instructions for starting the ADK web UI.
"""

from dotenv import load_dotenv

import asyncio
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search
from google.genai import types
from IPython.display import display, HTML


retry_config=types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1, # Initial delay before first retry (in seconds)
    http_status_codes=[429, 500, 503, 504] # Retry on these HTTP errors
)

# Agent implementation
root_agent = Agent(
    name="Google_Assistant",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    description="A simple agent that can answer general questions.",
    instruction="You are a helpful assistant. Use Google Search for current info or if unsure.",
    tools=[google_search],
)

print("Root Agent defined.")


runner = InMemoryRunner(agent=root_agent)
print("InMemoryRunner created with Root Agent.")

async def main():
    # run_debug to see step-by-step reasoning
    response = await runner.run_debug(
        "What are some important concepts to master in Finance?"
    )
    print("Agent Response:", response)


if __name__ == "__main__":

    load_dotenv()
    asyncio.run(main())