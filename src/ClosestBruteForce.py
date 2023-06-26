from FlightNode import FlightNode
from geopy import distance


def closest_pair_brute_force(flight_nodes: list[FlightNode]) -> tuple[float, int, int]:
    """
    Find the minumum distance between two nodes and return their ids
    using brute force
    :return minimum distance, node id, node id
    """

    min_distance = float("inf")
    closest_pair = (flight_nodes[0].flight_id, flight_nodes[0].flight_id)
    for i in range(len(flight_nodes)):
        for j in range(i + 1, len(flight_nodes)):
            dist = distance.geodesic((flight_nodes[i].latitude, flight_nodes[i].longitude), (flight_nodes[j].latitude, flight_nodes[j].longitude)).km
            if dist < min_distance and flight_nodes[i].flight_id != flight_nodes[j].flight_id:
                min_distance = dist
                closest_pair = (flight_nodes[i].flight_id, flight_nodes[j].flight_id)
    return min_distance, closest_pair[0], closest_pair[1]
