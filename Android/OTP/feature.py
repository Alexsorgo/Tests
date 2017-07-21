# -*- coding: utf-8 -*-
import getopt
import unittest
import os

import sys
import constants

from appium import webdriver

from size import autologin
from sql.rules import passw_sql, rules, acc_rule13

from sett_msg.psw_change import change_password, login_change
from transfers.rule import rule_24, acc_rule_13, rule_46

login = constants.login
password = constants.password
valuta = constants.valuta


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hl:p:", ["login=", "password="])
    except getopt.GetoptError:
        print """launch.py takes next args:
            -h - help
            -l - login specific user
            -p - password for this user"""
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print """launch.py takes next args:
            -h - help
            -l - login specific user
            -p - password for this user"""
            sys.exit()
        elif opt in ("-l", "--login"):
            global login
            login = arg.upper()
        elif opt in ("-p", "--password"):
            global password
            password = arg


class Rules(unittest.TestCase):
    mfo = '305299'
    cardno = '4029619999999937'
    name = 'Ivanov'
    inn = '2498510800'
    accno = '26200603301352'

    def setUp(self):
        # set up appium
        app = os.path.abspath('/Users/admin/PycharmProjects/PIB/webview/build/Debug-iphoneos/Chimera.app')
        # app = os.path.abspath(
        #     '/Users/admin/Library/Developer/Xcode/DerivedData/OTP-eysunpmsnvqlhdhcadsjutuavvpc/Build/Products/Debug-iphonesimulator/OTP.app')
        self.driver = webdriver.Remote(
            command_executor='http://0.0.0.0:4723/wd/hub',
            desired_capabilities={
                # 'bundleId': 'csltd.Chimera',
                # 'app': app,
                'appium-version': '1.6.5',
                'platformName': 'Android',
                'platformVersion': '7.1.2',
                'deviceName': 'Nexus 5X',
                # 'platformVersion': '6.0.1',
                # 'deviceName': 'Galaxy S5',
                'launchTimeout': 500000,
                'appPackage': 'ua.com.cs.ifobs.mobile.android.otp',
                'appActivity': 'ua.com.cs.ifobs.mobile.android.activity.OtpMainActivity',
                'realDeviceLogger': '/usr/local/lib/node_modules/deviceconsole/deviceconsole',
                'noReset': True,
                'fullReset': False,
                # "useNewWDA": True,
                # 'unicodeKeyboard': False,
            })

    def tearDown(self):
        self.driver.quit()

    # IFMOB-613:Проверка ввода при некорректных значениях
    def test_02(self):
        print login
        print password
        # try:
        #     rules(20)
        #     autologin(self, constants.login, constants.password)
        #     self.driver.switch_to.context('NATIVE_APP')
        #     err = self.driver.find_element_by_id(
        #         "ua.com.cs.ifobs.mobile.android.otp:id/dialogText").get_attribute('text')
        #     self.assertEqual(err, "There is no right to login")
        # except:
        #     self.driver.switch_to.context('NATIVE_APP')
        #     directory = '%s/screenshots/' % os.getcwd()
        #     file_name = 'test_05.png'
        #     self.driver.save_screenshot(directory + file_name)
        #     raise
        # finally:
        #     rules(20)


if __name__ == '__main__':
    main(sys.argv[1:])
    suite = unittest.TestLoader().loadTestsFromTestCase(Rules)
    unittest.TextTestRunner(verbosity=2).run(suite)
