from enum import Enum
import json


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


class User:
    users: dict = {}

    def __init__(self, id: int, sex: Sex, gender_preference: GenderPreference, location: Location):
        self.id: int = id
        self.sex: Sex = sex
        self.gender_preference: GenderPreference = gender_preference
        self.location: Location = location
        User.users[id] = self

    def __repr__(self):
        return f"User({self.id}, " \
               f"sex={self.sex.name}, " \
               f"gender_preference={self.gender_preference.name}, " \
               f"location={self.location})"


def load_users():
    # utilizar esta pagina para generar usuarios aleatorios
    # https://www.mockaroo.com/
    f = open('user_list.json')

    data = json.load(f)

    for user in data:
        User(
            user['id'],
            Sex(user['sex']),
            GenderPreference(user['gender_preference']),
            Location(user['location']['latitude'], user['location']['longitude'])
        )

    f.close()
