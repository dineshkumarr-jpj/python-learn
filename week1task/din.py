
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"{self.name} - {self.salary}"
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return f"{self.name} - {self.salary} - Team Size: {self.team_size}"
def log_call(func):
    def wrapper(*args, **kwargs):
        print("Calling get_details")
        return func(*args, **kwargs)
    return wrapper

Manager.get_details = log_call(Manager.get_details)
employees = [
    Employee("Arun", 40000),
    Employee("Priya", 45000),
    Employee("Rahul", 60000),
    Employee("Divya", 75000),
    Employee("Karthik", 80000)
]
for emp in employees:
    if emp.salary < 50000:
        print(emp.name, "- Low Salary")

    elif emp.salary < 70000:
        print(emp.name, "- Medium Salary")

    else:
        print(emp.name, "- High Salary")

manager = Manager("Divya", 75000, 5)

print(manager.get_details())
  