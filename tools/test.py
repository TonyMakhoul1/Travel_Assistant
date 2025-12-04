from dotenv import load_dotenv
import os
from serpapi import GoogleSearch
from crewai.tools import tool

load_dotenv()
serp_api = os.getenv("SERP_API_KEY")


@tool("Get Flights")
def get_flights(departure: str, destination: str) -> str:
    """
    Search for flights between two cities using Google Flights via SerpAPI.

    Parameters:
        departure (str): IATA code of the departure city (e.g., "BEY").
        destination (str): IATA code of the destination city (e.g., "DXB").

    Returns:
        str: Formatted flight options including price, airline name, flight number,
             departure/arrival details, and flight status
    """
    params = {
        'engine': "google_flights",
        'departure_id': departure,
        'arrival_id': destination,
        "outbound_date": "2025-12-03",
        "return_date": "2025-12-10",
        "currency": "USD",
        "api_key": serp_api
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    flights = results.get("best_flights") or results.get("other_flights") or []
    if not flights:
        return f"No flights found from {departure} to {destination}."

    return flights
