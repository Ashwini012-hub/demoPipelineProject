#Behavioural design pattern they deal with communication betweeen objects and classes. they focus on how objects and classes communicate to accomplish task
#Strategy : it allows to group different types of strategies under one abstarct class
#it allows to decide startegy at run time as per requirement

from abc import ABC,abstractmethod

#abstrct class
class LoginTypeStrategy(ABC):
    @abstractmethod
    def login(self):
        pass
#concrete classes
class InternalUserLogin(LoginTypeStrategy):

    def login(self):
        return 'Logged in as internal user'

class ExternalUserLogin(LoginTypeStrategy):

    def login(self):
        return 'Logged in as external user'
#main class
class StrategyTest:
    def log_in_as(self,login_type_startegy:LoginTypeStrategy):
        return login_type_startegy.login()

s = StrategyTest()
type = s.log_in_as(ExternalUserLogin())
print(type)







