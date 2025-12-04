from crewai import Crew

from agents.advice_agent import advice_agent
from agents.flight_agent import flight_agent
from agents.hotel_agent import hotel_agent
from agents.tour_agent import tour_agent

from tasks.advice_task import advice_task
from tasks.flight_task import flight_task
from tasks.hotel_task import hotel_task
from tasks.tour_task import tour_task

travel_crew = Crew(
    agents=[flight_agent, hotel_agent, tour_agent, advice_agent],
    tasks=[flight_task, hotel_task, tour_task, advice_task],
    verbose=True,
)
