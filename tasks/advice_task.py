from crewai import Task
from agents.advice_agent import advice_agent

advice_task = Task(
    description=(
        "Provide essential travel advice for the user's destination, including safety "
        "recommendations, cultural insights, local customs, navigation guidance, and useful tips."
    ),
    expected_output=(
        "A structured list of travel advice covering safety, cultural or historical insights, "
        "navigation or transportation tips, and other practical recommendations."
    ),
    agent=advice_agent
)
