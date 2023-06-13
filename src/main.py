from User import User, load_users

load_users()

print(list(User.users.values()))
