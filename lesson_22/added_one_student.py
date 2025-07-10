"""
Тут можна додати нового студента до БД
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Students, Courses

engine = create_engine('sqlite:///students_and_courses.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

"""
Для додавання студента необхідно заповнити поля student_first_name, student_last_name та student_age. 
Якщо студенту необхідно одразу додати курс то необхідно поле student_course заповнити згідно наявних курсів.
Актуальний список курсів на момент написання коду:
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
"""

student_first_name = "Dead"
student_last_name = "Pool"
student_age = 40
student_course = "Physics"


manually_added_student = Students(first_name=student_first_name, last_name=student_last_name, age=student_age)
desirable_course = session.query(Courses).filter_by(course_name=student_course).first()
existing_student = session.query(Students).filter_by(
    first_name=student_first_name, last_name=student_last_name, age=student_age).first()
if existing_student:
    print(f'Студент на ім\'я {existing_student.first_name} та прізвище {existing_student.last_name} '
          f'віком {existing_student.age} років вже є в базі.\nЙого ID: {existing_student.id}')
elif desirable_course:
    manually_added_student.courses.append(desirable_course)
    course = manually_added_student.courses[0]
    print(f'До курсу {course.course_name} тривалістю {course.course_duration} міс '
          f'{'з видачею диплому' if course.diploma is True else 'без видачі диплому'}. '
          f'Додано студента {manually_added_student.first_name} {manually_added_student.last_name} '
          f'віком {manually_added_student.age}')
else:
    print(f'Курсу {student_course} в нас немає.')

session.add(manually_added_student)

session.commit()
session.close()