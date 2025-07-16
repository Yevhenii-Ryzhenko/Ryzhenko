"""
Завдяки цьому коду можна знайти конкретного студента по ID вводячи дані у консолі
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Students, Courses

engine = create_engine('sqlite:///students_and_courses.db')
Session = sessionmaker(bind=engine)
session = Session()

students = session.query(Students).all()

print("Список студентів:")
for student in students:
    print(f"{student.id}. {student.first_name} {student.last_name} (вік: {student.age})")

student_id = int(input("Введи ID студента, щоб переглянути його курси: "))

selected_student = session.query(Students).filter_by(id=student_id).first()

if selected_student:
    print(f"Студент {selected_student.first_name} {selected_student.last_name}  записаний на "
          f"{'такий' if len(selected_student.courses) == 1 else 'такі'} {len(selected_student.courses)} "
          f"{'курс' if len(selected_student.courses) == 1 else 'курси'}:\n")
    if selected_student.courses:
        for course in selected_student.courses:
            print(f"- {course.course_name} ({course.course_duration} міс.) | Диплом: {'Так' if course.diploma else 'Ні'}")
    else:
        print("❌ Студент не записаний на жоден курс.")
else:
    print("⚠️ Студента з таким ID не знайдено.")

session.close()