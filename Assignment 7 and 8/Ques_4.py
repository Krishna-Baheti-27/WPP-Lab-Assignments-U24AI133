class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __add__(self, other):
        return Employee(self.name + " & " + other.name, self.salary + other.salary)
    
    def __sub__(self, other):
        return abs(self.salary - other.salary)
    
    def __str__(self):
        return f"Employee(Name: {self.name}, Salary: {self.salary})"

name1 = input("Enter name of first employee: ")
salary1 = float(input("Enter salary of first employee: "))
name2 = input("Enter name of second employee: ")
salary2 = float(input("Enter salary of second employee: "))

emp1 = Employee(name1, salary1)
emp2 = Employee(name2, salary2)

combined = emp1 + emp2
salary_diff = emp1 - emp2

print("Combined Employee:", combined)
print("Salary Difference:", salary_diff)