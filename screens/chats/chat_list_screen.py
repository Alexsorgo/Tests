from selenium.webdriver.common.by import By

from screens.chats.base_chat_screen import BaseChatScreen


class ChatListScreen(BaseChatScreen):
    CHAT_LIST = (By.ID, 'chatList_cell')
    CHAT_NAME = (By.ID, 'chat_name')

    def tap_user(self, fullname):
        user_list = self.driver.find_elements(*self.CHAT_NAME)
        for user in user_list:
            if fullname == user.get_attribute('value'):
                self.el.tap_element(user)
                break
