import os
from typing import List

from openai import OpenAI
from pydantic import BaseModel, Field


class Activity(BaseModel):
    time: str
    activity: str
    location: str
    notes: str


class DayItinerary(BaseModel):
    day: int
    theme: str
    activities: List[Activity]


class TravelItinerary(BaseModel):
    destination: str
    days: int
    travel_style: str
    itinerary: List[DayItinerary]


def generate_travel_plan(
    destination: str,
    days: int,
    travel_style: str,
) -> TravelItinerary:
    api_key = os.environ.get("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Configure it in your environment before running the program."
        )

    client = OpenAI(api_key=api_key)

    prompt = f"""
Create a {days}-day travel itinerary for {destination}.

Travel style: {travel_style}

For each day, provide a theme and a practical sequence of activities.
For every activity include:
- time
- activity
- location
- useful notes

Keep the plan realistic, well-paced, and useful for a traveler.
Return only the structured itinerary.
"""

    response = client.responses.parse(
        model="gpt-4o-mini",
        instructions=(
            "You are a helpful travel planner. Create practical, realistic "
            "itineraries while following the requested destination, duration, "
            "and travel style."
        ),
        input=prompt,
        text_format=TravelItinerary,
    )

    if response.output_parsed is None:
        raise RuntimeError("The API returned no parsed travel itinerary.")

    return response.output_parsed


if __name__ == "__main__":
    plan = generate_travel_plan(
        destination="Tokyo",
        days=3,
        travel_style="foodie and cultural",
    )

    print(plan.model_dump_json(indent=2))
