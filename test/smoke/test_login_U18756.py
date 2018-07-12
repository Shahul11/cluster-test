
import  unittest

from lib.UI.login_page import LoginPage # while you import the class u need to import the pacagename.file name then clas
from lib.utils import  create_driver
class TestLoginU18756(unittest.TestCase):

    def setup(self):
        self.driver=create_driver.get_driver_instance()
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_login_invalid_tc154321(self):
        self.login_page.wait_for_login_page_to_load()
        self.login_page.get_username_textbox().send_keys('admin')
        self.login_page.get_password_textbox().send_keys('sfdsfs')
        self.login_page.get_login_button().click()
        actual_error_msg=self.get_login_error_msg.text
        expected_error_msg='Username or Password is invalid. Please try again.'
        assert actual_error_msg==expected_error_msg