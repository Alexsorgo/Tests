from selenium.webdriver.common.by import By

from screens.base_screen import BaseScreen
from utils.logs import log


class BaseChannelScreen(BaseScreen):
    CHANNEL_BACK_BTN = (By.ID, 'back_button')

    def tap_cancel_create_channel(self):
        log.debug("Tap cancel create channel button")
        self.el.tap_btn(self.CHANNEL_BACK_BTN)
