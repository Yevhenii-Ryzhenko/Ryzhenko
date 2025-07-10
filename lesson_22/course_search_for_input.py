"""
Завдяки цьому коду можна знайти інформацію про конкретний курс по ID вводячи дані у консолі
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Students, Courses

engine = create_engine('sqlite:///students_and_courses.db')
Session = sessionmaker(bind=engine)
session = Session()

all_course = session.query(Courses).all()

print("Список курсів:")
for course in all_course:
    print(f"{course.id}. {course.course_name}. Тривалість: {course.course_duration} міс. Видача диплому: {course.diploma})")

course_id = int(input("Введіть ID курсу, щоб переглянути список студентів записаного на нього: "))

selected_course = session.query(Courses).filter_by(id=course_id).first()

if selected_course:
    student_count = len(selected_course.students)
    print(f'\nНа курс {selected_course.course_name} тривалістю {selected_course.course_duration} міс '
          f'{'З видачею диплому' if selected_course.diploma is True else 'БЕЗ видачі диплому'} '
          f'записано {len(selected_course.students)} студент(-ів).\n'
          f'Список студентів:')
    if student_count:
        for student in selected_course.students:
            print(f'- Ім\'я: {student.first_name}. Прізвище: {student.last_name}. Вік: {student.age}')
    else:
        print(f"На курс {selected_course.course_name} не записаний жоден студент. Бідося.")
else:
    print(f"Курсу з ID {course_id} не знайдено.")


session.close()