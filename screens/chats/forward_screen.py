from screens.chats.base_chat_screen import BaseChatScreen
from utils.logs import log


class ForwardScreen(BaseChatScreen):
    FORWARD_CELL = 'forward_cell'
    FORWARD_TITLE = 'participant_title'
    SEND_BTN = 'ic forward send icon'
    SEARCH_BTN = 'ic search'
    P2P_BTN = 'ic forward contacts'
    GROUP_BTN = 'ic forward groups'

    def select_forward(self, name):
        log.debug('Select forward message to: "{}"'.format(name))
        cells = self.driver.find_elements_by_id(self.FORWARD_CELL)
        for cell in cells:
            if cell.find_element_by_id(self.FORWARD_TITLE).get_attribute('value') == name:
                self.el.tap_element(cell)
                break

    def tap_send_btn(self):
        log.debug('Tap send forward message button')
        self.el.tap_btn_by_id(self.SEND_BTN)

    def tap_filter_group(self):
        log.debug('Tap groups in filter')
        self.el.tap_btn_by_id(self.GROUP_BTN)
