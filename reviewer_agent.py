from autogen_agentchat.agents import AssistantAgent

async def create_reviewer_agent(model_client):
    return AssistantAgent(
        name="TravelAgent",
        model_client=model_client,
        system_message="""You are the Lead Travel Agent (Supervisor).
        Review the itinerary proposed by the Planner.
        
        Check for:
        1. Weather Logic: Does the plan fit the weather? (No parks if raining!)
        2. Pacing: Is the day too busy?
        
        If the plan is solid, output ONLY the word "APPROVE".
        If not, give specific feedback on what to change.
        """
    )