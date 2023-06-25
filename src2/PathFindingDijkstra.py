import heapq
from math import inf
from DataGenerator import create_world_path, random_flights_generator, formatted_graph, formatted_flights, save_data
from Graph import Graph
from Flight import Flight
from Node import Node
from collections import deque


def generate_data(n: int):
    create_world_path(n)
    print(f'Graph: {Graph.graph}')
    random_flights_generator()
    print(f'Flights: {Flight.flights}')
    save_data(formatted_graph(), "graph.json")
    save_data(formatted_flights(), "flights.json")


def find_path_flight(node_origin: int, node_destination: int):
    path_flight = deque([])
    NO_PARENT = -1

    graphSPD: dict = dict([(i, inf) for i in range(Node.nodes_quantity)])
    graphSPD[node_origin] = 0
    parents = [-1] * Node.nodes_quantity

    # Start Dijkstra
    queue: list = []
    heapq.heappush(queue, (0, node_origin))  # (SPD, node)
    while len(queue) > 0:
        spdU, u = heapq.heappop(queue)
        for v, d in Graph.graph[u].items():
            if spdU + d < graphSPD[v]:
                graphSPD[v] = spdU + d
                heapq.heappush(queue, (graphSPD[v], v))
                parents[v] = u

    def print_path(current_vertex, parents_data):
        # Base case : Source node has
        # been processed
        if current_vertex == NO_PARENT:
            return
        print_path(parents_data[current_vertex], parents_data)
        path_flight.append(current_vertex)

    print_path(node_destination, parents)
    return path_flight, graphSPD[node_origin][node_destination]


if __name__ == '__main__':

    generate_data(10)
    for flight in Flight.flights.values():
        temp_path, cost = find_path_flight(flight.origin, flight.destination)
        flight.set_nodes(temp_path)
        flight.set_cost(cost)
        for _ in range(len(temp_path)):
            Node.nodes[temp_path.popleft()].add_flight(flight)

    for node in Node.nodes.values():
        print(f'Node: {node.id}')
        print(node.get_flights())
