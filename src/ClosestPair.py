from math import dist
from User import User, compatibles


def find_closest_compatible_users(users: list[User]) -> tuple[float, tuple[User, User]]:
    users.sort(key=lambda x: x.location.latitude)
    return closest_pair(0, len(users) - 1, users)


def closest_pair(i: int, j: int, users: list[User]) -> tuple[float, tuple[User, User]]:
    """
    Encuentra la pareja de usuarios mas cercana compatible entre los usuarios
    :param i: indice i de la iteracion
    :param j: indice j de la iteracion
    :param users: lista de usuarios
    :return: distancia minima y pareja de usuarios
    """

    # un usuario
    if i == j:
        return float("inf"), (users[i], users[j])
    elif j - i != 1:
        d_l: tuple[float, tuple[User, User]] = closest_pair(i, (i + j) // 2, users)
        d_r: tuple[float, tuple[User, User]] = closest_pair(1 + ((i + j) // 2), j, users)
        delta: tuple[float, tuple[User, User]] = d_l if d_l[0] <= d_r[0] else d_r
        d_s: tuple[float, tuple[User, User]] = closest_split_pair(i, j, delta, users)
        return d_s
    # dos usuarios
    elif j - i == 1 and compatibles(users[i], users[j]):
        return dist(users[i].location.to_tuple(), users[j].location.to_tuple()), (users[i], users[j])
    else:
        return float("inf"), (users[i], users[j])


def closest_split_pair(i: int, j: int, delta: tuple[float, tuple[User, User]], users: list[User]) -> tuple[float, tuple[User, User]]:
    """
    Funcion que hace parte del algorimo de closest pair, cuando
    la pareja de usuarios mas cercana se encuentran en mitades diferentes
    :param i: indice i de la iteracion
    :param j: indice j de la iteracion
    :param delta: distancia minima y pareja de usuarios
    :param users: lista de usuarios
    :return: distancia minima y pareja de usuarios del split pair
    """

    xp = users[(i + j) // 2].location.latitude
    s = [user for user in users[i:j + 1] if xp - delta[0] <= user.location.latitude <= xp + delta[0]]
    s.sort(key=lambda x: x.location.longitude)
    min_d = delta[0]
    winners = delta[1]
    for k in range(len(s)):
        for l in range(k + 1, min(k + 8, len(s))):
            p, q = s[k], s[l]
            if q.location.longitude - p.location.longitude >= min_d:
                break
            distance = dist(p.location.to_tuple(), q.location.to_tuple())
            if distance < min_d and compatibles(p, q):
                winners = (p, q)
                min_d = distance
    return min_d, winners
