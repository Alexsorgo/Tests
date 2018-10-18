from datetime import datetime

from selenium.common.exceptions import (NoSuchElementException,
                                        StaleElementReferenceException,
                                        TimeoutException)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.events import AbstractEventListener
from selenium.webdriver.support.wait import WebDriverWait

from utils.logs import log


class EventListener(AbstractEventListener):

    def before_find(self, by, value, driver):
        self.start_time = datetime.now()
        wait = WebDriverWait(driver, timeout=15,
                             ignored_exceptions=(StaleElementReferenceException, NoSuchElementException))
        try:
            wait.until(EC.visibility_of_element_located((by, value)))
        except TimeoutException:
            pass

    def after_find(self, by, value, driver):
        self.end_time = (datetime.now() - self.start_time).total_seconds()
        if self.end_time > 5:
            log.warning("ATTENTION! Finding element/elements took more then 5 seconds. Actual time is: {}. "
                        "\nElement: {}. ".format(self.end_time, (by, value)))
