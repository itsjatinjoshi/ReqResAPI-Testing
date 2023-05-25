import unittest
from APICalls.postAPI import PostAPIRequest
from Base.DrivedClass import URL
import logging
import pytest

@pytest.mark.usefixtures("class_fixture", "method_fixture")
class GetAPITest(unittest.TestCase):
    # base_url = URL().base_url()
    # getAPI = PostAPIRequest(base_url)

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.getAPI = PostAPIRequest(self.base_url)


    def test_create_user(self):
        statusCode = self.getAPI.createUser("aa", "bb")
        logging.info("------------> ", statusCode.status_code)
        assert statusCode.status_code == 201

    def test_register_user_successful(self):
        statusCode = self.getAPI.registerUserSuccessful("eve.holt@reqres.in", "pistol")
        logging.info("------------> ", statusCode.status_code)
        assert statusCode.status_code == 200

    def test_register_user_unsuccessful(self):
        statusCode = self.getAPI.registerUserUnsuccessful("sydney@fife")
        logging.info("------------> ", statusCode.status_code)
        assert statusCode.status_code == 400

    def test_login_user_successful(self):
        statusCode = self.getAPI.loginUserSuccessful("eve.holt@reqres.in", "cityslicka")
        logging.info("------------> ", statusCode.status_code)
        assert statusCode.status_code == 200

    def test_login_user_unsuccessful(self):
        statusCode = self.getAPI.loginUserUnsuccessful("peter@klaven")
        logging.info("------------> ", statusCode.status_code)
        assert statusCode.status_code == 400
