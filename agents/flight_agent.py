from crewai import Agent, LLM
from tools.get_flights import get_flights


llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.1
)

flight_agent = Agent(
    role="Flight Search Specialist",
    goal=(
        "Find and provide accurate, up-to-date flight options for the user based "
        "on their departure and arrival airports, including airline, flight number, "
        "departure and arrival times, and flight status."
    ),
    backstory=(
        "You are an expert travel assistant with extensive knowledge of flight schedules, "
        "airlines, and travel planning. You always provide clear, concise, and actionable "
        "flight information to help users plan their trips efficiently."
    ),
    llm=llm,
    tools=[get_flights],
    verbose=True
)
