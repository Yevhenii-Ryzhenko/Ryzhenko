database_users = [
  {"id": 1, "name": "John", "second_name": "Doe", "age": 30},
  {"id": 2, "name": "Jane", "second_name": "Joi", "age": 25}
]
user_input = [
  {"id": 1, "name": "John", "second_name": "Doe", "age": 30},
  {"id": 2, "name": "Jane", "second_name": "Joi", "age": 15}
]


def access_level(user):
    for db_user in database_users:
        if db_user['id'] == user['id']:
            user_level = 1
            if db_user['name'] == user['name']:
                user_level += 1
            if db_user['second_name'] == user['second_name']:
                user_level += 1
            if db_user['age'] == user['age']:
                user_level += 1
            if user_level == 4:
                return "full"
            elif user_level == 3:
                return "read-only"
            else:
                return "forbiden"
    return "forbiden"

user = user_input()
print(access_level(user))