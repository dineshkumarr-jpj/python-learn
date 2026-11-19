
import csv
import io

CSV_DATA = """id,name,department,salary,city
1,Arun,Sales,30000,Chennai
2,Priya,HR,45000,Chennai
3,Rahul,IT,60000,Bangalore
4,Divya,IT,75000,Chennai
5,Karthik,Finance,90000,Mumbai
6,Meena,Sales,52000,Bangalore
7,Suresh,IT,68000,Chennai
8,Anitha,HR,48000,Mumbai
"""
def bonus(salary, rate=0.1, *extras, **options):
    """Return salary * rate plus any extras; honour options['cap'] if given."""
    result = salary * rate + sum(extras)
    if "cap" in options:
        result = min(result, options["cap"])
    return result

class InvalidSalaryError(Exception):
    """Raised when a salary is negative."""

class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"{self.name} earns {self.salary} per month"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):  
        return f"{super().get_details()} and manages {self.team_size} people"
employees = list(csv.DictReader(io.StringIO(CSV_DATA)))
for e in employees:
    e["id"] = int(e["id"])
    e["salary"] = int(e["salary"])
above_50k = [e["name"] for e in employees if e["salary"] > 50000]
print("Above 50000:", above_50k)
raised = list(map(lambda e: {**e, "salary": round(e["salary"] * 1.10)}, employees))

chennai = [e["name"] for e in filter(lambda e: e["city"] == "Chennai", employees)]
print("Chennai:", chennai)
processed = []
for e in employees:
     if e["salary"] == 0:        # skip zero salaries
        continue
     processed.append(e["salary"])
     if e["salary"] > 85000:     # stop after the first salary above 85000
        break
  
try:
    Employee("Test", -500)
except InvalidSalaryError as err:
    print("Error:", err)
finally:
    print("Transaction finished")
assert bonus(50000) == 5000
assert bonus(50000, 0.1, 100, 200) == 5300
assert bonus(50000, 0.1, cap=3000) == 3000
assert Employee("A", 1000).annual_salary() == 12000
assert "manages 5 people" in Manager("M", 1000, 5).get_details()
assert raised[0]["salary"] == 33000
assert processed == [30000, 45000, 60000, 75000, 90000]