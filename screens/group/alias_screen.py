from selenium.webdriver.common.by import By

from screens.chats.base_chat_screen import BaseChatScreen
from utils.logs import log


class AliasScreen(BaseChatScreen):
    ALIAS_FIELD = (By.ID, 'alias_field_input')
    ALIAS_CANCEL = (By.ID, 'cancel_button')
    ALIAS_SAVE = (By.ID, 'save_button')
    ALIAS_SCREEN = (By.ID, 'MY GROUP ALIAS')

    def set_alias(self, alias):
        log.debug('Set alias: "{}"'.format(alias))
        self.el.set_text_clear(self.ALIAS_FIELD, alias)
        self.save_alias()

    def cancel_alias(self):
        log.debug('Cancel alias changes')
        self.driver.find_element(*self.ALIAS_CANCEL).click()

    def save_alias(self):
        log.debug('Tap save alias button')
        self.driver.find_element(*self.ALIAS_SAVE).click()

    def is_alias_screen(self):
        log.debug("Alias screen displayed")
        alias_screen = self.driver.find_elements(*self.ALIAS_SCREEN)
        if alias_screen:
            return True
        else:
            return False
