"""
Завдяки цьому коду можна оновити дані про конкретного студента
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Students, Courses

engine = create_engine('sqlite:///students_and_courses.db')
Session = sessionmaker(bind=engine)
session = Session()
all_students = session.query(Students).all()

""" Нижче необхідно вказати ID студента дані якого потрібно змінити """

student_id = 49

""" Нижче потрібно вказати нові данні (вводити у лапках. Якщо якесь поле змінювати не потрібно - ставимо значення None """

new_first_name = "Ronald"
new_last_name = "Cat"
new_age = 5

""" Нижче потрібно ввести значення назви курсу, на який необхідно записати студента.
    Список курсів наявних на даний момент (при вставленні використовувати лапки):
    
Maths
Literature
Poetry
Physics
Chemistry
Biology
Programming
Marketing
Ecology
Testing
History

Якщо курс студенту додавати не потрібно - ставимо значення None
"""

new_course_for_student = "Maths"

searching_student = session.query(Students).filter_by(id=student_id).first()
new_course = None
if new_course_for_student:
    new_course = session.query(Courses).filter_by(course_name=new_course_for_student).first()


""" Виведення інформації про студента до оновлення даних (для наглядності) """

if searching_student:
    print(f'Інформація про студента з ID {student_id}:\nІм\'я: {searching_student.first_name}.\n'
      f'Прізвище: {searching_student.last_name}\nВік: {searching_student.age}')
    if searching_student.courses:
        print(f'Записаний на {len(searching_student.courses)} курс(ів):')
        for course in searching_student.courses:
            print(
                f"- {course.course_name}")
    print('-'*50)

    def update_student_data(student, first_name=None, last_name=None, age=None):
        if first_name is not None:
            student.first_name = first_name
        if last_name is not None:
            student.last_name = last_name
        if age is not None:
            student.age = age

    update_student_data(searching_student, first_name=new_first_name, last_name=new_last_name, age=new_age)

    if new_course and new_course not in searching_student.courses:
        searching_student.courses.append(new_course)
    else:
        print(f'Студент вже записаний на курс {new_course_for_student}\n')

    session.add(searching_student)

    session.commit()

    if searching_student:
        print(f'Інформація про студента з ID {student_id} успішно оновлена!\nІм\'я: {searching_student.first_name}.\n'
          f'Прізвище: {searching_student.last_name}\nВік: {searching_student.age}')
        if searching_student.courses:
            print(f'Записаний на {len(searching_student.courses)} курс(ів):')
            for course in searching_student.courses:
                print(
                    f"- {course.course_name}")
else:
    print(f'Студента з ID {student_id} не знайдено!\nНа даний момент маємо {len(all_students)} студенти(-ів). '
          f'Перевірте правильність даних!')

session.close()