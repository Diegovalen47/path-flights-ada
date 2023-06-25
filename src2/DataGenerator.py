import networkx as nx
from itertools import combinations, groupby
from random import SystemRandom, random, choice, sample
from Node import Node
from Edge import Edge
from Graph import Graph
from Flight import Flight
from math import ceil
import json


def random_world_path_generator(n, p):
    edges = combinations(range(n), 2)
    G = nx.Graph()
    G.add_nodes_from(range(n))
    if p <= 0:
        return G
    if p >= 1:
        return nx.complete_graph(n, create_using=G)
    for _, node_edges in groupby(edges, key=lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if random() < p:
                G.add_edge(*e)

    for (start, end) in G.edges:
        G.edges[start, end]['weight'] = random()

    return G

def create_world_path(nodes_quantity):
    random_graph = random_world_path_generator(nodes_quantity, 0.1)

    for node in random_graph.nodes:
        Node(node, SystemRandom().uniform(-90, 90), SystemRandom().uniform(-180, 180))

    for start, end, weight in random_graph.edges.data('weight'):
        Edge(start, end, weight)

    Graph.create_graph()

def random_flights_generator():
    flights_number: int = ceil(SystemRandom().uniform(0.15, 0.2)*Node.nodes_quantity)

    for id in range(flights_number):
        origin, destination = sample(range(Node.nodes_quantity), 2)
        Flight(id, origin, destination)


def formatted_graph():
    nodes: list = []
    for i in range(Node.nodes_quantity):
        formatted_node = {
            "id": i,
            "lat": Node.nodes[i].latitude,
            "lon": Node.nodes[i].longitude,
            "edges": [{ "end": j, "weight": Graph.graph[i][j]} for j in Graph.graph[i].keys()]
        }
        nodes.append(formatted_node)

    return nodes

def formatted_flights():
    flights: list = []
    for flight in Flight.flights.values():
        formatted_flight = {
            "id": flight.id,
            "origin": flight.origin,
            "destination": flight.destination
        }
        flights.append(formatted_flight)

    return flights

def save_data(formatted_data: list, file_name: str):
    print("Saving data...")
    json_string = json.dumps(formatted_data)
    json_file = open(file_name, "w")
    json_file.write(json_string)
    json_file.close()
    print(f"Data saved in {file_name}")

