from selenium.webdriver.common.by import By

from tests.screens.profile_edit.base_profile_screen import BaseProfileScreen
from tests.utils.logs import log


class MyUsernameScreen(BaseProfileScreen):
    USERNAME_FIELD = (By.ID, 'username_field_input')

    def set_username(self, username):
        log.debug("Set new username: '{}'".format(username))
        self.el.set_text_clear(self.USERNAME_FIELD, username)

