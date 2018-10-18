from selenium.webdriver.common.by import By

from model.element import Element
from utils.logs import log


class BaseScreen(object):
    BACK_BTN = 'ic back'
    GALLERY = 'Select from Gallery'
    CAMERA = 'Take from Camera'
    CANCEL_BTN = 'close_button'
    SEARCH_FIELD = 'nynja_search_textField_text_view'
    SAVE_BTN = 'save_button'
    DELETE_BTN = 'delete_button'
    USER_TITLE = 'participant_title'

    def __init__(self, driver):
        self.driver = driver
        self.el = Element(self.driver)

    def set_search(self, search_value):
        log.debug("Set '{}' in search".format(search_value))
        self.el.set_text((By.ID, self.SEARCH_FIELD), search_value)

    def tap_search_result(self, search_value):
        log.debug("Tap on '{}' search")
        self.set_search(search_value)
        self.driver.find_element_by_id(search_value).click()

    def tap_cancel_btn(self):
        log.debug("Tap Cancel button")
        self.el.tap_btn_by_id(self.CANCEL_BTN)

    def error_verify(self, err):
        log.debug("Verify '{}' error present".format(err))
        return self.driver.find_element_by_id(err)

    def tap_back(self):
        log.debug("Tap back button")
        self.driver.find_element_by_id(self.BACK_BTN).click()

    def tap_photo_form_gallery(self):
        log.debug("Tap '{}' button on wheel".format(self.GALLERY))
        self.el.tap_btn_by_id(self.GALLERY)

    def tap_photo_form_camera(self):
        log.debug("Tap '{}' button on wheel".format(self.CAMERA))
        self.el.tap_btn_by_id(self.CAMERA)

    def tap_save(self):
        log.debug("Tap Save button")
        self.el.tap_btn_by_id(self.SAVE_BTN)

    def tap_delete(self):
        log.debug("Tap Delete button")
        self.el.tap_btn_by_id(self.DELETE_BTN)

    def airplane_mode(self):
        # TODO: need update in future
        log.debug("Open settings and tap airplane mode")
        self.driver.execute_script('mobile: launchApp', {'bundleId': 'com.apple.Preferences'})
        self.driver.find_elements_by_id('Airplane Mode')[2].click()
        self.driver.launch_app()
