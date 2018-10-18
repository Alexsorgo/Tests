from selenium.webdriver.common.by import By

from screens.profile_edit.base_profile_screen import BaseProfileScreen
from utils.logs import log


class MyNameScreen(BaseProfileScreen):
    FIRST_NAME_FIELD = (By.ID, 'first_name_field_input')
    LAST_NAME_FIELD = (By.ID, 'last_name_field_input')

    def set_first_name(self, first_name):
        log.debug("Set new first name: '{}'".format(first_name))
        self.el.set_text_clear(self.FIRST_NAME_FIELD, first_name)

    def set_last_name(self, last_name):
        log.debug("Set new last name: '{}'".format(last_name))
        self.el.set_text_clear(self.LAST_NAME_FIELD, last_name)
