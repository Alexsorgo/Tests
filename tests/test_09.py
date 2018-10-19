# -*- coding: utf-8 -*-
import unittest

from appium import webdriver

import constants
from login_planshet import login_planshet

login = constants.login
password = constants.password
valuta = constants.valuta
ukraine_mfo = constants.ukraine_mfo
ukraine_inn = constants.ukraine_inn
ukraine_accno = constants.ukraine_accno
bank_accno = constants.bank_accno
bank_inn = constants.bank_inn
name = constants.name
platformVersion = constants.iphoneVersion
deviceName = constants.iphoneName
udid = constants.iphoneudid


class Iphonerules(unittest.TestCase):

    def setUp(self):
        # set up appium
        self.driver = webdriver.Remote(
            command_executor='http://0.0.0.0:4723/wd/hub',
            desired_capabilities={
                'bundleId': 'com.nynja.mobile.communicator',
                # 'app': app,
                'appium-version': '1.6.3',
                'platformName': 'iOS',
                'platformVersion': platformVersion,
                'deviceName': deviceName,
                'udid': udid,
                'launchTimeout': 500000,
                # 'automationName': 'XCUITest',
                'realDeviceLogger': '/usr/local/lib/node_modules/deviceconsole/deviceconsole',
                "useNewWDA": True,
                'unicodeKeyboard': True
            })

    def tearDown(self):
        self.driver.quit()

    def test_01(self):
        lang = 0
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
        login_planshet(self, login, password, lang)
        self.assertTrue(self.driver.find_element_by_id(
                'navigationTitleIcon'))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Iphonerules)
    unittest.TextTestRunner(verbosity=2).run(suite)
