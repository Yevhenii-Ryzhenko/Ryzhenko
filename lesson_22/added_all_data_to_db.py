"""
Даний код написаний для додвання перших 20-ти студентів з рандомними даними і 5 курсів у БД
"""
from sqlalchemy import Column, Integer, String, create_engine, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from models import Base, Students, Courses
from create_random_data import create_students
import random
from faker import Faker

f = Faker()

engine = create_engine('sqlite:///students_and_courses.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

list_of_courses = ["Maths", "Literature", "Poetry", "Physics", "Chemistry", "Biology"]

for course_name in list_of_courses:
    exists = session.query(Courses).filter_by(course_name=course_name).first()
    if not exists:
        new_course = Courses(
            course_name=course_name,
            course_duration=random.randint(1, 24),
            diploma=random.choice([True, False])
        )
        session.add(new_course)

session.commit()

courses_from_db = session.query(Courses).all()

list_of_students = create_students(20)

for student in list_of_students:
    student.courses = random.sample(courses_from_db, k=random.randint(1, 5))
    session.add(student)

session.commit()
session.close()