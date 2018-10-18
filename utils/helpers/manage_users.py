from controls.menu import Menu
from utils.logs import log


class Manager:

    def __init__(self, driver):
        self.driver = driver
        self.menu = Menu(self.driver)

    def log_out(self):
        log.debug("Perform log out")
        self.menu.go_to(self.menu.wenums.SETTINGS, [self.menu.wenums.LOG_OUT])

    def delete_user(self):
        log.debug("Perform delete user")
        self.menu.go_to(self.menu.wenums.SETTINGS, [self.menu.wenums.LOG_OUT])

    # def log_in(self, phone_number):
    #     log.debug("Perform log in")
    #     from screens.login_screen import LoginScreen
    #     nynja_login_screen = LoginScreen(self.driver)
    #     nynja_login_screen.get_started()
    #     nynja_login_screen.set_phone_num(phone_number)
    #     nynja_login_screen.tap_skip_btn()
    #     nynja_login_screen.tap_confirm_btn()
    #     nynja_login_screen.set_sms()
    #     nynja_home_screen = nynja_login_screen.tap_sms_next_btn()
    #     if nynja_home_screen.is_home_screen_displayed():
    #         return nynja_home_screen
