from selenium.webdriver.common.by import By

from tests.screens.add_contact import BaseAddContactScreen
from tests.utils.logs import log


class ByUsernameScreen(BaseAddContactScreen):
    CONTACT_USERNAME_FIELD = (By.ID, 'username_field_input')

    def set_contact_username(self, username):
        log.debug("Set contact username: '{}'".format(username))
        self.el.set_text(self.CONTACT_USERNAME_FIELD, username)
