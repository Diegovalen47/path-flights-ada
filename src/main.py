from User import User, load_users, Sex, GenderPreference, Location
from ClosestPair import find_closest_compatible_users

load_users()

compatible_users: tuple[float, tuple[User, User]] = find_closest_compatible_users(list(User.users.values()))

print("La pareja de usuarios mas cercana es:")
print(f"{compatible_users[1][0]}")
print("y")
print(f"{compatible_users[1][1]}")
print(f"con una distancia de {round(compatible_users[0], 4)}")
