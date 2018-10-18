from selenium.webdriver.common.by import By

from screens.base_screen import BaseScreen
from utils.logs import log


class LoginScreen(BaseScreen):
    NEXT_BUTTON = (By.ID, 'NEXT')
    PHONE_FIELD = (By.ID, 'phone_field_input')
    CONFIRM_BUTTON = (By.ID, 'Confirm')
    SMS_CODE_FILED = (By.ID, 'code_field_input')
    COUNTRY_CODE = (By.ID, 'phone_field_code_input')
    TERMS = (By.ID, 'Terms of Service')
    LOGO = (By.ID, 'auth_light_logo')
    FIRST_NAME_FIELD = (By.ID, 'first_name_field_input')
    LAST_NAME_FIELD = (By.ID, 'last_name_field')
    DONE_BUTTON = (By.ID, 'DONE')
    CHECK_PAGE = (By.ID, 'How would you like to be called?')

    def set_full_number(self, code, number):
        self.set_country_code(code)
        self.set_phone_num(number)
        self.tap_next_btn()

    def set_country_code(self, code):
        log.debug("Set country code: {}".format(code))
        self.el.set_text_clear(self.COUNTRY_CODE, code)

    def set_phone_num(self, number):
        log.debug("Set phone number: {}".format(number))
        self.el.set_text(self.PHONE_FIELD, number)

    def tap_next_btn(self):
        log.debug("Tap '{}' button".format("Next"))
        self.el.tap_btn(self.NEXT_BUTTON)

    def tap_confirm_btn(self):
        log.debug("Tap '{}' button".format("Confirm"))
        self.el.click_btn(self.CONFIRM_BUTTON)

    def set_sms(self, sms_code='903182'):
        log.debug("Set sms code: {}".format(sms_code))
        self.el.set_text(self.SMS_CODE_FILED, sms_code)
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def set_first_name(self, first_name):
        log.debug("Set first name: {}".format(first_name))
        self.el.set_text(self.FIRST_NAME_FIELD, first_name)

    def set_last_name(self, last_name):
        log.debug("Set last name: {}".format(last_name))
        self.el.set_text(self.LAST_NAME_FIELD, last_name)

    def tap_done_btn(self):
        log.debug("Tap '{}' button".format("Done"))
        self.el.click_btn(self.DONE_BUTTON)
