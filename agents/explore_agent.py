class ExploreAgent:
    def suggest_experiences(self, destination):
        experiences = {
            "Bali": ["Ubud Monkey Forest", "Beach Yoga", "Seafood BBQ"],
            "Nepal": ["Trekking to Everest Base Camp", "Momo Tasting", "Temples Tour"],
            "London": ["Big Ben", "River Thames Cruise", "Fish & Chips"],
        }
        return experiences.get(destination, ["Explore the city and try local food."])
