class Employee:
  def __init__(self, name,salary):
        self.name = name
        self.salary = salary
  def detail(self):
   print("Name:", self.name)        
   print(self.name,"annual Salary:", self.salary*12)

emp1=Employee("arun",30000)
emp2=Employee("priya",45000)
emp1.detail()
emp2.detail()
    
