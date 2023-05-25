import unittest
from APICalls.patchAPI import PatchAPIRequest
from Base.DrivedClass import URL
import logging
import pytest


@pytest.mark.usefixtures("class_fixture", "method_fixture")
class GetAPITest(unittest.TestCase):
    # base_url = URL().base_url()
    #
    # getAPI = PatchAPIRequest(base_url)

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.getAPI = PatchAPIRequest(self.base_url)

    def test_patch_update_user(self):
        statusCode = self.getAPI.patchUpdateUser("aa", "bb", page_num=11)
        # logging.info("------------> ", statusCode.status_code)
        # print(statusCode.text)
        assert statusCode.status_code == 200
