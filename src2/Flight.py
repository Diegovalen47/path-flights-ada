from collections import deque


class Flight:
    flights: dict = {}

    def __init__(self, id: int, origin: int, destination: int):
        self.id: int = id
        self.origin: int = origin
        self.destination: int = destination
        self.nodes: deque = deque([])
        self.cost: int = 0
        Flight.flights[id] = self

    def set_nodes(self, path: deque):
        self.nodes = path

    def set_cost(self, cost: int):
        self.cost = cost

    def __ge__(self, other):
        return self.cost >= other.cost

    def __repr__(self):
        return f"Flight(id={self.id}, origen={self.origin}, destino={self.destination})"
