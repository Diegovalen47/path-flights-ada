from DataGenerator import create_world_path, random_flights_generator, formatted_graph, formatted_flights, save_data
from Graph import Graph
from Flight import Flight
from Node import Node

n = 30
create_world_path(n)
print(f'Graph: {Graph.graph}')
random_flights_generator()
print(f'Flights: {Flight.flights}')
save_data(formatted_graph(), "graph.json")
save_data(formatted_flights(), "flights.json")

print(Node.nodes_quantity)

