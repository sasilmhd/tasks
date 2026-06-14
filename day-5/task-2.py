class Employee:
    def __init__(self,name,department,salary):
        self.name=name
        self.department=department
        self.salary=salary
    def get_info(self):
        print("="*10)
        print(f"{self.name} in the {self.department} have a salary of {self.salary}")
    def __str__(self):
        return f"He was working at {self.department} department"
emp=Employee("Babu","BCA",50000)
print(emp)
print("Name:\t",emp.name)
print("Department:\t",emp.department)
print("Salary:\t",emp.salary)
emp.get_info()