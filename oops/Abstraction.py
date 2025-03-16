# from abc import ABC, abstractmethod
#
# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass
#
# class Car(Vehicle):
#     def start_engine(self):
#         return "Car engine started"
#
# car = Car()
# print(car.start_engine())  # Output: Car engine started



from abc import ABC, abstractmethod

class Calculator(ABC):
    def __init__(self,value):
        self.value = value

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def sub(self):
        pass

class B(Calculator):
    def add(self):
        print(self.value + 100)

    def sub(self):
        print(self.value - 100)



b = B(100)
b.add()
b.sub()