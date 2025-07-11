from tools import get_flights, suggest_hotels

class BookingAgent:
    def book_trip(self, destination):
        flights = get_flights(destination)
        hotels = suggest_hotels(destination)
        return flights, hotels
