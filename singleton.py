
#using class method
class WebDriver:
    '''THis is class variable it keep tracks whether instance is created or not
    when we say instance = None means still webdriver instance is not yet created'''
    __webdriver_instance = None
     #when first time when we are going to create webdriver object its going to call new
    def __new__(cls, *args, **kwargs):
        if cls.__webdriver_instance is None:
            #then its going to create it
            cls.__webdriver_instance = super(WebDriver, cls).__new__(cls, *args, **kwargs)
        return cls.__webdriver_instance
wd1 = WebDriver()
print(wd1)
wd2 = WebDriver()
print(wd2)






#2 using metaclass

class Singleton(type):
    __instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]

class MyClass(metaclass=Singleton):
    pass

t1 = MyClass
print(t1)
t2 = MyClass
print(t2)

