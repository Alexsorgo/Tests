from selenium.webdriver.common.by import By

from screens.base_screen import BaseScreen
from utils.logs import log


class BaseProfileScreen(BaseScreen):
    DONE_BTN = (By.ID, 'DONE')
    KEEP_BTN = (By.ID, 'keep_button')
    ACCEPT_PHOTO = (By.ID, 'ic edit done')

    def tap_done_btn(self):
        log.debug("Tap '{}' button".format("Done"))
        self.el.tap_btn(self.DONE_BTN)

    def tap_keep_btn(self):
        log.debug("Tap '{}' button".format("Keep"))
        self.el.click_btn(self.KEEP_BTN)

    def tap_accept_photo(self):
        log.debug("Tap '{}' button".format("Accept photo"))
        self.el.click_btn(self.ACCEPT_PHOTO)
