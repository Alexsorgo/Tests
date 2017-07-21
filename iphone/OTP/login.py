# -*- coding: utf-8 -*-
import os


def login_phone(self, login, password, lang):
    try:
        self.driver.implicitly_wait(10)
        log = self.driver.find_element_by_xpath(
            '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeSecureTextField')

        if lang == 0:
            log.clear()
            log.send_keys(login)
            pas = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeSecureTextField')
            pas.send_keys(password)
            self.driver.find_element_by_id('Next').click()
            self.assertTrue(self.driver.find_element_by_id(
                'navigationTitleIcon'))
            return lang
        elif lang == 1:
            log.clear()
            log.send_keys(login)
            pas = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeSecureTextField')
            pas.send_keys(password)
            self.driver.find_element_by_id('Далее').click()
            self.assertTrue(self.driver.find_element_by_id(
                'navigationTitleIcon'))
            return lang
        elif lang == 2:
            log.clear()
            log.send_keys(login)
            pas = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeSecureTextField')
            pas.send_keys(password)
            self.driver.find_element_by_id('Далі').click()
            self.assertTrue(self.driver.find_element_by_id(
                'navigationTitleIcon'))
            return lang
    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'login_error.png'
        self.driver.save_screenshot(directory + file_name)
        raise