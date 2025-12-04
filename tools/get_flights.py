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
        str: An str flight options including price, airline name, flight number,
             departure/arrival details, and flight status
    """
    params = {
        'engine': "google_flights",
        'departure_id': departure,
        'arrival_id': destination,
        "outbound_date": "2025-12-04",
        "return_date": "2025-12-10",
        "currency": "USD",
        "api_key": serp_api
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    flights = results.get("best_flights") or results.get("other_flights") or []

    if not flights:
        return f"No flights found from {departure} to {destination}."

    formatted_output = f"\nTop Flights from {departure} to {destination}\n"

    for idx, flight in enumerate(flights[:3], 1):
        leg1 = flight.get('flights', [])[0]
        leg_last = flight.get('flights', [])[-1]

        airline = leg1.get('airline', 'N/A')
        flight_number = leg1.get('flight_number', 'N/A')

        dep_airport = leg1.get('departure_airport', {})
        arr_airport = leg_last.get('arrival_airport', {})

        price = flight.get('price', 'N/A')

        formatted_output += f"\nFlight #{idx}\n"
        formatted_output += f"Airline: {airline}\n"
        formatted_output += f"Flight Number: {flight_number}\n"
        formatted_output += f"Price: ${price}\n"
        formatted_output += f"Departure: {dep_airport.get('name')} ({dep_airport.get('id')})\n"
        formatted_output += f"Departure Time: {dep_airport.get('time')}\n"
        formatted_output += f"Arrival: {arr_airport.get('name')} ({arr_airport.get('id')})\n"
        formatted_output += f"Arrival Time: {arr_airport.get('time')}\n"

    return formatted_output
