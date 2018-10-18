from selenium.webdriver.common.by import By

from screens.add_contact.base_add_contact_screen import BaseAddContactScreen
from utils.logs import log


class ByNumberScreen(BaseAddContactScreen):
    COUNTRY_FILED = (By.ID, 'phone_field_code_input')
    PHONE_FIELD = (By.ID, 'phone_field_input')

    def set_contact_number(self, country_code, number):
        log.debug("Set contact number: '{}'".format(number))
        self.el.set_text_clear(self.COUNTRY_FILED, country_code)
        self.el.set_text(self.PHONE_FIELD, number)
