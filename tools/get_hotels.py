from dotenv import load_dotenv
import os
from serpapi import GoogleSearch
from crewai.tools import tool

load_dotenv()
serp_api = os.getenv("SERP_API_KEY")


@tool("Get Hotels")
def get_hotels(city: str) -> str:
    """
    Search hotels from Google Hotels using SerpAPI.

    Parameters:
        city (str): The city code or name to search hotels for (e.g., "DXB" or "Bali").

    Returns:
        str: An str including city, check-in/out dates, 
              number of adults, total hotels found, and a list of hotels with
              name, price per night, rating, and reviews.
    """

    params = {
        "engine": "google_hotels",
        "q": f"{city} Resorts",
        "check_in_date": "2025-12-04",
        "check_out_date": "2025-12-05",
        "adults": "2",
        "currency": "USD",
        "api_key": serp_api
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    hotels = []

    for item in results.get("ads", []):
        hotels.append({
            "name": item.get('name'),
            "price_per_night": item.get("price"),
            "rating": item.get("overall_rating"),
            "reviews": item.get("reviews")
        })

    for item in results.get("properties", []):
        hotels.append({
            "name": item.get("name"),
            "price_per_night": item.get("rate_per_night", {}).get("lowest"),
            "rating": item.get("overall_rating"),
            "reviews": item.get("reviews")
        })
    limited_hotels = hotels[:5]

    output = f"\nTop Hotels in {city}\n"

    for h in limited_hotels:
        output += f"\n{h['name']}\n"
        output += f"Price per night: {h['price_per_night']}\n"
        output += f"Rating: {h['rating']}\n"
        output += f"Reviews: {h['reviews']}\n"

    return output
