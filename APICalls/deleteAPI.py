import posixpath
from urllib.parse import urljoin

import requests

from Base.Base import BaseTest


class DeleteAPIRequest(BaseTest):

    def __init__(self, url):
        super().__init__(url)
        self.url = url

    default_value = 2
    _deleteUser = f'api/users/'

    def deleteRequest(self, page_num=default_value):
        path = posixpath.join(self._deleteUser, str(page_num))
        response = self.deleteCall(urljoin(self.url, path))
        return response
