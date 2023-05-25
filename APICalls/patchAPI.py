import posixpath
from urllib.parse import urljoin

from Base.Base import BaseTest
import requests


class PatchAPIRequest(BaseTest):

    def __init__(self, url):
        super().__init__(url)
        self.url = url

    # todo: pass parameter for name, job etc according to method.
    default_value = 2
    _patchUpdateUser = f'api/users/'

    def patchUpdateUser(self, name, job, page_num = default_value):
        param = {"name": name, "job": job}
        path = posixpath.join(self._patchUpdateUser, str(page_num))
        # print(urljoin(self.url, path))
        response = self.patchCall(urljoin(self.url, path), params=param)

        return response
