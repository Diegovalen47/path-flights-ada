import Flight


class Node:
    nodes: dict = {}
    nodes_quantity: int = 0

    def __init__(self, id: int, latitude: float, longitude: float):
        self.id: int = id
        self.latitude: float = latitude
        self.longitude: float = longitude
        self.flights: dict = {}
        Node.nodes[id] = self
        Node.nodes_quantity += 1

    def get_flights(self):
        if self.flights:
            return self.flights
        else:
            return None

    def add_flight(self, flight: Flight):
        self.flights[flight.id] = flight

    def delete_flight(self, flight: Flight):
        del self.flights[flight.id]

    def __repr__(self):
        return f"Node(id={self.id}, latitude={self.latitude}, longitude={self.longitude})"
