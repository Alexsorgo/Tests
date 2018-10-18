from selenium.webdriver.common.by import By

from screens.chats.base_chat_screen import BaseChatScreen
from utils.logs import log


class SearchScreen(BaseChatScreen):
    SEARCH_RESULT = (By.ID, 'chatList_cell')
    NO_SEARCH_RESULT = (By.ID, 'Sorry, no search result')

    CHAT_NAME = (By.ID, 'chat_name')

    def is_result_displayed(self, fullname):
        log.debug("Find p2p chat")
        search_result_cells = self.driver.find_elements(*self.SEARCH_RESULT)
        if len(search_result_cells) == 1 and search_result_cells[0].find_element(*self.CHAT_NAME)\
                .get_attribute('value') == fullname:
            return True
        else:
            return False

    def is_no_result_displayed(self):
        log.debug("Sorry, no search result")
        return self.driver.wait_till_element_is_displayed(self. NO_SEARCH_RESULT)
