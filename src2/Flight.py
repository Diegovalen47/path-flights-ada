class Flight:

    flights: dict = {}

    def __init__(self, id: int, origin: int, destination: int):
        self.id: int = id
        self.origin: int = origin
        self.destination: int = destination
        Flight.flights[id] = self

    def __repr__(self):
        return f"Flight(id={self.id}, origen={self.origin}, destino={self.destination})"