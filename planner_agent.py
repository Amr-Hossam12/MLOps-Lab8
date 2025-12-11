from autogen_agentchat.agents import AssistantAgent

async def create_planner_agent(model_client):
    return AssistantAgent(
        name="TravelPlanner",
        model_client=model_client,
        system_message="""You are a Senior Travel Planner.
        Create a concise 3-Day Itinerary based on the provided city data.
        
        Rules:
        1. Adapt the plan to the weather (e.g., if Rainy, suggest indoor activities).
        2. Be specific about morning, afternoon, and evening.
        3. Wait for feedback from the TravelAgent.
        4. If the Agent requests changes, rewrite the itinerary.
        """
    )