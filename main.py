import asyncio
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.ui import Console

# Import agents
from config import get_model_client
from scout_agent import create_scout_agent
from planner_agent import create_planner_agent
from reviewer_agent import create_reviewer_agent

async def main():
    client = get_model_client()
    
    # Define the destination here
    target_city = "Paris" 

    # --- TEAM 1: GATHERING CONTEXT ---
    print(f"\n=== STEP 1: SCOUTING {target_city.upper()} ===")
    scout = await create_scout_agent(client)
    
    scout_team = RoundRobinGroupChat(
        participants=[scout],
        termination_condition=TextMentionTermination("TERMINATE")
    )
    
    # Run Team 1
    scout_task = f"Get details for {target_city}."
    scout_result = await scout_team.run(task=scout_task)
    
    # Extract data
    city_data = scout_result.messages[-1].content
    print(f"\n[System] Handoff to Planning Team:\n{city_data}")

    # --- TEAM 2: PLANNING (REFLECTION) ---
    print("\n=== STEP 2: DRAFTING ITINERARY ===")
    planner = await create_planner_agent(client)
    reviewer = await create_reviewer_agent(client)

    planning_team = RoundRobinGroupChat(
        participants=[planner, reviewer],
        termination_condition=TextMentionTermination("APPROVE")
    )

    # Contextual Task
    planning_task = f"""
    Here is the situation on the ground: 
    {city_data}
    
    Create a 3-Day Itinerary. Reviewer, ensure the plan fits the weather conditions perfectly.
    """

    # Run Team 2
    await Console(planning_team.run_stream(task=planning_task))

if __name__ == "__main__":
    asyncio.run(main())