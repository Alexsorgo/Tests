from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from screens.base_screen import BaseScreen
from utils.logs import log


class ContactScreen(BaseScreen):
    CONTACT_CELL = (By.ID, 'contact_cell')
    CONTACT_NAME = (By.ID, 'name_label')

    def tap_contact(self, name):
        log.debug("Tap contact '{}'".format(name))
        contacts = self.driver.find_elements(*self.CONTACT_CELL)
        for element in contacts:
            if element.find_element(*self.CONTACT_NAME).get_attribute('value') == name:
                self.el.tap_element(element)
                break
        else:
            log.error("No {} in the list".format(name))
            raise NoSuchElementException
