from appium.webdriver.common.touch_action import TouchAction
from dateutil import parser
from selenium.common.exceptions import (NoAlertPresentException,
                                        NoSuchElementException,
                                        StaleElementReferenceException,
                                        TimeoutException)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.support.wait import WebDriverWait

from utils.driver_setup.custom_expected_conditions import attribute_presents
from utils.logs import log


class CustomActions(EventFiringWebDriver):

    def is_alert_present(self):
        try:
            return self._driver.switch_to.alert
        except NoAlertPresentException:
            return False

    def accept_alert(self):
        try:
            self._driver.switch_to.alert.accept()
        except NoAlertPresentException:
            return False

    def dismiss_alert(self):
        try:
            alert = self._driver.switch_to.alert
            alert.dismiss()
        except NoAlertPresentException:
            return False

    def wait_till_alert_is_not_displayed(self, timeout=3):
        wait = WebDriverWait(self._driver, timeout=int(timeout), ignored_exceptions=StaleElementReferenceException)
        try:
            return wait.until_not(EC.alert_is_present())
        except NoAlertPresentException:
            return None

    def wait_till_alert_is_displayed(self, timeout=10):
        wait = WebDriverWait(self._driver, timeout=int(timeout), ignored_exceptions=StaleElementReferenceException)
        return wait.until(EC.alert_is_present())

    def wait_till_element_is_not_visible(self, locator, timeout=10):
        wait = WebDriverWait(self._driver, timeout=int(timeout),
                             ignored_exceptions=StaleElementReferenceException)
        return wait.until(EC.invisibility_of_element_located(locator))

    def wait_till_element_is_displayed(self, locator, timeout=10):
        log.debug("Waiting for element")
        wait = WebDriverWait(self._driver, timeout=int(timeout),
                             ignored_exceptions=(StaleElementReferenceException, NoSuchElementException))
        try:
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_till_element_disappear(self, element, timeout=10):
        wait = WebDriverWait(self._driver, timeout=timeout,
                             ignored_exceptions=(StaleElementReferenceException,
                                                 NoSuchElementException,
                                                 TimeoutException))
        try:
            return wait.until_not(EC.presence_of_element_located(element))
        except TimeoutException:
            return None
        except NoSuchElementException:
            return None

    def wait_till_attribute_disappear(self, element, attribute_name, attribute_value, timeout=10):
        wait = WebDriverWait(self._driver, timeout=timeout,
                             ignored_exceptions=(StaleElementReferenceException,
                                                 NoSuchElementException,
                                                 TimeoutException))
        try:
            return wait.until_not(attribute_presents(element, attribute_name, attribute_value))
        except (TimeoutException, NoSuchElementException):
            return None

    def wait_till_element_appears(self, element, timeout=10):
        wait = WebDriverWait(self._driver, timeout=timeout,
                             ignored_exceptions=(StaleElementReferenceException,
                                                 NoSuchElementException,
                                                 TimeoutException))
        try:
            return wait.until(EC.presence_of_element_located(element))
        except TimeoutException:
            return None

    def is_element_clickable(self, locator, timeout=10):
        wait = WebDriverWait(self._driver, timeout=int(timeout),
                             ignored_exceptions=(StaleElementReferenceException, TimeoutException))
        try:
            self.wait_till_element_is_displayed(locator, timeout=10)
        except NoSuchElementException:
            pass
        return wait.until(EC.element_to_be_clickable(locator))

    def wait_till_element_is_not_attached_to_dom(self, web_element, timeout=10):
        """
        Wait until an element is no longer attached to the DOM.
        element is the element to wait for.
        returns False if the element is still attached to the DOM, true otherwise.
        """
        wait = WebDriverWait(self._driver, timeout=int(timeout),
                             ignored_exceptions=(StaleElementReferenceException, NoSuchElementException))
        try:
            wait.until(EC.staleness_of(web_element))
            return True
        except TimeoutException:
            return False

    def scroll_page_to_the_top(self):
        self._driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")

    def scroll_page_to_the_bottom(self):
        self._.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_element(self, web_element):
        self._driver.execute_script("return arguments[0].scrollIntoView();", web_element)

    def wait_till_elements_are_displayed(self, locator, timeout=10):
        wait = WebDriverWait(self._driver, timeout=int(timeout),
                             ignored_exceptions=(StaleElementReferenceException, NoSuchElementException))
        try:
            wait.until(EC.presence_of_all_elements_located(locator))
            return True
        except TimeoutException:
            return False

    def save_screenshot_as_file(self, test_name):
        import os
        from datetime import datetime
        from project_constants import project_path
        current_date = "_" + (datetime.now().strftime("%Y_%m_%d_%H-%M"))
        save_path = os.path.join(project_path, "screenshot_on_fail")
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        self._driver.save_screenshot(os.path.join(save_path, test_name + current_date + ".png"))

    def set_value_in_text_box(self, web_element, text):
        web_element.click()
        web_element.send_keys(text)

    def js_find_element_by_xpath(self, xpath):
        """
        Find element by xpath directly in DOM using 'execute_script'
        :param xpath: xpath string
        :return: web element
        """
        script = """
            var ready = function (fn) {        
                // Sanity check
                if (typeof fn !== 'function') return;

                // If document is already loaded, run method
                if (document.readyState === 'complete') {
                    return fn();
                }            

                // Otherwise, wait until document is loaded
                document.addEventListener('DOMContentLoaded', fn, false);
            };
            return ready(function() {
                return document.evaluate("%s",document,null,9,null).singleNodeValue
            });
        """ % xpath
        return self._driver.execute_script(script)

    def js_find_elements_by_xpath(self, xpath):
        """
        Find elements by xpath directly in DOM using 'execute_script'
        :param xpath: xpath string
        :return: list of web elements
        """
        script = """
        return (function () {
        var xpathToExecute = "%s";
        var result = [];
        var nodesSnapshot = document.evaluate(xpathToExecute, document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
            null );
        for ( var i=0 ; i < nodesSnapshot.snapshotLength; i++ ) { result.push( nodesSnapshot.snapshotItem(i) ); }
        return result;})();
        """ % xpath
        return self._driver.execute_script(script)

    def get_device_datetime(self):
        """Get current time from device and parse to 'datetime' object"""
        return parser.parse(self._driver.execute_script("return new Date().toLocaleString();"))

    def click_element_with_offset(self, element, x_offset=0, y_offset=0):
        """
        :param element: web element to be clicked
        :param x_offset: offset to click on x axis, int
        :param y_offset: offset to click on y axis, int
        """
        actions = ActionChains(self._driver)
        actions.move_to_element_with_offset(element, x_offset, y_offset)
        actions.click()
        actions.perform()

    def swipe_screen(self, start_x, start_y, end_x, end_y, duration=2000):
        """
        Method for swiping screen by coordinates
        :param start_x: x-coordinate at which to start
        :param start_y: y-coordinate at which to start
        :param end_x: x-coordinate at which to stop
        :param end_y: y-coordinate at which to stop
        :param duration: (optional) time to take the swipe, in ms.
        """
        log.debug("Swipe screen from ({0}; {1}) to ({2}; {3}) in time {4}".format(start_x,
                                                                                  start_y, end_x, end_y, duration))
        self._driver.swipe(start_x, start_y, end_x, end_y, duration)

    def get_screen_width(self):
        log.debug("Get Tablet screen width")
        return int(self._driver.execute_script("return window.innerWidth || document.body.clientWidth"))

    def get_screen_height(self):
        log.debug("Get Tablet screen height")
        return int(self._driver.execute_script("return window.innerHeight || document.body.clientHeight"))

    def click_element_using_js(self, element):
        """
        This method to click webelement using JS script
        :param element: web element to be clicked
        """
        log.debug("Click on the element using JS")
        self._driver.execute_script("arguments[0].click();", element)

    def long_press(self, webelem):
        action = TouchAction(self._driver)
        action.long_press(el=webelem, duration=3000).release().perform()
