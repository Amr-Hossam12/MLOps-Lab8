from autogen_agentchat.agents import AssistantAgent

# --- The Tool ---
async def get_city_details(city: str) -> str:
    # Simulating an API call to a weather/travel service
    data = {
        "PARIS": "Weather: Rainy, 12°C. Crowd Level: High. Best for: Museums, Cafes.",
        "TOKYO": "Weather: Sunny, 22°C. Crowd Level: Moderate. Best for: Parks, Shopping, Temples.",
        "CAIRO": "Weather: Hot, 35°C. Crowd Level: Low. Best for: Pyramids, Indoor Bazaars.",
    }
    result = data.get(city.upper())
    if result:
        return f"Current Status for {city.upper()}: {result}"
    return "No data available for this city."

# --- The Agent ---
async def create_scout_agent(model_client):
    return AssistantAgent(
        name="DestinationScout",
        model_client=model_client,
        tools=[get_city_details],
        system_message="""You are a Destination Scout.
        Fetch the current status (weather/crowds) for the requested city.
        Once you have the data, output it clearly and type TERMINATE.
        """
    )