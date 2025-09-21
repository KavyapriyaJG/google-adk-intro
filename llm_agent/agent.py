from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    name="llm_agent",
    model="gemini-2.0-flash",
    description="Jarvis Agent",
    instruction="""
    You are a helpful assistant that answer simple queries from the user. 
    Be nice and explain in detail.
    """,
)

# root_agent = Agent(
#     name="llm_agent",
#     model=LiteLlm("groq/llama-3.3-70b-versatile"),
#     description="Jarvis Agent",
#     instruction="""
#     You are a helpful assistant that answer simple queries from the user. 
#     Be nice and explain in detail.
#     """,
# )

# adk run llm_agent
# What is a JARVIS for Ironman?
