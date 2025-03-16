#three elements handler, request and chain
#eg authentication chain
#handler: each authentication class
#request: dict object
#chain: basic, token, session authentication

from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self):
        self.next_handler = None

    @abstractmethod
    def authenticate(self,request):
        pass

    def set_next(self,handler):
        self.next_handler = handler

    def run(self, request):
        self.authenticate(request)
        if not request.get("is_authenticated"):
            if self.next_handler:
                self.next_handler.run(request)
            else:
                print("request is not authenticated")


class BasicAuthentication(Handler):
    def authenticate(self,request):
        if 'username' in request and 'password' in request:
            request["is_authenticated"] = True
            print("This request is Authenticated using basic authentication")


class TokenAuthentication(Handler):
    def authenticate(self,request):
        if 'token' in request:
            request["is_authenticated"] = True
            print("This request is Authenticated using token authentication")

class SessionAuthentication(Handler):
    def authenticate(self,request):
        if 'session' in request:
            request["is_authenticated"] = True
            print("This request is Authenticated using basic authentication")

#basic-token-session
#Get handler objects
basic_auth = BasicAuthentication()
token_auth = TokenAuthentication()
session_auth = SessionAuthentication()

#building a chain
basic_auth.set_next(token_auth)
token_auth.set_next(session_auth)

#test
request = {"username":"test", "password":"test"}
basic_auth.run(request)


