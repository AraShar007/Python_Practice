class Employee:
   def __init__(self, name,salary):
      self.name = name
      self.salary = salary
      print("just salary")
   def getName(self):
      return self.name
   def getSalary(self):
      return self.salary

class SalesOfficer(Employee):
   def __init__(self, name,salary, incentive):
      self.name = name
      self.salary = salary
      self.incentive = incentive
      print("salary & incentive")
   def getSalary(self, name, salary, incentive):
      super().getSalary()
      return self.salary+self.incentive

e1=Employee("Megha", 7000)
# print(f"The name and salary of employee is {e1.name} and {e1.salary}")
s1=SalesOfficer("anjali", 8000, 1000)
# print(s1.getSalary("anjali", 8000, 1000))
# print(f"The name {s1.name}, salary {s1.salary} and incentive {s1.incentive}")

