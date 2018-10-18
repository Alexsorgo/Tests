from selenium.webdriver.common.by import By

from model.element import Element
from utils.logs import log


class BaseGalleryScreen(object):
    SEND_AS_FILE_ID = 'send_as_file_button'
    SEND_BUTTON_ID = 'send_button'
    CURTAIN_BUTTON_ID = 'collapsed_view_button'
    SELECT_ID = 'counter_indicator_button'

    def __init__(self, driver):
        self.driver = driver
        self.el = Element(self.driver)

    def tap_send_btn(self):
        log.debug('Tap send selected images')
        self.el.tap_btn_by_id(self.SEND_BUTTON_ID)

    def tap_send_as_file(self):
        log.debug('Tap send as file selected images')
        self.el.tap_btn_by_id(self.SEND_AS_FILE_ID)

    def open_curtain(self):
        log.debug('Open curtain')
        self.el.tap_btn_by_id(self.CURTAIN_BUTTON_ID)

    def select_image(self):
        log.debug('Tap select image')
        self.el.tap_btn_by_id(self.SELECT_ID)

    def is_send_as_file_btn_display(self):
        log.debug('Find send as file button')
        return self.driver.wait_till_element_is_displayed((By.ID, self.SEND_BUTTON_ID))
