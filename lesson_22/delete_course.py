"""
Завдяки цьому коду можна видалити курс з БД
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Students, Courses

engine = create_engine('sqlite:///students_and_courses.db')
Session = sessionmaker(bind=engine)
session = Session()

"""
Нижче потрібно ввести ID курсу, який необхідно видалити
"""

id_course_for_delete = 11

all_courses = session.query(Courses).all()

course_for_delete = session.query(Courses).filter_by(id=id_course_for_delete).first()

if course_for_delete:
    print(f'Ви дійсно бажаєте видалити курс з ID {course_for_delete.id}?\nІнформація про курс:\n'
          f'Назва: {course_for_delete.course_name} тривалістю {course_for_delete.course_duration} міс.\n'
          f'{'З видачею диплому' if course_for_delete.diploma is True else 'Без видачі диплому'}.')
    if course_for_delete.students:
        print(f'На курс записано {len(course_for_delete.students)} студентів. Бажаєте переглянути список студентів?')
        viewing_the_list_of_students = input('Введіть "Y" для перегляду списку і "N" для пропуску цього етапу: ')
        if viewing_the_list_of_students == "Y":
            for student in course_for_delete.students:
                print(f"- {student.first_name} {student.last_name}. Вік: {student.age}")
        elif viewing_the_list_of_students == "N":
            print(f"Добре. Тоді переходимо до наступного етапу.")
        else:
            print(f'Необхідно ввести "Y" або "N"')
    else:
        print(f"На курс не записаний жоден зі студентів.")
    print(f'Підтвердіть видалення курсу {course_for_delete.course_name} з ID {course_for_delete.id}.')
    confirmation_lvl_1 = input('Для підтвердження  введіть "Y", для скасування - "N": ')
    if confirmation_lvl_1 == "Y":
        print(f'Ви впевнені?')
        confirmation_lvl_2 = input("Y або N: ")
        if confirmation_lvl_2 == "Y":
            session.delete(course_for_delete)
            session.commit()
            print(f'Курс з ID {id_course_for_delete} успішно видалено.')
        elif confirmation_lvl_2 == "N":
            print(f'Процес видалення курсу перервано.')
        else:
            print(f'Необхідно ввести "Y" або "N"')
    elif confirmation_lvl_1 == "N":
        print(f'Процес видалення курсу перервано.')
    else:
        print(f'Необхідно ввести "Y" або "N"')
else:
    print(f'Курс з ID {id_course_for_delete} не знайдений!')

session.close()