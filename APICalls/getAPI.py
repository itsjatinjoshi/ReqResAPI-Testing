import posixpath
from urllib.parse import urljoin

from Base.Base import BaseTest
import requests


class GetAPIRequest(BaseTest):

    def __init__(self, url):
        super().__init__(url)
        self.url = url

    # todo: pass parameter for default value
    default_value = 2
    delayValue = 3
    # GET API REQUESTS
    _allUsersList = f'api/users?'
    _singleUserList = f'api/users/'
    _userNotFoundList = f'api/users/'  # use parameter 23 for it
    _allUnknownUsersList = f'api/unknown'
    _singleUnknownUserList = f'api/unknown/'
    _singleUserNotFoundList = f'api/unknown/'  # use parameter 23 for it

    def getAllUserList(self, page_num=default_value):
        param = {'page': page_num}
        allUserList = self.getCall(self.url + self._allUsersList, params=param)
        return allUserList

    def getUserList(self, page_num=default_value):
        path = posixpath.join(self._singleUserList, str(page_num))
        userList = self.getCall(urljoin(self.url, path))
        return userList

    def getUserNotFoundList(self, page_num=23):
        path = posixpath.join(self._userNotFoundList, str(page_num))
        userList = self.getCall(urljoin(self.url, path))
        # print(userList.text)
        return userList

    def getAllUnknownUserList(self):
        allUnknownUserList = self.getCall(self.url + self._allUnknownUsersList)
        return allUnknownUserList

    def getSingleUnknownUserList(self, page_num=default_value):
        path = posixpath.join(self._singleUnknownUserList, str(page_num))
        userList = self.getCall(urljoin(self.url, path))
        # print(userList.text)
        return userList

    def getSingleUserNotFoundList(self, page_num=23):
        path = posixpath.join(self._singleUserNotFoundList, str(page_num))
        userList = self.getCall(urljoin(self.url, path))
        # print(userList.text)
        return userList
