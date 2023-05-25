import requests


class BaseTest():

    def __init__(self, url):
        self.baseurl = url

    # todo : set the statusCode, request, response etc in this class

    def getCall(self, url, params=None):
        response = requests.get(url=url, params=params)
        return response

    def postCall(self, url, params=None, data=None, json=None):
        response = requests.post(url, params=params, data=data,
                                 json=json)
        return response

    def putCall(self, url, params=None):
        response = requests.get(url, params=params)
        return response

    def patchCall(self, url, params=None):
        response = requests.get(url, params=params)
        return response

    def deleteCall(self, url, params=None):
        response = requests.delete(url, params=params)
        return response