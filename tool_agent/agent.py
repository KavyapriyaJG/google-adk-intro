from google.adk.agents import Agent
from google.adk.tools import google_search
import random

def get_ironman_fact():
    facts = [
        "Iron Man's real name is Tony Stark.",
        "Tony Stark built his first suit in a cave with limited resources.",
        "Iron Man is one of the founding members of the Avengers.",
        "The Iron Man suit is powered by an Arc Reactor.",
        "Robert Downey Jr. played Iron Man in the Marvel Cinematic Universe.",
        "Tony Stark's AI assistant is named JARVIS.",
        "Iron Man's suit has over 50 different versions in the comics and movies.",
    ]
    return random.choice(facts)


# root_agent = Agent(
#     name="tool_agent",
#     model="gemini-2.0-flash",
#     description="Jarvis Agent with a Tool",
#     instruction="""
#     You are a helpful assistant that can use the following tools:
#     - google_search
#     """,
#     tools=[google_search],
#     # tools=[get_current_time]
# )


root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Jarvis Agent with a Tool",
    instruction="""
    When user asks with any question, answer with a fact about Ironman and continue conversation.
    You are a helpful assistant that can use the following tools:
    - get_ironman_fact
    """,
    tools=[get_ironman_fact]
)

# What is the current weather in New York?
# Hi
