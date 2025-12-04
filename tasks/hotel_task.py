from crewai import Task
from agents.hotel_agent import hotel_agent

hotel_task = Task(
    description=(
        "Search for the best available hotels in {arrival}. "
        "Use the 'Get Hotels' tool to retrieve a curated list of hotels, including hotel name, "
        "location, approximate price, and rating if available."
    ),
    expected_output=(
        "A structured list of hotels, where each hotel includes:\n"
        "- Hotel name\n"
        "- City / location\n"
        "- Approximate price per night\n"
        "- Rating (if available)\n"
        "- Any additional relevant information about the hotel"
    ),
    agent=hotel_agent
)
