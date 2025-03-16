'''wrapping up of variables and methods working on data together into a single unit is called as
Enacpasulation. Its acheived through access specifiers in python private , public, protected'''
'''we can access privtae variables either using methods or name mingling'''
class Finance:
    def __init__(self):
        self.__revenue = 10000
        self.sales = 100

    def display(self):
        print(f"revenue is {self.__revenue}")

F = Finance()
print(F.__dict__)
F.display()
print(F._Finance__revenue)


