import networkx as nx
from itertools import combinations, groupby
from random import SystemRandom, random, choice, sample
from Edge import Edge
from Graph import Graph
from Flight import Flight
from math import ceil
import json
import matplotlib.pyplot as plt

# Rango peso de las aristas
WEIGHT_MAX = 20
# Probabilidad de que exista una arista entre dos nodos
PROBABILITY = 0.1
# Rango de latitudes y longitudes de colombia
LATITUDES = (4, 13)
LONGITUDES = (66, 79)
# Proporcion de vuelos respecto a la cantidad de nodos
FLIGHTS_PROPORTION = (0.2, 0.3)


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
        G.edges[start, end]['weight'] = SystemRandom().uniform(0.15, 1)*WEIGHT_MAX
    nx.draw(G, with_labels=True)
    plt.show()
    return G


def create_world_path(nodes_quantity):
    from Node import Node

    random_graph = random_world_path_generator(nodes_quantity, PROBABILITY)

    for node in random_graph.nodes:
        # Latitudes y longitudes posibles, respecto a los limites de colombia
        Node(node, SystemRandom().uniform(LATITUDES[0], LATITUDES[1]), SystemRandom().uniform(LONGITUDES[0], LONGITUDES[1]))

    for start, end, weight in random_graph.edges.data('weight'):
        Edge(start, end, weight)

    Graph.create_graph()


def random_flights_generator():
    from Node import Node

    flights_number: int = ceil(SystemRandom().uniform(FLIGHTS_PROPORTION[0], FLIGHTS_PROPORTION[1]) * Node.nodes_quantity)

    for id in range(flights_number):
        origin, destination = sample(range(Node.nodes_quantity), 2)
        Flight(id, origin, destination)


def formatted_graph():
    from Node import Node

    nodes: list = []
    for i in range(Node.nodes_quantity):
        formatted_node = {
            "id": i,
            "lat": Node.nodes[i].latitude,
            "lon": Node.nodes[i].longitude,
            "edges": [{"end": j, "weight": Graph.graph[i][j]} for j in Graph.graph[i].keys()]
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


def generate_data(n: int):
    create_world_path(n)
    random_flights_generator()
    save_data(formatted_graph(), "graph.json")
    save_data(formatted_flights(), "flights.json")


def save_data(formatted_data: list, file_name: str):
    print("Saving data...")
    json_string = json.dumps(formatted_data)
    json_file = open(file_name, "w")
    json_file.write(json_string)
    json_file.close()
    print(f"Data saved in {file_name}")


def load_graph_and_nodes():
    from Node import Node

    print("Cargando datos del grafo desde el json...")
    f = open("graph.json", "r")

    data = json.load(f)
    aux_graph = {i: {} for i in range(len(data))}
    for node in data:
        Node(node["id"], node["lat"], node["lon"])
        for edge in node["edges"]:
            aux_graph[node["id"]][edge["end"]] = edge["weight"]
    Graph.graph = aux_graph

    print("Grafo cargado desde el json")
    f.close()


def load_flights():
    print("Cargando datos de los vuelos desde el json...")
    f = open("flights.json", "r")

    data = json.load(f)
    for flight in data:
        Flight(flight["id"], flight["origin"], flight["destination"])

    print("Vuelos cargados desde el json")
    f.close()


if __name__ == '__main__':
    # En una pagina que muestra los vuelos en tiempo real
    # se tomaron muestran de cuantos vuelos hay en un momento determinado
    # transitando colombia, y se promedio el dato
    generate_data(15)
