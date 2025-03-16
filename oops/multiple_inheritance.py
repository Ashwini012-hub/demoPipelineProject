class Country:
    def __init__(self):
        print("country class constructor called")
        self.city = 'Delhi'

class State:
    def __init__(self):
        print("State class constructor called")
        self.city = 'Karnataka'

class District(State, Country):
    def __init__(self):
        super().__init__()
        print("District class constructor called")
        self.city = 'Banglore'

d = District()
print(d.__dict__)


