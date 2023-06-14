from User import User, get_random_location, get_random_genre_preference, get_random_sex
import json
import time


def save_users(quantity):
    print("Creando usuarios aleatorios...")
    users = create_random_users(quantity)
    json_string = json.dumps(users)
    json_file = open("users_list.json", "w")
    json_file.write(json_string)
    json_file.close()
    print(f"{quantity} usuarios creados y guardados en users_list.json")


def create_random_users(quantity):
    users = []
    for i in range(quantity):
        user = User(i, get_random_sex(), get_random_genre_preference(), get_random_location())
        formatted_user = {
            "id": user.id,
            "sex": user.sex.value,
            "gender_preference": user.gender_preference.value,
            "location": {
                "latitude": user.location.latitude,
                "longitude": user.location.longitude
            }
        }
        users.append(formatted_user)
    return users


# Al generar muestras de usuarios, colocar la cantidad que se desea
# en el parametro de la funcion save_users
st = time.time()
save_users(5000)
et = time.time()

elapsed_time = et - st

print(f"Tiempo transcurrido: {elapsed_time} segundos")
