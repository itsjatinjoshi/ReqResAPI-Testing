import unittest

import pytest

from APICalls.deleteAPI import DeleteAPIRequest
from Base.DrivedClass import URL
import logging

@pytest.mark.usefixtures("class_fixture", "method_fixture")
class GetAPITest(unittest.TestCase):
    # base_url = URL().base_url()
    #
    # getAPI = DeleteAPIRequest(base_url)


    @pytest.fixture(autouse=True)
    def classObject(self):
        self.getAPI = DeleteAPIRequest(self.base_url)

    def test_delete_update_user(self):
        statusCode = self.getAPI.deleteRequest(page_num=3)
        logging.info("------------> ", statusCode.status_code)
        assert statusCode.status_code == 204
