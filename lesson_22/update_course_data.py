"""
Завдяки цьому коду можна оновити дані про конкретний курс
"""

from sqlalchemy import create_engine, Boolean
from sqlalchemy.orm import sessionmaker
from models import Base, Students, Courses

engine = create_engine('sqlite:///students_and_courses.db')
Session = sessionmaker(bind=engine)
session = Session()
all_courses = session.query(Courses).all()

""" Нижче необхідно вказати ID курсу дані якого потрібно змінити """

course_id = 9

""" Нижче потрібно вказати нові данні (вводити у лапках). Якщо якесь поле змінювати не потрібно - ставимо значення None """

new_course_name = "Ecology"
new_course_duration = None
new_diploma_value = True

searching_course = session.query(Courses).filter_by(id=course_id).first()

""" Виведення інформації про курс до оновлення даних (для наглядності) """
if not isinstance(new_diploma_value, bool):
    print(f'Поле diploma_value приймає лише значення True або False. Введіть коректні дані.')
else:
    if searching_course:
        print(f'Інформація про курс з ID {course_id}:\nНазва курсу: {searching_course.course_name}.\n'
              f'Тривалість: {searching_course.course_duration} міс.\n'
              f'Видача диплому: {"Так" if searching_course.diploma is True else "Ні"}.')
        if searching_course.students:
            print(f'На курс записано {len(searching_course.students)} студент(-ів).')
        else:
            print('На курс не записано жодного студента')
        print('-'*50)

        def update_course_data(course, course_name=None, course_duration=None, diploma_value=None):
            if course_name is not None:
                course.course_name = course_name
            if course_duration is not None:
                course.course_duration = course_duration
            if diploma_value is not None:
                course.diploma = diploma_value

        update_course_data(searching_course, course_name=new_course_name,
                           course_duration=new_course_duration, diploma_value=new_diploma_value)


        session.add(searching_course)

        session.commit()

        print(f'Інформація про курс з ID {course_id} оновлена!\nНазва курсу: {searching_course.course_name}.\n'
              f'Тривалість: {searching_course.course_duration} міс.\n'
              f'Видача диплому: {"Так" if searching_course.diploma is True else "Ні"}.')
        if searching_course.students:
           print(f'На курс записано {len(searching_course.students)} студент(-ів).')
        else:
            print('На курс не записано жодного студента')
    else:
        print(f'Курс з ID {course_id} не знайдено!\nНа даний момент маємо {len(all_courses)} курс(-ів). '
              f'Перевірте правильність даних!')

session.close()