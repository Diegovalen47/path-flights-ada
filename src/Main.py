from DataGenerator import load_graph_and_nodes, load_flights
from PathFindingDijkstra import set_path_found
from Flight import Flight, delete_path_flight
from FlightNode import FlightNode
from Node import Node
from ClosestDivideAndConquer import closest_pair_divide_and_conquer
from ClosestBruteForce import closest_pair_brute_force
from time import time
from Graph import Graph

iterations = 0


def iterative_closest_pair_finding(algorithm):
    print(" ")
    print("Buscando riesgo de colision de vuelos...")
    print(f"  (distancia, id_vuelo_1, id_vuelo_2)")
    global iterations
    while True:
        dist, f1, f2 = algorithm(FlightNode.flight_nodes_factory(Node.nodes))
        iterations += 1

        if dist <= 10:
            print(f"  ({round(dist, 4)} Km, {f1}, {f2})", end=' ')
            flight_1: Flight = Flight.flights[f1]
            flight_2: Flight = Flight.flights[f2]

            if flight_1 >= flight_2:
                print(f"Eliminando vuelo {flight_1.id} al ser mas costoso que {flight_2.id}")
                delete_path_flight(flight_1)
            else:
                delete_path_flight(flight_2)
                print(f"Eliminando vuelo {flight_2.id} al ser mas costoso que {flight_1.id}")

        else:
            print("Distancia segura: (Mayor a 10 Km)", end=' ')
            print(f"({round(dist, 4)} Km, {f1}, {f2}) No se eliminan mas vuelos")
            print(" ")
            break


def print_time_results(len_nodes, len_flights, iterations, elapsed_time):
    vuelos = list(Flight.flights.keys())
    cant_vuelos = len(vuelos)
    print(f"  Cantidad de Nodos:                {len_nodes}")
    print(f"  Cantidad de Vuelos:               {len_flights}")
    print(f"  Iteraciones Pares mas cercanos:   {iterations}")
    print(f"  Tiempo de ejecucion:              {round(elapsed_time, 5)} segundos")
    print(f"  Vuelos que pueden hacerse:        ({cant_vuelos}) {vuelos}")


if __name__ == '__main__':

    # Se cargan los datos de del grafo y los vuelos
    # construyendo estos en sus respectivas
    # estructuras de datos
    load_graph_and_nodes()
    load_flights()
    print(Graph.graph)

    print("Seleccione con que metodo desea ejecutar el algoritmo")
    print("1. Fuerza bruta")
    print("2. Divide y venceras")
    option = int(input())
    print(" ")

    # Eligir con que algorimo se ejecutara el programa
    start_time = time()
    set_path_found()
    if option == 1:
        iterative_closest_pair_finding(closest_pair_brute_force)
        end_time = time()
        elapsed_time = end_time - start_time
        print(f"Utilizando FUERZA BRUTA: ")
        print_time_results(len(Node.nodes), Flight.flights_quantity, iterations, elapsed_time)
    elif option == 2:
        iterative_closest_pair_finding(closest_pair_divide_and_conquer)
        end_time = time()
        elapsed_time = end_time - start_time
        print(f"Utilizando DIVIDE Y VENCERÁS: ")
        print_time_results(len(Node.nodes), Flight.flights_quantity, iterations, elapsed_time)
