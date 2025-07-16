"""
Службовий файл для створення рандомної інформації про студентів
"""
from faker import Faker
import random
from models import Students

f = Faker()

def create_students(num=20):
    list_of_students = []
    for s in range(num):  # скільки студентів хочеш створити
        student = Students(
            first_name=f.first_name(),
            last_name=f.last_name(),
            age=random.choice(range(18,66))
    )
        list_of_students.append(student)
    return list_of_students