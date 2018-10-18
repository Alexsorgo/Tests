from selenium.webdriver.common.by import By

from screens.base_screen import BaseScreen
from utils.logs import log


class GroupListScreen(BaseScreen):
    GROUPS_CELL = (By.ID, 'chatList_cell')

    def get_group_count(self):
        log.debug('Get groups counter')
        groups = self.driver.find_elements(*self.GROUPS_CELL)
        return len(groups)

    def open_group_chat(self, name):
        log.debug("Go to group chat: '{}'".format(name))
        self.driver.find_element_by_id(name).click()

    def open_first_group(self):
        log.debug('Open first group chat from list')
        self.el.tap_btn(self.GROUPS_CELL)
