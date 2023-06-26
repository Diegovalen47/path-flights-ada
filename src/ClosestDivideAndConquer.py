from FlightNode import FlightNode
from geopy import distance


def closest_pair_divide_and_conquer(fligth_nodes: list[FlightNode]) -> tuple[float, int, int]:
    """
    Find the minumum distance between two nodes and return their ids
    using divide and conquer closest pair technique
    :return minimum distance, node id, node id
    """
    fligth_nodes.sort(key=lambda node: node.latitude)
    return closest_pair(0, len(fligth_nodes) - 1, fligth_nodes)


def closest_pair(i: int, j: int, flight_nodes: list[FlightNode]) -> tuple[float, int, int]:
    """
    Encuentra la pareja de usuarios mas cercana compatible entre los usuarios
    :param i: indice i de la iteracion
    :param j: indice j de la iteracion
    :param flight_nodes: Flight node list
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
    min_d: float = delta[0]
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
