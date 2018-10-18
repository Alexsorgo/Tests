from selenium.webdriver.common.by import By

from screens.chats.base_chat_screen import BaseChatScreen
from utils.logs import log


class LocationScreen(BaseChatScreen):
    CLOSE_LOCATION = (By.ID, 'close_button')
    MAP_MODE = (By.ID, 'ic map mode')
    CURRENT_LOCATION = (By.ID, 'ic map current')
    SEARCH = (By.ID, 'ic map search')
    SEND_LOCATION = (By.ID, 'send')
    MAP_SEARCH_TITLE = 'title_label'

    def tap_close_location(self):
        log.debug("Tap '{}' button".format("Close"))
        self.el.click_btn(self.CLOSE_LOCATION)

    def tap_mode(self):
        log.debug("Tap '{}' button".format("Mode"))
        self.el.click_btn(self.MAP_MODE)

    def tap_current(self):
        log.debug("Tap '{}' button".format("Current location"))
        self.el.click_btn(self.CURRENT_LOCATION)

    def tap_search(self):
        log.debug("Tap '{}' button".format("Search"))
        self.el.click_btn(self.SEARCH)

    def tap_send_location(self):
        log.debug("Tap '{}' button".format("Send"))
        self.el.click_btn(self.SEND_LOCATION)

    def search_and_open_place(self, search_value):
        log.debug("Set place '{}' in search".format(search_value))
        self.el.set_text((By.ID, self.SEARCH_FIELD), search_value)
        titles = self.driver.find_elements_by_id(self.MAP_SEARCH_TITLE)
        for title in titles:
            if title.get_attribute('value') == search_value:
                self.el.tap_element(title)
                break
