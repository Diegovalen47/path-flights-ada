from User import User, load_users
from DivideAndConquerPair import closest_pair_divide_and_conquer
from BruteForcePair import closest_pair_brute_force
import time


load_users()

# get the start time
st = time.time()
result_divide_and_conquer: tuple[float, tuple[User, User]] = closest_pair_divide_and_conquer(User.users)
# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st

print("")
print("Utilizando el algoritmo DIVIDE Y VENCERAS")
print("La pareja de usuarios compatible mas cercana es:")
print(f"  {result_divide_and_conquer[1][0]}")
print(f"  {result_divide_and_conquer[1][1]}")
print(f"Con una distancia minima de {round(result_divide_and_conquer[0], 4)}")
print(f"Con un tiempo de ejecución de: {elapsed_time} segundos")

# get the start time
st_brute = time.time()
result_brute_force: tuple[float, tuple[User, User]] = closest_pair_brute_force(User.users)
# get the end time
et_brute = time.time()

# get the execution time
elapsed_time_brute = et_brute - st_brute

print("")
print("Utilizando el algoritmo por FUERZA BRUTA")
print("La pareja de usuarios compatible mas cercana es:")
print(f"  {result_brute_force[1][0]}")
print(f"  {result_brute_force[1][1]}")
print(f"Con una distancia minima de {round(result_brute_force[0], 4)}")
print(f"Con un tiempo de ejecución de: {elapsed_time_brute} segundos")
