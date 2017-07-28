# -*- coding: utf-8 -*-

import unittest
import os

from appium import webdriver

from deposits.dep_open import dep_open


class Rules(unittest.TestCase):

    mfo = '305299'
    cardno = '4029619999999937'
    name = 'Ivanov'
    inn = '2498510800'
    accno = '26200603301352'

    def setUp(self):
        # set up appium
        app = os.path.abspath('/Users/admin/Desktop/Pivdenny/otp.ipa')
        # app = os.path.abspath('/Users/admin/Library/Developer/Xcode/DerivedData/OTP-eysunpmsnvqlhdhcadsjutuavvpc/Build/Products/Debug-iphonesimulator/OTP.app')
        self.driver = webdriver.Remote(
            command_executor='http://0.0.0.0:4723/wd/hub',
            desired_capabilities={
                'bundleId': 'ua.com.csltd.phone.otp',
                # 'app': app,
                'appium-version': '1.6.3',
                'platformName': 'iOS',
                'platformVersion': '10.1.1',
                'deviceName': "Alexandr Pogulyaka’s iPad",
                # 'deviceName': 'iPhone 7 Plus',
                'udid': 'cd31170244fc70f532ea362e9ecab74deb579ed6',
                'launchTimeout': 500000,
                # 'automationName': 'XCUITest',
                'realDeviceLogger': '/usr/local/lib/node_modules/deviceconsole/deviceconsole',
                "useNewWDA": True,
                'unicodeKeyboard': True
            })

    def tearDown(self):
        self.driver.quit()

    # Нет прав на вход в систему
    def test_14(self):
        dep_open(self)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Rules)
    unittest.TextTestRunner(verbosity=2).run(suite)
