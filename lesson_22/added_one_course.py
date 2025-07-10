"""
Тут можна створити новий курс
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Students, Courses

engine = create_engine('sqlite:///students_and_courses.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

"""
Додавання курсу з вказанням даних. Необхідно ввести довільну назву курсу, його тривалість у місяцях та заповнити
поле new_diploma True або False залежно від видачі диплому по закінченню курсу
"""

new_course_name = "History"
new_course_duration = 20
new_diploma = False

existing_course = session.query(Courses).filter_by(course_name=new_course_name).first()

added_course = Courses(course_name=new_course_name, course_duration=new_course_duration, diploma=new_diploma)
if existing_course:
    print(f'Курс з назвою {added_course.course_name} вже додано. Його ID: {existing_course.id}\n'
          f'Додавання нового курсу перервано')
else:
    added_course = Courses(course_name=new_course_name, course_duration=new_course_duration, diploma=new_diploma)
    session.add(added_course)
    session.commit()
    print(f'Курс додано!\nID курсу: {added_course.id}. Назва курсу: {added_course.course_name}')


session.close()