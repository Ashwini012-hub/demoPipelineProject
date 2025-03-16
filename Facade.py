# facade class is an interface between system classes and client
# facade class cannot be changed
#only system classes can be modified
# all system claases can be accessed at one place in facade which will e helpful for client


import requests

class GetTest:

    @staticmethod
    def request_to_get():
        request_url = requests.get("http://httpbin.org/get")
        response = request_url.text
        print(response)

class PostTest:

    @staticmethod
    def request_to_post():
        request_url = requests.post("http://httpbin.org/post", params={'name':'Ash', "age":30})
        print(request_url.status_code)

class DeleteTest:

    @staticmethod
    def request_to_delete():
        request_url = requests.delete("http://httpbin.org/delete")
        response = request_url.status_code
        print(response)

class CRUDFacade:
    def __init__(self):
        self.get_test = GetTest
        self.post_test = PostTest
        self.delete_test = DeleteTest

    def execute_crud_facade(self):
        self.get_test.request_to_get()
        self.post_test.request_to_post()
        self.delete_test.request_to_delete()

crud = CRUDFacade()
crud.execute_crud_facade()

