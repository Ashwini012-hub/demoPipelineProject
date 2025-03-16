#creating class and  instance object and method
class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_details(self):
         print(f"Name and Age of Employee is {self.name} {self.age}")

e1 = Employee('Ash',30)
print(e1)
print(e1.__dict__)
e1.get_details()