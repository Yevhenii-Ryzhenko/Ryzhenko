class Student:

    def __init__(self, first_name, last_name, age, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gpa = gpa

    def change_gpa(self, gpa):
        self.gpa = gpa

student_first = Student("Shevchenko", "Andriy", "48", "85")
student_second = Student("Rebrov", "Serhiy", "51", "84")

print(student_first.gpa)
print(student_second.gpa)

student_first.change_gpa("100")
student_second.change_gpa("99")

print(student_first.gpa)
print(student_second.gpa)