from selenium.webdriver.common.by import By

from tests.configs import config
from tests.enums import error_enums
from tests.screens.login_screen import LoginScreen
from tests.base_test import BaseTest
from tests.utils.logs import log
from tests.utils.verify import Verify


class Test_w(BaseTest):
    """
    Nynja registration with max limit char in first name
    """
    COUNTRY_CODE_NUMBER = config.CHINA_COUNTRY_CODE
    PHONE_NUMBER = config.CHINA_NUMBER
    FIRST_NAME = config.INCORRECT_FIRSTNAME
    LAST_NAME = config.CHINA_LASTNAME

    def test_w(self):
        login = LoginScreen(self.driver)
        log.info("Registration max limit firstname chars")
        if not self.driver.find_elements(*(By.ID, 'How would you like to be called?')):
            login.set_full_number(self.COUNTRY_CODE_NUMBER, self.PHONE_NUMBER)
            login.tap_confirm_btn()
            login.set_sms()
        login.set_first_name(self.FIRST_NAME)
        login.set_last_name(self.LAST_NAME)
        login.tap_done_btn()

        log.info("Verify user is not registered.")
        Verify.true(login.error_verify(error_enums.MAX_FIRSTNAME), "Limit doesn't work")
