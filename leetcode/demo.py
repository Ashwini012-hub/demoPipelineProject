class A:
    def __init__(self,name, id):
        self.name = name
        self.id = id

class B(A):
    def __init__(self,name, id):
        super().__init__(name, id)
        self.name = 'Ash'
        self.id = 30
b = B('Ash', 30)
print(b.__dict__)

