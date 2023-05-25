import posixpath
from urllib.parse import urljoin

import requests

from Base.Base import BaseTest


class PutAPIRequest(BaseTest):

    def __init__(self, url):
        super().__init__(url)
        self.url = url

    default_value = 3
    _updateUser = f'api/users/'

    def updateRequest(self, name, job, page_num=default_value):
        param = {"name": name, "job": job}
        # # url = (self.url + self._updateUser)
        # response = self.putCall(self.url + self._updateUser, params=param)

        path = posixpath.join(self._updateUser, str(page_num))
        print(urljoin(self.url, path))
        response = self.putCall(urljoin(self.url, path), params=param)
        print(response.text)
        return response
