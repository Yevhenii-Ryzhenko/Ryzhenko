"""
Тут можна додати конкретний (існуючий) курс будь-якому студенту
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Students, Courses

engine = create_engine('sqlite:///students_and_courses.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

"""
Нижче необхідно ввести ID існуючого студента та назву існуючого курсу 
"""

student_id = 20
student_course = "Physics"

selected_student = session.query(Students).filter_by(id=student_id).first()
desirable_course = session.query(Courses).filter_by(course_name=student_course).first()

if selected_student:
    if desirable_course:
        if desirable_course in selected_student.courses:
            print(f'Студент {selected_student.first_name} {selected_student.last_name} уже '
                  f'записаний на курс "{desirable_course.course_name}".')
        else:
            selected_student.courses.append(desirable_course)
            session.commit()
            print(f'Студенту {selected_student.first_name} {selected_student.last_name} віком {selected_student.age} років '
                  f'додано курс {desirable_course.course_name} тривалістю {desirable_course.course_duration} міс '
                  f'{'з видачею диплому' if desirable_course.diploma is True else 'без видачі диплому'}.')
    else:
        print(f'Курсу {student_course} в нас немає.')
else:
    print(f'Студента з ID {student_id} не знайдено')

session.close()