# -*- coding: utf-8 -*-
import getopt
import os
import sys
import unittest
from time import sleep

from appium import webdriver

from logins.logins import invalid_psw
from sett_msg.msg import new_mess, mess_limit
from sett_msg.psw_change import change_password, login_change
from size import autologin
from sql.rules import rules, user_block, acc_rule13, passw_sql
from transfers.own import own, ukraine
import constants
from transfers.rule import rule_17, rule_18, rule_24, rule_23, rule_17and18, rule_46, acc_rule_13, accounts_mask, \
    cards_active

login = constants.login
password = constants.password
valuta = constants.valuta
platformVersion = constants.androidVersion
deviceName = constants.androidName


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hl:p:", ["login=", "password="])
    except getopt.GetoptError:
        print """launch.py takes next args:
            -h - help
            -l - login specific user (default = AUTOTEST)
            -p - password for this user (default = 321)"""
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print """launch.py takes next args:
            -h - help
            -l - login specific user (default = AUTOTEST)
            -p - password for this user (default = 321) """
            sys.exit()
        elif opt in ("-l", "--login"):
            global login
            login = arg.upper()
        elif opt in ("-p", "--password"):
            global password
            password = arg


class Androidrules(unittest.TestCase):

    def setUp(self):
        # set up appium
        # app = os.path.abspath('/Users/admin/PycharmProjects/PIB/webview/build/Debug-iphoneos/Chimera.app')
        # app = os.path.abspath(
        #     '/Users/admin/Library/Developer/Xcode/DerivedData/OTP-eysunpmsnvqlhdhcadsjutuavvpc/Build/Products/Debug-iphonesimulator/OTP.app')
        self.driver = webdriver.Remote(
            command_executor='http://0.0.0.0:4723/wd/hub',
            desired_capabilities={
                # 'app': app,
                'appium-version': '1.6.5',
                'platformName': 'Android',
                'platformVersion': platformVersion,
                'deviceName': deviceName,
                'launchTimeout': 500000,
                'appPackage': 'ua.com.cs.ifobs.mobile.android.otp',
                'appActivity': 'ua.com.cs.ifobs.mobile.android.activity.OtpMainActivity',
                'realDeviceLogger': '/usr/local/lib/node_modules/deviceconsole/deviceconsole',
                'noReset': True,
                'fullReset': False,
                # "useNewWDA": True,
                # 'unicodeKeyboard': True,
            })

    def tearDown(self):
        self.driver.quit()

    # IFMOB-613:Проверка ввода при некорректных значениях
    def test_01(self):
        try:
            self.driver.implicitly_wait(60)
            sleep(10)
            print self.driver.contexts
            invalid_psw(self, login, password)
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_01.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # IFMOB-612:Проверка входа при корректных значениях
    def test_02(self):
        try:
            autologin(self, login, password)
            self.assertTrue(self.driver.find_elements_by_xpath(
                '//*[@class="OtpDashboardMobileBundle-OtpDashboardStyle-logo"]'))
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_02.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # IFMOB-614:Проверка входа в систему в разным уровнем регистра логина пользователя
    def test_03(self):
        try:
            self.driver.implicitly_wait(30)
            combine = ''
            i = 0
            while i < len(login):
                if i % 2 == 1:
                    combine += login[i].upper()
                else:
                    combine += login[i]
                i += 1
            autologin(self, combine, password)
            sleep(7)
            self.assertTrue(self.driver.find_elements_by_xpath(
                '//*[@class="OtpDashboardMobileBundle-OtpDashboardStyle-logo"]'))
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_03.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # Нет прав на вход в систему
    # IFMOB-623:Вход в систему
    def test_04(self):
        try:
            rules(1, login)
            autologin(self, login, password)
            self.driver.switch_to.context('NATIVE_APP')
            err = self.driver.find_element_by_id(
                "ua.com.cs.ifobs.mobile.android.otp:id/dialogText").get_attribute('text')
            self.assertEqual(err, 'No rights to login to the internet bank')
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_04.png'
            self.driver.save_screenshot(directory + file_name)
            raise
        finally:
            rules(1, login)


    def test_05(self):
        try:
            rules(20, login)
            autologin(self, login, password)
            self.driver.switch_to.context('NATIVE_APP')
            err = self.driver.find_element_by_id(
                "ua.com.cs.ifobs.mobile.android.otp:id/dialogText").get_attribute('text')
            self.assertEqual(err, "There is no right to login")
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_05.png'
            self.driver.save_screenshot(directory + file_name)
            raise
        finally:
            rules(20, login)

    # Пользователь заблокирован
    # IFMOB-615:Проверка входа заблокированным пользователем
    def test_06(self):
        try:
            user_block(login)
            autologin(self, login, password)
            self.driver.switch_to.context('NATIVE_APP')
            err = self.driver.find_element_by_id(
                "ua.com.cs.ifobs.mobile.android.otp:id/dialogText").get_attribute('text')
            self.assertEqual(err, "Impossible to complete the operation - This user is blocked. Contact the bank.")
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_06.png'
            self.driver.save_screenshot(directory + file_name)
            raise
        finally:
            user_block(login)

    # Нет прав на работу с нац валютой
    # IFMOB-627:Работа с документами в нац. валюте
    def test_07(self):
        try:
            rules(17, login)
            rule_17(self, login, password)
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_07.png'
            self.driver.save_screenshot(directory + file_name)
            raise
        finally:
            rules(17, login)

    # Нет прав на работу с валютными документами
    # IFMOB-628:Работа с валютными документами
    def test_08(self):
        try:
            rules(18, login)
            rule_18(self, login, password)
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_08.png'
            self.driver.save_screenshot(directory + file_name)
            raise
        finally:
            rules(18, login)

    # Нет прав на Депозиты
    # IFMOB-630:Просмотр информации по депозитам
    def test_09(self):
        try:
            rules(24, login)
            rule_24(self, login, password)
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_09.png'
            self.driver.save_screenshot(directory + file_name)
            raise
        finally:
            rules(24, login)

    # Нет прав на Кредиты
    # IFMOB-629:Просмотр информации по кредитам
    def test_10(self):
        try:
            rules(23, login)
            rule_23(self, login, password)
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_10.png'
            self.driver.save_screenshot(directory + file_name)
            raise
        finally:
            rules(23, login)

    # Нет прав на платежи (выключенны оба права на работу с документами)
    # IFMOB-628:Работа с валютными документами (п.2)
    def test_11(self):
        try:
            rules(18, login)
            rules(17, login)
            rule_17and18(self, login, password)
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_11.png'
            self.driver.save_screenshot(directory + file_name)
            raise
        finally:
            rules(18, login)
            rules(17, login)

    # Нет прав на Карты
    # IFMOB-632:Подсистема платежных карт
    def test_12(self):
        try:
            rules(46, login)
            rule_46(self, login, password)
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_12.png'
            self.driver.save_screenshot(directory + file_name)
            raise
        finally:
            rules(46, login)

    # IFMOB-641:Права на счета-"Счет доступен"
    def test_13(self):
        try:
            acc_rule_13(self, login, password)
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_13.png'
            self.driver.save_screenshot(directory + file_name)
            raise
        finally:
            acc_rule13(login)

    # IFMOB-640:Отображения счетов в зависимости от маски
    def test_14(self):
        try:
            accounts_mask(self, login, password)
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_14.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # IFMOB-664:Отображение карт на брифе и разделе "Карты"
    # IFMOB-665:Маскирование номера карты
    def test_15(self):
        try:
            cards_active(self, login, password)
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_15.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # IFMOB-666:Отображение карт при установленном праве "Подсистема платежных карт"
    def test_16(self):
        try:
            rules(46, login)
            rule_46(self, login, password)
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_16.png'
            self.driver.save_screenshot(directory + file_name)
            raise
        finally:
            rules(46, login)

    # IFMOB-740:Списание с карты на карту
    def test_17(self):
        try:
            own(self, login, password, valuta, 'c2c')
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_17.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # IFMOB-739:Списание с карты на счет
    def test_18(self):
        try:
            own(self, login, password, valuta, 'c2a')
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_18.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # IFMOB-737:Списание со счета на счет
    def test_19(self):
        try:
            own(self, login, password, valuta, 'a2a')
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_19.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # IFMOB-738:Списание со счета на карту
    def test_20(self):
        try:
            own(self, login, password, valuta, 'a2c')
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_20.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # IFMOB-748:Списание с карты
    def test_21(self):
        try:
            ukraine(self, login, password, valuta, 'c2u')
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_21.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # IFMOB-747:Списание со счета
    def test_22(self):
        try:
            ukraine(self, login, password, valuta, 'a2u')
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_22.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # IFMOB-734:Отправка сообщения без темы/текста сообщения
    def test_23(self):
        try:
            new_mess(self, login, password)
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_23.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # IFMOB-735:Проверка максимальной длины сообщения
    def test_24(self):
        try:
            mess_limit(self, login, password)
        except:

            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_24.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # Смена пароля положительный тест
    def test_25(self):
        try:
            change_password(self, login, password, constants.new_pass, constants.conf_pass,
                            'positive')
        except:

            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_25.png'
            self.driver.save_screenshot(directory + file_name)
            raise
        finally:
            passw_sql(login)

    # IFMOB-2625:Пустое поле "Новый пароль"/"Подтверждение"
    def test_26(self):
        change_password(self, login, password, '', '',
                        'empty')

    # IFMOB-2626:Разное значение нового пароля и подтверждения
    def test_27(self):
        try:
            change_password(self, login, password, constants.new_pass, constants.conf_pass + '4',
                            'different')
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_27.png'
            self.driver.save_screenshot(directory + file_name)
            raise
        finally:
            passw_sql(login)

    # # IFMOB-2637:Проверка на латиницу
    # def test_28(self):
    #     change_password(self, login, password, 'Привет', 'Привет',
    #                     'latin')


    # IFMOB-2628:Проверка на ввод пробела.
    def test_29(self):
        try:
            change_password(self, login, password, '12 3', '12 3',
                            'space')
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_29.png'
            self.driver.save_screenshot(directory + file_name)
            raise
        finally:
            passw_sql(login)

    # IFMOB-2627:Новый пароль равен текущему
    def test_30(self):
        try:
            change_password(self, login, password, password, password,
                            'same')
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_30.png'
            self.driver.save_screenshot(directory + file_name)
            raise
        finally:
            passw_sql(login)

    # IFMOB-2802:Смена логина. Новый логин не идентичен
    def test_31(self):
        try:
            login_change(self, login, password, constants.busy_log, constants.busy_log,
                         'busy')
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_31.png'
            self.driver.save_screenshot(directory + file_name)
            raise


    # IFMOB-2638:Валидация полей смены логина
    def test_32(self):
        try:
            login_change(self, login, password, login, login,
                         'same')
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_32.png'
            self.driver.save_screenshot(directory + file_name)
            raise


    # IFMOB-2638:Валидация полей смены логина
    # Проверка на < 6 символов и ввод недопустимых символов (.+)
    def test_33(self):
        try:
            login_change(self, login, password, login, login,
                         'validation')
        except:
            self.driver.switch_to.context('NATIVE_APP')
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_32.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # # Открытие депозита
    # def test_34(self):


if __name__ == '__main__':
    main(sys.argv[1:])
    suite = unittest.TestLoader().loadTestsFromTestCase(Androidrules)
    unittest.TextTestRunner(verbosity=2).run(suite)
