from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from model.element import center, proportion
from screens.base_screen import BaseScreen
from utils.logs import log


class HomeScreen(BaseScreen):
    QR = (By.ID, 'ic qr code')
    WHEEL_BTN = (By.ID, 'btn wheel inactive')
    CONTACT_LIST = (By.ID, 'Go to history')
    ADDED_USER = (By.XPATH, '//XCUIElementTypeStaticText[@name="Added"]')
    AVATAR_PLACEHOLDER = (By.ID, 'profile_details_view_placeholder_image')
    AVATAR_DOWNLOADED = (By.ID, 'profile_details_view_loaded_image')
    CHAT_LIST = (By.ID, 'message_cell')
    STARRED_SECTION = 'star_footer_action_button'
    STARRED_MSGS = 'star_star_message_cell'
    STARRED_MSGS_TEXT = 'message_label'
    SCHEDULE_MESSAGE_CELL = 'schedule_profile_scheduled_message_cell'

    def tap_wheel_btn(self):
        log.debug("Tap '{}' button".format("Wheel"))
        self.el.click_btn(self.WHEEL_BTN)

    def tap_avatar(self):
        log.debug("Tap '{}' button".format("Avatar"))
        self.el.click_btn(self.AVATAR_DOWNLOADED)

    def close_avatar(self):
        log.debug('Swipe up')
        el = self.driver.find_element_by_xpath('//XCUIElementTypeApplication')
        action = TouchAction(self.driver)
        swipe_start = proportion(240, 655, self.driver.get_window_size()['width'],
                                 self.driver.get_window_size()['height'])

        swipe_end = proportion(360, 575, self.driver.get_window_size()['width'],
                               self.driver.get_window_size()['height'])

        action.press(el, swipe_start['x'], swipe_start['y']).wait(100).move_to(el, swipe_end['x'],
                                                                               swipe_end['y']).release()
        action.perform()

    def long_press_wheel_btn(self):
        log.debug("Long press '{}' button to go home page".format("Wheel"))
        wh = self.driver.find_element(*self.WHEEL_BTN)
        action = TouchAction(self.driver)
        action.long_press(x=center(wh)['XCentr'], y=center(wh)['YCentr'], duration=3000).release().perform()

    def tap_contact_list(self):
        log.debug("Tap '{}' view".format("Contact"))
        self.el.tap_btn(self.CONTACT_LIST)

    def tap_stared_msg(self, msg_text):
        log.debug("Scroll to '{}' section".format("Stared"))
        self.scroll_down()
        log.debug("Tap starred message: '{}'".format(msg_text))
        texts_elements = self.driver.find_elements_by_id(self.STARRED_MSGS_TEXT)
        for elem in texts_elements:
            if elem.get_attribute('value') == msg_text:
                self.el.tap_element(elem)

    def is_home_screen_displayed(self):
        log.debug("Wait till Home Screen is displayed")
        return self.driver.wait_till_element_is_displayed(self.QR, timeout=7)

    def is_profile_updated(self, locator):
        log.debug("Find updated profile element")
        return self.driver.wait_till_element_is_displayed((By.ID, locator))

    def is_avatar_updated(self):
        log.debug("Find avatar photo")
        return self.driver.wait_till_element_is_displayed(self.AVATAR_DOWNLOADED)

    def scroll_down(self):
        el = self.driver.find_element_by_xpath('//XCUIElementTypeApplication')
        action = TouchAction(self.driver)
        swipe_start = proportion(240, 655, self.driver.get_window_size()['width'],
                                 self.driver.get_window_size()['height'])

        swipe_end = proportion(360, 575, self.driver.get_window_size()['width'],
                               self.driver.get_window_size()['height'])

        action.press(el, swipe_start['x'], swipe_start['y']).wait(100).move_to(el, swipe_end['x'],
                                                                               swipe_end['y']).release()
        action.perform()

    def open_starred_section(self):
        log.debug("Scroll and tap to '{}' section".format("Stared"))
        self.scroll_down()
        msg = self.driver.find_element_by_id(self.STARRED_SECTION)
        msg.click()

    def is_starred_displayed(self, msg):
        log.debug('Check is starred message displayed')
        self.scroll_down()
        texts_elements = self.driver.find_elements_by_id(self.STARRED_MSGS_TEXT)
        texts = []
        for cell in texts_elements:
            texts.append(cell.get_attribute('value'))
        if msg in texts:
            return True
        else:
            return False

    def is_schedule_display(self, msg):
        log.debug('Check "{}" message scheduled'.format(msg))
        self.scroll_down()
        sched_msgs = self.driver.find_elements_by_id(self.SCHEDULE_MESSAGE_CELL)
        last_sched_texts = sched_msgs[0].find_elements_by_xpath('//XCUIElementTypeStaticText')
        texts = []
        for text in last_sched_texts:
            texts.append(text.get_attribute('value'))
        print(texts)
        if msg in texts:
            return True
        else:
            return False

