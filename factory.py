#Factory Method Design Pattern define an interface for creating an object, but let subclass decide which class to instantiate.

from selenium import webdriver
from abc import ABC, abstractmethod

class OrganizeManager(ABC):
    @abstractmethod
    def get_driver(self):
        pass

    @abstractmethod
    def quit_driver(self):
        pass

class OrganizeChromeDriver(OrganizeManager):
    def __init__(self,driver):
        self.driver = driver
        self.driver.get_driver = webdriver.Chrome()
        self.driver.quit = driver.close

    def get_driver(self):
        return self.driver.get_driver

    def quit_driver(self):
        return self.driver.quit

class OrganizeFFDriver(OrganizeManager):
    def __init__(self,driver):
        self.driver = driver
        self.driver.get_driver = webdriver.firefox
        self.driver.quit = "Quit Driver"

    def get_driver(self):
        return self.driver.get_driver

    def quit_driver(self):
        return self.driver.quit

class DriverManagerFactory:
    @staticmethod
    def select_webdriver(driver_type):
        try:
            if driver_type == 'chrome':
                return OrganizeChromeDriver(driver_type)
        except:
            raise AssertionError("chrome driver not available")

        try:
            if driver_type == 'firefox':
                return OrganizeFFDriver(driver_type)
        except:
            raise AssertionError("firefox driver not available")



class Test1:
    def chrome_test(self):
        driver_manager = DriverManagerFactory.select_webdriver('chrome')
        driver_manager.get_driver()
        driver_manager.quit_driver()


class Test2:
    def firefox_test(self):
        driver_manager = DriverManagerFactory.select_webdriver('firefox')
        driver_manager.get_driver()
        driver_manager.quit_driver()

# t = Test1()
# t.chrome_test()


