from time import sleep

from selenium.webdriver.common.by import By

from screens.chats.base_chat_screen import BaseChatScreen
from utils.logs import log


class CameraScreen(BaseChatScreen):
    TAKE_PHOTO = (By.ID, 'btn take photo default')
    CHANGE_CAMERA = (By.ID, 'ic change camera ios')
    VIDEO_CAMERA = (By.ID, 'Video')
    PHOTO_CAMERA = (By.ID, 'Photo')
    SEND_PHOTO = (By.ID, 'ic forward send icon')
    RETAKE = (By.ID, 'Retake')
    TAKE_VIDEO = (By.ID, 'btn record default')
    STOP_VIDEO = (By.ID, 'btn recording')
    ACCEPT_PHOTO = (By.ID, 'ic edit done')

    def tap_take_photo(self):
        log.debug("Tap '{}' button".format("Take photo"))
        self.el.click_btn(self.TAKE_PHOTO)

    def tap_change_camera(self):
        log.debug("Tap '{}' button".format("Change camera"))
        self.el.click_btn(self.CHANGE_CAMERA)

    def tap_video_camera(self):
        log.debug("Tap '{}' button".format("Video"))
        self.el.click_btn(self.VIDEO_CAMERA)

    def tap_photo_camera(self):
        log.debug("Tap '{}' button".format("Photo"))
        self.el.click_btn(self.PHOTO_CAMERA)

    def tap_send_button(self):
        log.debug("Tap '{}' button".format("Use photo"))
        self.el.click_btn(self.SEND_PHOTO)

    def tap_retake(self):
        log.debug("Tap '{}' button".format("Retake photo"))
        self.el.click_btn(self.RETAKE)

    def record_video(self):
        log.debug("Tap '{}' button".format("Record video"))
        self.el.click_btn(self.TAKE_VIDEO)
        sleep(5)
        self.el.click_btn(self.STOP_VIDEO)
        
    def tap_accept_photo(self):
        log.debug('Tap accept photo')
        self.el.tap_btn(self.ACCEPT_PHOTO)
