
# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]
#print(people_records)
people_records.insert(0,('Yevhenii', 'Ryzhenko', '29', 'QA Engineer', 'Odesa'))

# print(people_records)
# print(people_records[1])
# print(people_records[5])
people_records[1], people_records[5] = people_records[5], people_records[1]
print(people_records)
# print(people_records[1])
# print(people_records[5])

first_person = people_records[6]
second_person = people_records[10]
third_person = people_records[13]
#print(first_person, second_person, third_person)
if first_person[2] >= 30 and second_person[2] >= 30 and third_person[2] >= 30:
  print ('Всі люди модифікованого списку з індексами 6, 10 та 13 мають вік ≥ 30.')
else:
   if first_person[2] < 30:
    print(f'Людина з модифікованого списку з індексом 6 {people_records[6]} не досягла 30 років')
   if second_person[2] < 30:
    print(f'Людина з модифікованого списку з індексом 10 {people_records[10]} не досягла 30 років')
   if third_person[2] < 30:
    print(f'Людина з модифікованого списку з індексом 13 {people_records[13]} не досягла 30 років')

