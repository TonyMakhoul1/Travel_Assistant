from dotenv import load_dotenv
from crew import travel_crew

load_dotenv()


def run(departure: str, arrival: str):
    inputs = {
        "departure": departure,
        "arrival": arrival
    }
    result = travel_crew.kickoff(inputs=inputs)

    flights = result.get("Flight Search Specialist", "No flight info")
    hotels = result.get("Hotel Search Specialist", "No hotel info")
    itinerary = result.get("Travel Itinerary Specialist", "No itinerary")
    safety = result.get("Travel Advice & Safety Specialist", "No safety tips")

    final_report = f"""
# COMPLETE DUBAI TRAVEL PLAN

## Flights
{flights}

## Hotels
{hotels}

## 7-Day Itinerary
{itinerary}

## Safety & Travel Tips
{safety}
"""

    print(final_report)


if __name__ == "__main__":
    departure = input("Departure city or airport code: ").upper()
    arrival = input("Arrival city or airport code: ").upper()

    if not departure.strip() or not arrival.strip():
        print("Both Departure and Arrival are required!")
    else:
        run(departure=departure, arrival=arrival)
