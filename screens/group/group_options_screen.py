from appium.webdriver.common.touch_action import TouchAction

from model.element import proportion
from screens.base_screen import BaseScreen
from utils.logs import log


class GroupOptionScreen(BaseScreen):
    GROUP_ALIAS = 'My Alias in Group:'
    GROUP_NAME = 'Group Name*:'
    GROUP_RULES = 'Group Rules'
    NOTIFICATIONS = 'Notifications'
    STORAGE = 'Storage'
    LANGUAGE_SETTINGS = 'Language Settings'
    ADD_PARTICIPANTS = 'Add Participants'
    GROUP_PARTICIPANTS = 'Group Participants'
    DELETE_PARTICIPANTS = 'Delete Participants'
    GROUP_ADMINS = 'Group Admins'
    CLEAR_HISTORY = 'Clear Chat History'
    DELETE_GROUP = 'Delete and Leave'
    RETURN_TO_CHAT = 'Return to Group Chat'
    ALERT_DELETE = 'Delete'

    def open_alias(self):
        log.debug('Open edit alias screen')
        self.el.tap_btn_by_id(self.GROUP_ALIAS)

    def open_group_name(self):
        log.debug('Open edit group name screen')
        self.el.tap_btn_by_id(self.GROUP_NAME)

    def open_group_participants(self):
        log.debug('Open group participants screen')
        self.el.tap_btn_by_id(self.GROUP_PARTICIPANTS)

    def open_group_admins(self):
        log.debug('Open group admins screen')
        self.el.tap_btn_by_id(self.GROUP_ADMINS)

    def delete_and_leave(self):
        log.debug('Tap delete and leave group')
        self.el.tap_btn_by_id(self.DELETE_GROUP)
        self.tap_delete_btn()

    def clear_history(self):
        log.debug('Clear history')
        self.el.tap_btn_by_id(self.CLEAR_HISTORY)
        self.tap_delete_btn()

    def tap_delete_btn(self):
        log.debug('Tap delete on alert')
        self.el.tap_btn_by_id(self.ALERT_DELETE)

    def verify_element(self, el):
        log.debug('Check that alias "{}" displayed'.format(el))
        result = self.driver.find_element_by_id(el)
        if result:
            return True
        else:
            return False

    def swipe_options(self):
        log.debug('Swipe options screen')
        el = self.driver.find_element_by_xpath('//XCUIElementTypeApplication')
        action = TouchAction(self.driver)
        swipe_start = proportion(240, 655, self.driver.get_window_size()['width'],
                                 self.driver.get_window_size()['height'])

        swipe_end = proportion(360, 575, self.driver.get_window_size()['width'],
                               self.driver.get_window_size()['height'])

        action.press(el, swipe_start['x'], swipe_start['y']).wait(100).move_to(el, swipe_end['x'],
                                                                               swipe_end['y']).release()
        action.perform()

    def back_to_chat(self):
        log.debug('Tap "{}" button'.format(self.RETURN_TO_CHAT))
        self.swipe_options()
        self.el.tap_btn_by_id(self.RETURN_TO_CHAT)
