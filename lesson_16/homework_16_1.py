class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager (Employee):

    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer (Employee):

    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class TeamLead (Manager, Developer):

    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size



lead = TeamLead("Yevhenii", 20000, "IT", "Python", 3)
print(f'lead.name: {lead.name},\nlead.salary: {lead.salary},\nlead.department: {lead.department},\n'
      f'lead.programming_language: {lead.programming_language},\nlead.team_size: {lead.team_size}')
# print(lead.name)
# print(lead.salary)
# print(lead.department)
# print(lead.programming_language)
# print(lead.team_size)

