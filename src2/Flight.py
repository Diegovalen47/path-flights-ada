from collections import deque
from Node import Node


class Flight:
    flights: dict = {}
    flights_quantity: int = 0

    def __init__(self, id: int, origin: int, destination: int):
        self.id: int = id
        self.origin: int = origin
        self.destination: int = destination
        self.nodes: deque = deque([])
        self.cost: int = 0
        Flight.flights[id] = self
        Flight.flights_quantity += 1

    def set_nodes(self, path: deque):
        self.nodes = path

    def set_cost(self, cost: int):
        self.cost = cost

    def __ge__(self, other):
        if self.cost == other.cost:
            return other.id >= self.id
        return self.cost >= other.cost

    def __repr__(self):
        return f"Flight(id={self.id}, origen={self.origin}, destino={self.destination})"


def delete_path_flight(flight: Flight):
    deleted = set()
    for _ in range(len(flight.nodes)):
        ide = flight.id
        if ide not in deleted:
            Flight.flights.pop(ide)
            deleted.add(ide)
        Node.nodes[flight.nodes.pop()].delete_flight(flight)
