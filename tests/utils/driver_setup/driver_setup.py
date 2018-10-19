from tests.utils.driver_setup.custom_selenium_actions import CustomActions
from tests.utils import EventListener


class Drivers:

    @staticmethod
    def create_mobile(appium_server, desired_caps):
        from appium.webdriver import Remote
        return CustomActions(Remote(appium_server, desired_caps), EventListener())
