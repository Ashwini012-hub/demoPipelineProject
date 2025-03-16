class InvalidAge(Exception):
    def __init__(self):
        print('Age cannot be negative')

try:
    age = -10
    if age < 0:
        raise InvalidAge()
except Exception as var:
    print(var)