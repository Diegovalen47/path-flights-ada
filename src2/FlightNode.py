from Node import Node

class FlightNode:

    def __init__(self, id: int, flight_id: int, latitude: float, longitude: float):
        self.id: int = id
        self.flight_id: int = flight_id
        self.latitude: float = latitude
        self.longitude: float = longitude

    @staticmethod
    def flight_nodes_factory(nodes: dict[Node]):
        flight_nodes: list = []
        for node in nodes.values():
            for flight in node.flights.keys():
                flight_nodes.append(FlightNode(node.id, flight, node.latitude, node.longitude))

        return flight_nodes


