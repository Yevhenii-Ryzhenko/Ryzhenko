"""
Завдяки цьому коду можна знайти одного, або кількох студентів знаючи їх ID
"""

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Base, Students, Courses

engine = create_engine('sqlite:///students_and_courses.db')
Session = sessionmaker(bind=engine)
session = Session()

"""
У список необхідно ввести один, або кілька ID для виводу інформації про студентів
"""

student_id = [13, 15, 23, 0]

for i in student_id:
    selected_student = session.query(Students).filter_by(id=i).first()


    if selected_student:
        if selected_student.courses:
            print(f"Студент {selected_student.first_name} {selected_student.last_name} з ID {i} записаний на "
                  f"{'такий' if len(selected_student.courses) == 1 else 'такі'} {len(selected_student.courses)} "
                  f"{'курс' if len(selected_student.courses) == 1 else 'курси'}:\n")
            for course in selected_student.courses:
                print(f"- {course.course_name} (тривалість - {course.course_duration} міс.) | Диплом: {'Так' if course.diploma else 'Ні'}")
        else:
            print(f"Студент {selected_student.first_name} {selected_student.last_name} "
                  f"з ID {i} не записаний на жоден курс.")
    else:
        print(f"Студента з ID {i} не знайдено.")
    print(f'\n{'-'*50}\n')

session.close()