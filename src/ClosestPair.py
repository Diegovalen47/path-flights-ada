from math import dist
from User import User, Sex, GenderPreference


def compatibles(user1: User, user2: User) -> bool:
    """
    Determina si dos usuarios son compatibles teniendo en cuenta
    su sexo y preferencia de genero
    """

    # Si user1 es bisexual pero el usuario2 no
    if user1.gender_preference.name == GenderPreference.AMBOS.name and user2.gender_preference.name != GenderPreference.AMBOS.name:
        # y la preferencia del user2 es diferente al sexo del user1, no son compatibles
        if user2.gender_preference.name != user1.sex.name:
            return False
    # Si user2 es bisexual pero el user1 no
    if user2.gender_preference.name == GenderPreference.AMBOS.name and user1.gender_preference.name != GenderPreference.AMBOS.name:
        # y la preferencia del user1 es diferente al sexo del user2, no son compatibles
        if user1.gender_preference.name != user2.sex.name:
            return False
    # Si a ambos les gusta solo un sexo
    if user1.gender_preference.name != GenderPreference.AMBOS.name and user2.gender_preference.name != GenderPreference.AMBOS.name:
        # y la preferencia del user1 es diferente al sexo del user2, no son compatibles
        if user1.gender_preference.name != user2.sex.name:
            return False
        # y la preferencia del user2 es diferente al sexo del user1, no son compatibles
        if user2.gender_preference.name != user1.sex.name:
            return False
    return True


def closest_pair(i: int, j: int, users: list[User]):
    # un usuario
    if i == j:
        return float("inf"), (users[i], users[j])
    elif j - i != 1:
        dL = closest_pair(i, (i + j) // 2, users)
        dR = closest_pair(1 + ((i + j) // 2), j, users)
        delta = dL if dL[0] <= dR[0] else dR
        dS = closest_split_pair(i, j, delta, users)
        return dS
    # dos usuarios
    elif j - i == 1 and compatibles(users[i], users[j]):
        return dist(users[i].location.to_tuple(), users[j].location.to_tuple()), (users[i], users[j])
    else:
        return float("inf"), (users[i], users[j])


def closest_split_pair(i, j, delta, users):
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


def find_closest_compatible_users(users: list[User]):
    users.sort(key=lambda x: x.location.latitude)
    distance = closest_pair(0, len(users) - 1, users)
    return distance
