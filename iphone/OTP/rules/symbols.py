# -*- coding: utf-8 -*-
import os


def symbols(self):
    lang = 0
    valid_login = 'AUTOTEST'
    valid_pass = '321'
    while lang < 3:
        try:
            if lang == 0:
                self.driver.find_element_by_id('Remember login?')
            elif lang == 1:
                self.driver.find_element_by_id('Запомнить логин?')
            elif lang == 2:
                self.driver.find_element_by_id("Запам'ятати логін?")
            break
        except:
            lang += 1
    try:
        self.driver.implicitly_wait(10)
        log = self.driver.find_element_by_xpath(
            '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeSecureTextField')

        if lang == 0:
            log.clear()
            log.send_keys(valid_login)
            pas = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeSecureTextField')
            pas.send_keys(valid_pass)
            crypt_log = log.get_attribute('Value')
            self.assertEqual(crypt_log, u'••••••••')
            crypt_pas = pas.get_attribute('Value')
            self.assertEqual(crypt_pas, u'•••')
            log_icon = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeButton')
            log_icon.click()
            pasw_icon = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeButton[2]')
            pasw_icon.click()
            ucrypt_log = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeTextField').get_attribute(
                'Value')
            ucrypt_pas = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField').get_attribute(
                'Value')
            self.assertEqual(ucrypt_log, 'AUTOTEST')
            self.assertEqual(ucrypt_pas, '321')

        elif lang == 1:
            log.clear()
            log.send_keys(valid_login)
            pas = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeSecureTextField')
            pas.send_keys(valid_pass)
            crypt_log = log.get_attribute('Value')
            self.assertEqual(crypt_log, u'••••••••')
            crypt_pas = pas.get_attribute('Value')
            self.assertEqual(crypt_pas, u'•••')
            log_icon = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeButton')
            log_icon.click()
            pasw_icon = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeButton[2]')
            pasw_icon.click()
            ucrypt_log = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeTextField').get_attribute(
                'Value')
            ucrypt_pas = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField').get_attribute(
                'Value')
            self.assertEqual(ucrypt_log, 'AUTOTEST')
            self.assertEqual(ucrypt_pas, '321')

        elif lang == 2:
            log.clear()
            log.send_keys(valid_login)
            pas = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeSecureTextField')
            pas.send_keys(valid_pass)
            crypt_log = log.get_attribute('Value')
            self.assertEqual(crypt_log, u'••••••••')
            crypt_pas = pas.get_attribute('Value')
            self.assertEqual(crypt_pas, u'•••')
            log_icon = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeButton')
            log_icon.click()
            pasw_icon = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeButton[2]')
            pasw_icon.click()
            ucrypt_log = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeTextField').get_attribute('Value')
            ucrypt_pas = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField').get_attribute('Value')
            self.assertEqual(ucrypt_log, 'AUTOTEST')
            self.assertEqual(ucrypt_pas, '321')

        else:
            directory = '%s/' % os.getcwd()
            file_name = 'test_04.png'
            self.driver.save_screenshot(directory + file_name)
            raise
    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_04.png'
        self.driver.save_screenshot(directory + file_name)
        raise
