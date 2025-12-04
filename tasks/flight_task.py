from crewai import Task
from agents.flight_agent import flight_agent

flight_task = Task(
    description=(
        "Search for the most relevant and available flights from {departure} to {arrival}. "
        "Use the 'Get Flights' tool to retrieve flight options, including airline, flight number, "
        "departure and arrival airports, and scheduled times."
    ),
    expected_output=(
        "A structured list of available flights, where each flight including:\n"
        "- Airline name\n"
        "- Flight number\n"
        "- Flight price\n"
        "- Departure airport\n"
        "- Scheduled departure time\n"
        "- Arrival airport \n"
        "- Scheduled arrival time\n"
    ),
    agent=flight_agent
)
