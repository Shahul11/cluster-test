
import unittest
import time

from lib.UI.login_page import LoginPage
from lib.utils import create_driver

class TestLoginU18756(unittest.TestCase):

    def setUp(self):
        self.driver=create_driver.get_driver_instance()
        self.login_page = LoginPage(self.driver)

    def test_login_invalid_tc154321(self):
        self.login_page.wait_for_login_page_to_load()
        self.login_page.get_username_textbox().send_keys('admin')
        self.login_page.get_password_textbox().send_keys('sfdsfs')
        self.login_page.get_login_button().click()
        time.sleep(5)
        actual_error_msg = self.login_page.get_login_error_msg().text
        expected_error_msg='Username or Password is invalid. Please try again.'
        assert actual_error_msg==expected_error_msg

    def tearDown(self):
        self.driver.close()