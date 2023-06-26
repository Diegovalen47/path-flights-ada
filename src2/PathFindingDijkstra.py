import heapq
from math import inf
from DataGenerator import create_world_path, random_flights_generator, formatted_graph, formatted_flights, save_data
from Graph import Graph
from Flight import Flight
from Node import Node
from collections import deque
from FlightNode import FlightNode
from geopy import distance


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
    return path_flight, graphSPD[node_destination]

def closest_pair_divide_and_conquer(fligth_nodes: list[FlightNode]) -> tuple[float, int, int]:
    """
    Find the minumum distance between two nodes and return their ids
    :return minimum distance, node id, node id
    """
    fligth_nodes.sort(key=lambda node: node.latitude)
    return closest_pair(0, len(fligth_nodes) - 1, fligth_nodes)

def closest_pair(i: int, j: int, flight_nodes: list[FlightNode]) -> tuple[float, int, int]:
    """
    Encuentra la pareja de usuarios mas cercana compatible entre los usuarios
    :param i: indice i de la iteracion
    :param j: indice j de la iteracion
    :param fligth_nodes: Flight node list
    :return: minimum distance, node id, node id
    """

    if i == j:
        return float("inf"), flight_nodes[i].flight_id, flight_nodes[j].flight_id
    elif j - i != 1:
        d_l: tuple = closest_pair(i, (i + j) // 2, flight_nodes)
        d_r: tuple = closest_pair(1 + ((i + j) // 2), j, flight_nodes)
        delta: tuple = d_l if d_l[0] <= d_r[0] else d_r
        d_s: tuple = closest_split_pair(i, j, delta, flight_nodes)
        return d_s
    elif j - i == 1 and flight_nodes[i].flight_id != flight_nodes[j].flight_id:
        return distance.geodesic((flight_nodes[i].latitude, flight_nodes[i].longitude), (flight_nodes[j].latitude, flight_nodes[j].longitude)).km, flight_nodes[i].flight_id, flight_nodes[j].flight_id
    else:
        return float("inf"), flight_nodes[i].flight_id, flight_nodes[j].flight_id

def closest_split_pair(i: int, j: int, delta: tuple, flight_nodes: list[FlightNode]) -> tuple[float, int, int]:

    xp = flight_nodes[(i + j) // 2].latitude
    s = [flight_node for flight_node in flight_nodes[i:j + 1] if xp - delta[0] <= flight_node.latitude <= xp + delta[0]]
    s.sort(key=lambda node: node.longitude)
    min_d:float = delta[0]
    winners: tuple[int, int] = (delta[1], delta[2])
    for k in range(len(s)):
        for l in range(k + 1, min(k + 8, len(s))):
            p, q = s[k], s[l]
            if q.longitude - p.longitude >= min_d:
                break
            dist = distance.geodesic((p.latitude, p.longitude), (q.latitude, q.longitude)).km
            if dist < min_d and p.flight_id != q.flight_id:
                winners = (p.flight_id, q.flight_id)
                min_d = dist
    return min_d, winners[0], winners[-1]

def delete_path_flight(flight: Flight):

    for _ in range(len(flight.nodes)):
        Node.nodes[flight.nodes.pop()].delete_flight(flight)

if __name__ == '__main__':

    generate_data(10)
    for flight in Flight.flights.values():
        temp_path, cost = find_path_flight(flight.origin, flight.destination)
        flight.set_nodes(temp_path.copy())
        flight.set_cost(cost)
        for _ in range(len(temp_path)):
            Node.nodes[temp_path.popleft()].add_flight(flight)

    for node in Node.nodes.values():
        print(f'Node: {node.id}')
        print(node.get_flights())

    dist: float = 0
    cont: int = 0

    while True:
        dist, f1, f2 = closest_pair_divide_and_conquer(FlightNode.flight_nodes_factory(Node.nodes))

        if dist <= 1:
            print(dist, f1, f2)
            flight_1: Flight = Flight.flights[f1]
            flight_2: Flight = Flight.flights[f2]

            if flight_1 >= flight_2:
                delete_path_flight(flight_1)
            else:
                delete_path_flight(flight_2)

        else:
            print("Esta tupla ta bien ", end=' ')
            print(dist, f1, f2)
            break




