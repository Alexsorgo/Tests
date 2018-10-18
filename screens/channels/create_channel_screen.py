from selenium.webdriver.common.by import By

from screens.channels.base_channel_screen import BaseChannelScreen
from utils.logs import log


class CreateChannelScreen(BaseChannelScreen):
    CHANNEL_NAME = (By.ID, 'name_field')
    CHANNEL_LINK = (By.ID, 'link_field')
    CHANNEL_DESC = (By.ID, 'description_view')
    CREATE_RANDOM_LINK = (By.ID, 'action_button')
    CREATE_BTN = (By.ID, 'create_button')
    CHANNEL_AVATAR = (By.ID, 'image_view')

    def set_channel_name(self, name):
        log.debug("Set channel name: '{}'".format(str(name)))
        self.el.set_text(self.CHANNEL_NAME, name)

    def set_channel_link(self, link):
        log.debug("Set channel link: '{}'".format(str(link)))
        self.el.set_text(self.CHANNEL_LINK, link)

    def set_channel_desc(self, descr):
        log.debug("Set channel description: '{}'".format(str(descr)))
        self.el.set_text(self.CHANNEL_DESC, descr)

    def tap_create_channel(self):
        log.debug("Tap create channel button")
        self.el.tap_btn(self.CREATE_BTN)

    def create_random_link(self):
        log.debug("Generate random link")
        self.el.tap_btn(self.CREATE_RANDOM_LINK)
