from crewai import Task
from agents.tour_agent import tour_agent

tour_task = Task(
    description=(
        "Create a complete and enjoyable travel itinerary for the user in {arrival}. "
        "The itinerary should include recommended attractions, activities, cultural experiences, "
        "local food suggestions, and any unique things to do in the destination. "
        "Organize the plan in a clear schedule (morning, afternoon, evening) and make it both practical "
        "and exciting for the traveler."
    ),
    expected_output=(
        "A structured, day-by-day itinerary for the destination {arrival}, including:\n"
        "- Top attractions to visit\n"
        "- Activities for morning, afternoon, and evening\n"
        "- Cultural or historical experiences\n"
        "- Food and restaurant recommendations\n"
        "The output should be engaging, helpful, and tailored to creating a memorable trip."
    ),
    agent=tour_agent
)
