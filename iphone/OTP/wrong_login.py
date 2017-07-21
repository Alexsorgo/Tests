# -*- coding: utf-8 -*-
import os


def custom_login(self, login, passw, lang):
    # lang = 0
    try:
        self.driver.implicitly_wait(10)
        log = self.driver.find_element_by_xpath(
            '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeSecureTextField')

        if lang == 0:
            log.clear()
            log.send_keys(login)
            pas = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeSecureTextField')
            pas.send_keys(passw)
            self.driver.find_element_by_id('Next:').click()
            # self.driver.find_element_by_id('Next').click()
            self.assertTrue(self.driver.find_element_by_id(
                "It is impossible to login. Check if the login and password are correct."))
            return lang
        elif lang == 1:
            log.clear()
            log.send_keys(login)
            pas = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeSecureTextField')
            pas.send_keys(passw)
            self.driver.find_element_by_id('Next:').click()
            # self.driver.find_element_by_id('Далее').click()
            self.assertTrue(self.driver.find_element_by_id(
                "Подключение к системе невозможно. Проверьте корректность логина и пароля."))
            return lang
        elif lang == 2:
            log.clear()
            log.send_keys(login)
            pas = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeSecureTextField')
            pas.send_keys(passw)
            self.driver.find_element_by_id('Next:').click()
            # self.driver.find_element_by_id('Далі').click()
            self.assertTrue(self.driver.find_element_by_id(
                'Підключення до системи неможливе. Перевірте коректність логіна і паролю.'))
            return lang
        else:
            directory = '%s/' % os.getcwd()
            file_name = 'login_error.png'
            self.driver.save_screenshot(directory + file_name)
            raise
    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'custom_login_error.png'
        self.driver.save_screenshot(directory + file_name)
        raise