from User import User, load_users
from ClosestPair import find_closest_compatible_users
from BruteForcePair import closest_pairs
import time


load_users()

# get the start time
st = time.time()
compatible_users_split_pair: tuple[float, tuple[User, User]] = find_closest_compatible_users(User.users)
# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st

print("")
print("Utilizando el algoritmo DIVIDE Y VENCERAS")
print("La pareja de usuarios compatible mas cercana es:")
print(f"  {compatible_users_split_pair[1][0]}")
print(f"  {compatible_users_split_pair[1][1]}")
print(f"Con una distancia minima de {round(compatible_users_split_pair[0], 4)}")
print(f"Con un tiempo de ejecución de: {elapsed_time} segundos")

# get the start time
st_brute = time.time()
compatible_users_brute_force: tuple[float, tuple[User, User]] = closest_pairs(User.users)
# get the end time
et_brute = time.time()

# get the execution time
elapsed_time_brute = et_brute - st_brute

print("")
print("Utilizando el algoritmo por FUERZA BRUTA")
print("La pareja de usuarios compatible mas cercana es:")
print(f"  {compatible_users_brute_force[1][0]}")
print(f"  {compatible_users_brute_force[1][1]}")
print(f"Con una distancia minima de {round(compatible_users_brute_force[0], 4)}")
print(f"Con un tiempo de ejecución de: {elapsed_time_brute} segundos")
