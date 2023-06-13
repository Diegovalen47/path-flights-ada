from User import User, load_users, Sex, GenderPreference, Location
from ClosestPair import find_closest_compatible_users, compatibles

load_users()

compatible_users = find_closest_compatible_users(list(User.users.values()))

print(compatible_users)