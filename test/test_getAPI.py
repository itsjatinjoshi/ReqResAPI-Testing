import unittest
from APICalls.getAPI import GetAPIRequest
from Base.DrivedClass import URL
import logging
import pytest


@pytest.mark.usefixtures("class_fixture", "method_fixture")
class GetAPITest(unittest.TestCase):
    # base_url = URL().base_url()
    #
    # getAPI = GetAPIRequest(base_url)

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.getAPI = GetAPIRequest(self.base_url)

    def test_get_all_user_list(self):
        statusCode = self.getAPI.getAllUserList(page_num=3)
        # logging.info("------------> ", statusCode.status_code)
        # print("ALL USER LIST: ", statusCode.content)
        assert statusCode.status_code == 200, "GET Request for all user failed."

    def test_get_user_list(self):
        statusCode = self.getAPI.getUserList(page_num=3)
        # logging.info("------------> ", statusCode.status_code)
        # print("SINGLE USER LIST: ", statusCode.content)
        assert statusCode.status_code == 200, "GET Request for user failed."

    def test_user_not_found_list(self):
        statusCode = self.getAPI.getUserNotFoundList(page_num=23)
        # logging.info("------------> ", statusCode.status_code)
        # print("USER NOT FOUND LIST: ", statusCode.content)
        # print(statusCode.status_code)
        assert statusCode.status_code == 404, "GET Request for no user found failed."

    #
    def test_all_unknown_user_list(self):
        statusCode = self.getAPI.getAllUnknownUserList()
        # logging.info("------------> ", statusCode.status_code)
        # print("ALL UNKNOWN USER LIST: ", statusCode.content)
        assert statusCode.status_code == 200, "GET Request for all Unknown user failed."

    def test_get_single_unknown_user_list(self):
        statusCode = self.getAPI.getSingleUnknownUserList()
        # logging.info("------------> ", statusCode.status_code)
        # print("SINGLE UNKNOWN USER LIST: ", statusCode.content)
        assert statusCode.status_code == 200, "GET Request for Single Unknown user failed."

    #
    def test_single_user_not_found_list(self):
        statusCode = self.getAPI.getSingleUserNotFoundList(page_num=23)
        # logging.info("------------> ", statusCode.status_code)
        # print("SINGLE USER NOT FOUND LIST: ", statusCode.content)
        assert statusCode.status_code == 404, "GET Request for Single User Not Found failed."
