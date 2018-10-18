from selenium.webdriver.common.by import By

from screens.add_contact.base_add_contact_screen import BaseAddContactScreen
from utils.logs import log


class ByUsernameScreen(BaseAddContactScreen):
    CONTACT_USERNAME_FIELD = (By.ID, 'username_field_input')

    def set_contact_username(self, username):
        log.debug("Set contact username: '{}'".format(username))
        self.el.set_text(self.CONTACT_USERNAME_FIELD, username)
