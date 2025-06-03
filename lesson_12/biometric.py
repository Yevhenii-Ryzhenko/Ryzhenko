"""
Біометрична авторизація. Функція виконує авторизацію на підставі отриманого списка словників даних та словника, отриманого з іншої функції від користувача.
    Параметри користувача: id - int, name - str, second_name - str, age - int
    Якщо дані від користувача співпадають з єталонними даними - користувач отримує повний доступ. Якщо відрізняється одне поле - доступ read-only, якщо більше - доступ заборонено.
    Функція повертає рівень доступу: full, read-only, forbiden
# варіант вхідних значень
database_users = [
  {"id": 1, "name": "John", "second_name": "Doe", "age": 30}
  {"id": 2, "name": "Jane", "second_name": "Joi", "age": 25}
]
# варіанти user_input :
{"id": 1, "name": "John", "second_name": "Doe", "age": 30}
{"id": 1, "name": "John", "second_name": "Joi", "age": 30}
{"id": 1, "name": "John", "second_name": "Joi", "age": 25}
"""
database_users = [
  {"id": 1, "name": "John", "second_name": "Doe", "age": 30},
  {"id": 2, "name": "Jane", "second_name": "Joi", "age": 26}
]


# def user_input():
#     return {
#     'id': int(input("Enter your ID:")),
#     'name': str(input("Enter your name:")),
#     'second_name': str(input("Enter your second_name:")),
#     'age': int(input("Enter your age:"))
# }


def access_level(user):
# Спочатку додається перевірка, що user надав id
    if "id" not in user:
        return "User is not found"
# Додається перевірка, що user надав усі необхідні дані (name, second_name, age)
    if ("name" not in user or "second_name" not in user or "age" not in user):
        return "You provided insufficient data"
    max_level = 0
    for db_user in database_users:
        if db_user['id'] == user['id']:
            user_level = 1
            if db_user['name'] == user['name']:
                user_level += 1
            if db_user['second_name'] == user['second_name']:
                user_level += 1
            if db_user['age'] == user['age']:
                user_level += 1
            max_level = max (max_level, user_level)
    if max_level == 4:
        return "full"
    elif max_level == 3:
        return "read-only"
    else:
        return "forbiden"

# Необхідно перевірити, що усі id у db_user - унікальні
# У іншому випадку - необхідно виправити database_users перш ніж визначати рівень доступу
def database_users_check(user):
    id_list = [db_user['id'] for db_user in database_users]
    if len(id_list) != len(set(id_list)):
        return "ERROR! Check your database_users. You have repeated id"
    return access_level(user)

user = {"id": 2, "name": "Jane", "second_name": "Joi", "age": 25}

print(database_users_check(user))