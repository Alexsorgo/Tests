from selenium.webdriver.common.by import By

from configs import config
from screens.base_screen import BaseScreen
from utils.logs import log


class OtherProfileScreen(BaseScreen):
    USER_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME
    BLOCK_USER = (By.ID, 'Block user')
    ACCEPT_ALLERT = (By.ID, 'Yes')
    UNBLOCK_USER = (By.ID, 'Unblock user')
    SEND_A_MESSAGE = (By.ID, 'SEND A MESSAGE')
    CONTACT_USER = (By.ID, USER_NAME)
    BANNED_USER = (By.ID, 'Banned')
    LANGUAGE = (By.ID, 'Language Settings')
    STORAGE = (By.ID, 'Storage')

    def tap_block_user(self):
        log.debug("Tap '{}' button".format("Block user"))
        self.el.tap_btn(self.BLOCK_USER)

    def tap_accept_alert(self):
        log.debug("Tap '{}' in alert".format("Yes"))
        self.el.click_btn(self.ACCEPT_ALLERT)

    def tap_send_message(self):
        log.debug("Tap '{}' button on other profile".format("Send message"))
        self.driver.wait_till_element_is_displayed(self.UNBLOCK_USER)
        self.el.tap_btn(self.SEND_A_MESSAGE)

    def tap_user(self):
        log.debug("Open chat with '{}'".format("America Autotest"))
        self.el.tap_btn(self.CONTACT_USER)

    def tap_banned_user(self):
        log.debug("Open first '{}' user from list".format("Banned"))
        self.el.tap_btn(self.BANNED_USER)

    def tap_unblock_user(self):
        log.debug("Tap '{}' button".format("Unblock user"))
        self.el.tap_btn(self.UNBLOCK_USER)

    def open_language_settings(self):
        log.debug('Open language settings')
        self.el.tap_btn(self.LANGUAGE)

    def open_storage(self):
        log.debug('Open language settings')
        self.el.tap_btn(self.STORAGE)

    def is_profile_displayed(self):
        log.debug('Check other user profile displayed')
        return self.driver.find_element(*self.SEND_A_MESSAGE)
