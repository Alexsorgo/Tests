from selenium.webdriver.common.by import By

from screens.base_screen import BaseScreen
from utils.logs import log


class ChannelsListScreen(BaseScreen):
    CHANNELS_CELL = (By.ID, 'chatList_cell')

    def get_channel_count(self):
        log.debug('Get channels counter')
        groups = self.driver.find_elements(*self.CHANNELS_CELL)
        return len(groups)

    def open_channel(self, name):
        log.debug("Go to channel: '{}'".format(name))
        self.driver.find_element_by_id(name).click()

    def open_first_channel(self):
        log.debug('Open first channel from list')
        self.el.tap_btn(self.CHANNELS_CELL)
