from User import User, load_users
from ClosestPair import find_closest_compatible_users
import time


load_users()

# get the start time
st = time.time()
compatible_users: tuple[float, tuple[User, User]] = find_closest_compatible_users(User.users)
# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st

print("La pareja de usuarios compatible mas cercana es:")
print(f"  {compatible_users[1][0]}")
print(f"  {compatible_users[1][1]}")
print(f"Con una distancia minima de {round(compatible_users[0], 4)}")
print(f"Con un tiempo de ejecución de: {elapsed_time} segundos")
print("Utilizando el algoritmo de pares mas cercanos")
