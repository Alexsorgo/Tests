from selenium.webdriver.common.by import By

from model.element import Element
from utils.logs import log


class KeyboardView:
    EMOJI_BOARD_CHECK = (By.ID, 'FREQUENTLY USED')
    NEXT_KEYBOARD = (By.ID, 'Next keyboard')
    EMOJI = (By.XPATH, '//XCUIElementTypeKey[@name="😊"]')
    STICKER_PREVIEW = (By.ID, 'sticker_image_view')
    STICKER_SEARCH = (By.ID, 'sticker_menu_item_search')

    def __init__(self, driver):
        self.driver = driver
        self.el = Element(self.driver)

    def tap_next_keyboard(self):
        log.debug('Open next keyboard')
        self.el.tap_btn(self.NEXT_KEYBOARD)

    def tap_emoji(self):
        log.debug('Tap emoji')
        self.el.tap_btn(self.EMOJI)

    def open_emoji_keyboard(self):
        log.debug('Open emoji keyboard')
        result = False
        while not result:
            self.tap_next_keyboard()
            result = self.check_emoji_keyboard()

    def check_emoji_keyboard(self):
        log.debug('Check emoji keyboard open')
        return self.driver.wait_till_element_is_displayed(self.EMOJI_BOARD_CHECK, 3)

    def tap_sticker_preview(self):
        log.debug('Tap sticker preview')
        self.el.tap_btn(self.STICKER_PREVIEW)

    def tap_sticker_search(self):
        log.debug('Tap sticker search btn')
        self.el.tap_btn(self.STICKER_SEARCH)

    def get_sticker_preview_count(self):
        log.debug('Check sticker preview count')
        previews = self.driver.find_elements(*self.STICKER_PREVIEW)
        return len(previews)

    def is_sticker_preview_display(self):
        log.debug('Check sticker preview')
        return True if self.driver.find_elements(*self.STICKER_PREVIEW) else False
