"""
Завдяки цьому коду можна видалити конкретний курс у конкретного студента
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Students, Courses

engine = create_engine('sqlite:///students_and_courses.db')
Session = sessionmaker(bind=engine)
session = Session()

"""
Нижче необхідно ввести ID студента та назву курсу, який необхідно видалити
"""

id_student = 15
course_to_delete = "Chemistry"


student_for_processing = session.query(Students).filter_by(id=id_student).first()
deleted_course = session.query(Courses).filter_by(course_name=course_to_delete).first()

if student_for_processing:
    print(f'Ви працюєте зі студентом ID {student_for_processing.id}. Ім\'я: {student_for_processing.first_name} '
          f'{student_for_processing.last_name} віком {student_for_processing.age}.')
    if deleted_course:
        if deleted_course in student_for_processing.courses:
            print(f'Студент був записаний на {len(student_for_processing.courses)} курс(-ів):')
            for course in student_for_processing.courses:
                print(
                    f"- {course.course_name} ({course.course_duration} міс.) | Диплом: {'Так' if course.diploma else 'Ні'}")
            student_for_processing.courses.remove(deleted_course)
            session.commit()

            print(f'З профілю студента видалено курс {course_to_delete}.')
            print(f'Після видалення студент записаний на {len(student_for_processing.courses)} курсів:')
            for new_course in student_for_processing.courses:
                print(f"- {new_course.course_name} ({new_course.course_duration} міс.) | Диплом: {'Так' if new_course.diploma else 'Ні'}")
        else:
            print(f"Студент не записаний на жоден з курсів.")
    else:
        print(f'Курсу {course_to_delete} в нас немає')
else:
    print(f'Студент з ID {id_student} не знайдений!')

session.close()