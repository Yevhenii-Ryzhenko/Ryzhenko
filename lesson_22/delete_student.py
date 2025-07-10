"""
Завдяки цьому коду можна видалити студента із БД
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Students, Courses

engine = create_engine('sqlite:///students_and_courses.db')
Session = sessionmaker(bind=engine)
session = Session()

"""
Нижче необхідно ввести ID студента, дані якого потрібно видалити
"""

id_student_for_delete = 49

all_students = session.query(Students).all()

student_for_delete = session.query(Students).filter_by(id=id_student_for_delete).first()

if student_for_delete:
    print(f'Ви дійсно бажаєте видалити дані студента з ID {student_for_delete.id}?\nІнформація про студента:\n'
          f'Повне ім\'я: {student_for_delete.first_name} {student_for_delete.last_name}. Вік: {student_for_delete.age}.\n')
    if student_for_delete.courses:
        print(f'Студент записаний на {len(student_for_delete.courses)} курс(-ів):')
        for course in student_for_delete.courses:
            print(f"- {course.course_name} ({course.course_duration} міс.) | Диплом: {'Так' if course.diploma else 'Ні'}")
    else:
        print(f"Студент не записаний на жоден з курсів.")
    print(f'Підтвердіть видалення студента з ID {student_for_delete.id}.')
    confirmation_lvl_1 = input('Для підтвердження  введіть "Y", для скасування - "N": ')
    if confirmation_lvl_1 == "Y":
        print(f'Ви впевнені?')
        confirmation_lvl_2 = input("Y або N: ")
        if confirmation_lvl_2 == "Y":
            session.delete(student_for_delete)
            session.commit()
            print(f'Інформація про студента з ID {id_student_for_delete} успішно видалена')
        elif confirmation_lvl_2 == "N":
            print(f'Процес видалення студента перервано.')
        else:
            print(f'Необхідно ввести "Y" або "N"')
    elif confirmation_lvl_1 == "N":
        print(f'Процес видалення студента перервано.')
    else:
        print(f'Необхідно ввести "Y" або "N"')
else:
    print(f'Студент з ID {id_student_for_delete} не знайдений!')

session.close()