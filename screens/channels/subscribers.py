from selenium.webdriver.common.by import By

from screens.channels.base_channel_screen import BaseChannelScreen
from utils.logs import log


class SubscribersScreen(BaseChannelScreen):
    SELECT_ALL = (By.ID, 'quantity_button')
    SUBSCRIBERS_CELL = (By.XPATH, '//XCUIElementTypeCell')
    SELECT_CURRENT = (By.ID, 'ic_unchecked')
    NEXT_BTN = (By.ID, 'next_button')

    def select_all(self):
        log.debug("Select all subscribers")
        self.el.tap_btn(self.SELECT_ALL)

    def select_user(self, user):
        log.debug("Select '{}' subscriber".format(str(user)))
        btn = [el.find_element(*self.SELECT_CURRENT) for el in self.driver.find_elements(*self.SUBSCRIBERS_CELL)
               if el.find_element(*(By.ID, self.USER_TITLE)).get_attribute('value') == user]
        self.el.tap_element(btn[0])

    def tap_next_button(self):
        log.debug("Tap next button")
        self.el.tap_btn(self.NEXT_BTN)
