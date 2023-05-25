from Base.Base import BaseTest
import requests


class PostAPIRequest(BaseTest):

    def __init__(self, url):
        super().__init__(url)
        self.url = url

    # todo: pass parameter for name, job etc according to method.
    _createUser = 'api/users'
    _registerUserSuccessful = 'api/register'
    _registerUserUnsuccessful = 'api/register'
    _loginUserSuccessful = 'api/login'
    _loginUserUnsuccessful = 'api/login'

    def createUser(self, name, job):
        param = {"name": name, "job": job}
        response = self.postCall(self.url + self._createUser, param)
        return response

    def registerUserSuccessful(self, email, password):
        param = {"email": email, "password": password}

        response = self.postCall(self.url + self._registerUserSuccessful,
                                 data=param)
        return response

    def registerUserUnsuccessful(self, email):
        param = {"email": email}
        response = self.postCall(self.url + self._registerUserUnsuccessful,
                                 data=param)
        return response

    def loginUserSuccessful(self, email, password):
        param = {"email": email, "password": password}
        response = self.postCall(self.url + self._loginUserSuccessful,
                                 json=param)
        return response

    def loginUserUnsuccessful(self, email):
        param = {"email": email}
        response = self.postCall(self.url + self._loginUserUnsuccessful,
                                 json=param)
        return response
