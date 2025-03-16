class Animal:
    def __init__(self,name):
        self.name = name
        self.isalive = True

    def eat(self):
        print(f"Animal {self.name} is eating")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

d = Dog('Dog')
print(d.__dict__)
(d.eat())
