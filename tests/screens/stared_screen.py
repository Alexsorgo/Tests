from appium.webdriver.common.touch_action import TouchAction

from tests.model.element import center
from tests.screens.base_screen import BaseScreen
from tests.utils.logs import log


class StarredScreen(BaseScreen):
    STAR_MESSAGE_CELL_ID = 'star_message_cell'
    STAR_MESSAGE_TEXT_ID = 'message_label'
    UNSTAR_ID = 'Unstar'
    CHAT_TITLE = 'name_label'

    def is_starred_message_displayed(self, msg):
        log.debug("Get first starred message name")
        texts = self.driver.find_elements_by_id(self.STAR_MESSAGE_TEXT_ID)
        tx = []
        for i in texts:
            tx.append(i.get_attribute('value'))
        if msg in tx:
            log.debug('{} in {}'.format(msg, tx))
            return True
        else:
            log.debug('{} not in {}'.format(msg, tx))
            return False

    def is_context_option_unstar_displayed(self):
        log.debug('Context menu got unstar option')
        unstar = self.driver.find_elements_by_id(self.UNSTAR_ID)
        if unstar:
            log.debug('Unstar option displayed')
            return True
        else:
            log.debug("Unstar option doesn't display")
            return False

    def open_context(self, msg):
        log.debug('Open context menu on starred message')
        message = self.driver.find_element_by_id(msg)
        action = TouchAction(self.driver)
        action.press(x=center(message)['XCentr'], y=center(message)['YCentr']).wait(1500).release().perform()

    def unstar_message(self, msg):
        log.debug('Tap "{}" button'.format(self.UNSTAR_ID))
        self.open_context(msg)
        self.el.tap_btn_by_id(self.UNSTAR_ID)

    def is_message_star_displayed(self, chat_name, message_name):
        log.debug("Find star voice message")
        cell = self.driver.find_elements_by_id(self.STAR_MESSAGE_CELL_ID)
        if cell[0].find_element_by_id(self.CHAT_TITLE).get_attribute('value') == chat_name and\
           cell[0].find_element_by_id(self.STAR_MESSAGE_TEXT_ID).get_attribute('value') == message_name:
            return True
        else:
            return False
