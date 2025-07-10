"""
Завдяки цьому коду можна знайти один, або кілька курсів знаючи їх ID
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Students, Courses

engine = create_engine('sqlite:///students_and_courses.db')
Session = sessionmaker(bind=engine)
session = Session()

"""
У список необхідно ввести один, або кілька ID для виводу інформації про курси
"""

course_id = [2,3]

for c in course_id:
    selected_course = session.query(Courses).filter_by(id=c).first()

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
            print(f"На курс {selected_course.course_name} не записаний жоден студент.")
    else:
        print(f"Курсу з ID {course_id} не знайдено.")


session.close()