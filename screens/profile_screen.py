from selenium.webdriver.common.by import By

from screens.base_screen import BaseScreen
from utils.logs import log


class ProfileScreen(BaseScreen):
    USERNAME_FIELD = (By.ID, 'username_field_input')
    FIRSTNAME_FIELD = (By.ID, 'first_name_field_input')
    LASTNAME_FIELD = (By.ID, 'last_name_field_input')
    DONE_BTN = (By.ID, 'DONE')
    KEEP_BTN = (By.ID, 'keep_button')
    ACCEPT_PHOTO = (By.ID, 'ic edit done')

    def set_username(self, username):
        log.debug("Set new username: '{}'".format(username))
        self.el.set_text_clear(self.USERNAME_FIELD, username)

    def set_first_name(self, first_name):
        log.debug("Set new first name: '{}'".format(first_name))
        self.el.set_text_clear(self.FIRSTNAME_FIELD, first_name)

    def set_last_name(self, last_name):
        log.debug("Set new last name: '{}'".format(last_name))
        self.el.set_text_clear(self.LASTNAME_FIELD, last_name)

    def tap_done_btn(self):
        log.debug("Tap '{}' button".format("Done"))
        self.el.tap_btn(self.DONE_BTN)

    def tap_keep_btn(self):
        log.debug("Tap '{}' button".format("Keep"))
        self.el.click_btn(self.KEEP_BTN)

    def tap_accept_photo(self):
        log.debug("Tap '{}' button".format("Accept photo"))
        self.el.click_btn(self.ACCEPT_PHOTO)
