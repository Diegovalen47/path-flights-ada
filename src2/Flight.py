from collections import deque


class Flight:
    flights: dict = {}
    nodes: deque = deque([])
    cost: int = 0

    def __init__(self, id: int, origin: int, destination: int):
        self.id: int = id
        self.origin: int = origin
        self.destination: int = destination
        Flight.flights[id] = self

    def set_nodes(self, path: deque):
        self.nodes = path

    def set_cost(self, cost: int):
        self.cost = cost

    def __repr__(self):
        return f"Flight(id={self.id}, origen={self.origin}, destino={self.destination})"
