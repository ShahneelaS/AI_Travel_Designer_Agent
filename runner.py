from agents.destination_agent import DestinationAgent
from agents.booking_agent import BookingAgent
from agents.explore_agent import ExploreAgent

def run_travel_planner():
    mood = input("What is your travel mood or interest? (relax/adventure/culture): ").lower()

    # Destination Agent
    dest_agent = DestinationAgent()
    suggestions = dest_agent.suggest_destinations(mood)
    print("\n📍 Suggested Destinations:")
    for i, dest in enumerate(suggestions):
        print(f"{i + 1}. {dest}")

    choice = int(input("\nChoose a destination (number): ")) - 1
    destination = suggestions[choice]

    # Booking Agent
    book_agent = BookingAgent()
    flights, hotels = book_agent.book_trip(destination)

    print(f"\n✈️ Available Flights to {destination}:")
    for f in flights:
        print(f"- {f}")

    print(f"\n🏨 Recommended Hotels in {destination}:")
    for h in hotels:
        print(f"- {h}")

    # Explore Agent
    explore_agent = ExploreAgent()
    experiences = explore_agent.suggest_experiences(destination)

    print(f"\n🌟 Things to Explore in {destination}:")
    for item in experiences:
        print(f"- {item}")
