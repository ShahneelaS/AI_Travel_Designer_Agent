class DestinationAgent:
    def suggest_destinations(self, mood):
        if "relax" in mood:
            return ["Bali", "Maldives", "Goa"]
        elif "adventure" in mood:
            return ["Switzerland", "Nepal", "New Zealand"]
        else:
            return ["London", "Tokyo", "Istanbul"]
