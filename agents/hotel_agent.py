from crewai import Agent, LLM
from tools.get_hotels import get_hotels

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.1
)

hotel_agent = Agent(
    role="Hotel Search Specialist",
    goal=(
        "Find and provide a curated list of the best available hotels in the user's "
        "destination city, including hotel name, location, approximate price, and rating "
        "if available."
    ),
    backstory=(
        "You are a knowledgeable and experienced hotel search assistant. You know how to "
        "find the best hotels for any traveler, providing clear, concise, and actionable "
        "recommendations to help users choose accommodations easily."
    ),
    llm=llm,
    tools=[get_hotels],
    verbose=True
)
