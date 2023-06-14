from User import User, compatibles
from math import dist


def closest_pair_brute_force(users: list[User]) -> tuple[float, tuple[User, User]]:
    """
    Devuelve la pareja de usuarios mas cercana y la distancia entre ellos
    :param users: lista de usuarios
    :return: tupla con la distancia y la pareja de usuarios mas cercana
    """

    min_distance = float("inf")
    closest_pair = (None, None)
    for i in range(len(users)):
        for j in range(i + 1, len(users)):
            distance = dist(users[i].location.to_tuple(), users[j].location.to_tuple())
            if distance < min_distance and compatibles(users[i], users[j]):
                min_distance = distance
                closest_pair = (users[i], users[j])
    return min_distance, closest_pair
