class A:
    def display(self):
        print("I am class A")

class B(A):
    def printer(self):
        print("I am in class B")

class C(B):
    pass

b = B()
b.display()
b.printer()