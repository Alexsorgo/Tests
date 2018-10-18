from selenium.common.exceptions import (NoAlertPresentException,
                                        StaleElementReferenceException)
from selenium.webdriver.support import expected_conditions as EC


class attribute_presents(object):

    def __init__(self, element, attribute_name, attribute_value):
        self.element = element
        self.attribute = attribute_name
        self.value = attribute_value

    def __call__(self, driver):
        try:
            element_class = EC._find_element(driver, self.element).get_attribute(self.attribute)
            return element_class and self.value in element_class
        except StaleElementReferenceException:
            return False


class alert_is_not_present(object):
    def __call__(self, driver):
        try:
            alert = driver.switch_to.alert
            alert.text
            return False
        except NoAlertPresentException:
            return True
