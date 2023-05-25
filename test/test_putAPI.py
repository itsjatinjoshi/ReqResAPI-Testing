import unittest
from APICalls.putAPI import PutAPIRequest
from Base.DrivedClass import URL
import logging
import pytest


@pytest.mark.usefixtures("class_fixture", "method_fixture")
class GetAPITest(unittest.TestCase):
    # base_url = URL().base_url()
    #
    # getAPI = PutAPIRequest(base_url)

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.getAPI = PutAPIRequest(self.base_url)

    def test_put_update_user(self):
        statusCode = self.getAPI.updateRequest("aa", "bb", page_num=3)
        logging.info("------------> ", statusCode.status_code)
        assert statusCode.status_code == 200
