from selenium.webdriver.common.by import By

from screens.base_screen import BaseScreen
from utils.logs import log


class BaseAddContactScreen(BaseScreen):
    ADD_CONTACT_BTN = (By.ID, 'ADD TO CONTACTS')
    SEARCH = (By.ID, 'SEARCH')
    REQUEST_SENT = (By.XPATH, '//XCUIElementTypeStaticText[@name="Your request has been sent"]')

    def search(self):
        log.debug("Find '{}' button".format("Search"))
        self.driver.find_element(*self.SEARCH)

    def tap_search(self):
        log.debug("Tap '{}' button".format("Search"))
        self.el.click_btn(self.SEARCH)

    def tap_add_contact_btn(self):
        log.debug("Tap '{}' button".format("Add contact"))
        self.el.click_btn(self.ADD_CONTACT_BTN)

    def request_sent_check(self):
        log.debug("Find '{}' text".format("Requested sent"))
        return self.driver.find_element(*self.REQUEST_SENT)
