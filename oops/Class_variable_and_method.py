class Employee:
    emp_id = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.id = Employee.emp_id
        Employee.emp_id += 1

    def get_details(self):
         print(f"Name and Age of Employee is {self.name} {self.age}")
         print(f"Employee id is {Employee.emp_id}")
e1 = Employee('Ash',30)
e2 = Employee('Anu',28)
print(e1.__dict__)
print(e2.__dict__)
