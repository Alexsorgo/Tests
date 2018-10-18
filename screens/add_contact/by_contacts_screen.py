from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from screens.contact_screen import ContactScreen
from utils.logs import log


class ByContactsScreen(ContactScreen):
    CONTACT_USERNAME_FIELD = (By.ID, 'username_field_input')
    ADD_BTN = (By.ID, 'Add')
    REQUESTED = (By.ID, 'Requested')

    def tap_add_contact(self, name):
        log.debug("Send friend request to: '{}'".format(name))
        new_cont_list = self.driver.find_elements(*self.CONTACT_CELL)
        for element in new_cont_list:
            if element.find_element(*self.CONTACT_NAME).get_attribute('value') == name:
                self.el.tap_btn(self.ADD_BTN)
                break
        else:
            log.error("No {} in the list".format(name))
            raise NoSuchElementException

    def requested_check(self):
        log.debug("Find '{}' button".format("Requested"))
        return self.driver.find_element(*self.REQUESTED)
