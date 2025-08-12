from faker import Faker
import random

f = Faker()

class Creds:

    login = "guest"
    password= "welcome2qauto"

class CrateRandomData:

    name = f.first_name()
    last_name = f.last_name()
    email = f.email()
    password = f.password(length=random.randint(8,15), special_chars=True, upper_case=True, lower_case=True)
    repeat_password = password

