from selenium.webdriver.common.by import By

from screens.chats.base_chat_screen import BaseChatScreen
from utils.logs import log


class StorageScreen(BaseChatScreen):
    IMAGE_CELL = (By.ID, 'storage_image_cell')
    FILES = (By.ID, 'FILES')
    PHOTOS = (By.ID, 'PHOTOS')
    VIDEOS = (By.ID, 'VIDEOS')
    FILE_CELL = (By.ID, 'storage_file_cell')

    def tap_files(self):
        log.debug('Tap files in filter')
        self.el.tap_btn(self.FILES)

    def get_count_images(self, before=0):
        log.debug('Collect all images in chat')
        if self.driver.wait_till_element_is_displayed(self.IMAGE_CELL, 3):
            image_boxes = self.driver.find_elements(*self.IMAGE_CELL)
            log.debug('Collected "{}" images'.format(str(len(image_boxes))))
            actual = len(image_boxes) - before
            return actual
        return 0

    def get_sent_files_count(self, before=0):
        log.debug('Collect all files in chat')
        self.tap_files()
        if self.driver.wait_till_element_is_displayed(self.FILE_CELL, 3):
            file_boxes = self.driver.find_elements(*self.FILE_CELL)
            log.debug('Collected "{}" files'.format(str(len(file_boxes))))
            actual = len(file_boxes) - before
            return actual
        return 0
