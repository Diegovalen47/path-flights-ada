import json
from enum import Enum
from random import random, SystemRandom


class Sex(Enum):
    MASCULINO = 'M'
    FEMENINO = 'F'


class GenderPreference(Enum):
    MASCULINO = 'M'
    FEMENINO = 'F'
    AMBOS = 'A'


class Location:
    def __init__(self, latitude: float, longitude: float):
        self.latitude: float = latitude
        self.longitude: float = longitude

    def __repr__(self):
        return f"Location(latitude={self.latitude}, longitude={self.longitude})"

    def to_tuple(self):
        return self.latitude, self.longitude


def get_random_sex():
    number = random()
    if number < 0.5:
        return Sex.FEMENINO
    else:
        return Sex.MASCULINO


def get_random_genre_preference():
    number = random()
    if number < 0.33:
        return GenderPreference.MASCULINO
    elif number < 0.66:
        return GenderPreference.FEMENINO
    else:
        return GenderPreference.AMBOS


def get_random_location():
    return Location(SystemRandom().uniform(-230000, 230000), SystemRandom().uniform(-230000, 230000))


class User:

    users: list = []

    def __init__(self, id: int, sex: Sex, gender_preference: GenderPreference, location: Location):
        self.id: int = id
        self.sex: Sex = sex
        self.gender_preference: GenderPreference = gender_preference
        self.location: Location = location

    def __repr__(self):
        return f"User({self.id}, " \
               f"sex={self.sex.name}, " \
               f"gender_preference={self.gender_preference.name}, " \
               f"location={self.location})"


def load_users():
    print("Cargando usuarios desde el json...")
    f = open('users_list.json')

    data = json.load(f)

    for user in data:
        usuario = User(
            user['id'],
            Sex(user['sex']),
            GenderPreference(user['gender_preference']),
            Location(user['location']['latitude'], user['location']['longitude'])
        )

        User.users.append(usuario)

    print(f"{len(data)} usuarios cargados desde el json")
    f.close()
