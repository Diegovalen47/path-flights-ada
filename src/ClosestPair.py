from math import dist
from User import User


def closest_pair(i, j, puntos):
    if i == j:
        return float("inf")
    elif j-i != 1:
        dL = closest_pair(i, (i + j) // 2, puntos)
        dR = closest_pair(1 + ((i + j) // 2), j, puntos)
        delta = min(dL, dR)
        dS = closest_split_pair(i, j, delta, puntos)
        return dS
    elif j-1 == 1 and puntos[i][1] != puntos[j][1]:
        return dist(puntos[i][0], puntos[j][0])
    else:
        return float("inf")


def closest_split_pair(i, j, delta, puntos):
    xp = puntos[(i+j)//2][0][0]
    S = [p for p in puntos[i:j+1] if xp - delta <= p[0][0] <= xp + delta]
    S.sort(key=lambda x: x[0][1])
    minD = delta
    for k in range(len(S)):
        for l in range(k+1, min(k+8, len(S))):
            p, q = S[k], S[l]
            if q[0][1] - p[0][1] >= minD:
                break
            distance = dist(p[0], q[0])
            if distance < minD and p[1] != q[1]:
                minD = distance
    return minD


def find_closest_compatible_users(users: list[User]):
    users.sort(key=lambda x: x.location.latitude)
    distance = closest_pair(0, len(users) - 1, users)
