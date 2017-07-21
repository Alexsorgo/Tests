# -*- coding: utf-8 -*-
import unittest
import os

from appium import webdriver

import constants
from accounts_cards.account_active import account_active
from accounts_cards.accounts_cards_rule13 import accounts_cards_rule13
from accounts_cards.accounts_mask import accounts_mask
from accounts_cards.cards_active import cards_active
from accounts_cards.cards_disable import cards_disable
from callback.in_login import in_login
from callback.main_login import main_login
from deposits.dep_save import dep_save
from login_planshet import login_planshet
from messages.mess_limit import mess_limit
from messages.new_mess import new_mess
from negative.neg_balance import neg_balance
from negative.neg_a2a import wrong_sms
from rules.block import block
from rules.no_auth import no_auth
from rules.rule_17 import rule_17
from rules.rule_17and18 import rule_17and18
from rules.rule_18 import rule_18
from rules.rule_20 import rule_20
from rules.rule_23 import rule_23
from rules.rule_24 import rule_24
from rules.rule_46 import rule_46
from rules.rule_82 import rule_82
from settings.busy_log import busy_log
from settings.change_psw import change_psw
from settings.dif_psw import dif_psw
from settings.empty_psw import empty_psw
from settings.latin_log import latin_log
from settings.latin_psw import latin_psw
from settings.same_log import same_log
from settings.same_psw import same_psw
from settings.space_psw import space_psw
from settings.validation_log import validation_log
from transfers.A2A import a2a
from transfers.A2C import a2c
from transfers.C2A import c2a
from transfers.C2C import c2c
from transfers.bank_card import bank_card
from transfers.bank_schet import bank_schet
from transfers.ukraine_card import ukraine_card
from transfers.ukraine_schet import ukraine_schet

login = constants.login
password = constants.password
valuta = constants.valuta
ukraine_mfo = constants.ukraine_mfo
ukraine_inn = constants.ukraine_inn
ukraine_accno = constants.ukraine_accno
bank_accno = constants.bank_accno
bank_inn = constants.bank_inn
name = constants.name


class Iphonerules(unittest.TestCase):

    # mfo = '305299'
    # cardno = '4029619999999937'
    # name = 'Ivanov'
    # inn = '2498510800'
    # accno = '26200603301352'

    def setUp(self):
        # set up appium
        # app = os.path.abspath('/Users/admin/Library/Developer/Xcode/DerivedData/OTP-eysunpmsnvqlhdhcadsjutuavvpc/Build/Products/Debug-iphoneos/OTP.app')
        app = os.path.abspath('/Users/admin/Library/Developer/Xcode/DerivedData/OTP-eysunpmsnvqlhdhcadsjutuavvpc/Build/Products/Debug-iphonesimulator/OTP.app')
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

    # IFMOB-612:Проверка входа при корректных значениях
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
        # login_phone(self, login, password, lang))
        login_planshet(self, login, password, lang)
        self.assertTrue(self.assertTrue(self.driver.find_element_by_id(
                'navigationTitleIcon')))


    # IFMOB-613:Проверка ввода при некорректных значениях
    def test_02(self):
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
        login_planshet(self, login, password + '4', lang)
        if lang == 0:
            self.assertTrue(self.driver.find_element_by_id(
                "It is impossible to login. Check if the login and password are correct."))
        elif lang == 1:
            self.assertTrue(self.driver.find_element_by_id(
                "Подключение к системе невозможно. Проверьте корректность логина и пароля."))
        elif lang == 2:
            self.assertTrue(self.driver.find_element_by_id(
                'Підключення до системи неможливе. Перевірте коректність логіна і паролю.'))
        else:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_02.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # IFMOB-614:Проверка входа в систему в разным уровнем регистра логина пользователя
    def test_03(self):
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
        combine = ''
        i = 0
        while i < len(login):
            if i % 2 == 1:
                combine += login[i].upper()
            else:
                combine += login[i]
            i += 1
        login_planshet(self, combine, password, lang)
        try:
            self.assertTrue(self.driver.find_element_by_id(
                'navigationTitleIcon'))
        except:
            directory = '%s/' % os.getcwd()
            file_name = 'test_03.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # IFMOB-2615:Проверка отображения / сокрытия символов в полях ввода
    # def test_04(self):
    #     symbols(self)

    # Нет прав на вход в систему
    # IFMOB-623:Вход в систему
    def test_14(self):
        no_auth(self, login, password)

    # Нет прав на работу с внешними интерфейсами
    # IFMOB-624:Работа с внешними интерфейсами / Интерфейсы WinMobile
    def test_15(self):
        rule_20(self, login, password)

    # Пользователь заблокирован
    # IFMOB-615:Проверка входа заблокированным пользователем
    def test_16(self):
        block(self, login, password)

    # Нет прав на работу с нац валютой
    # IFMOB-627:Работа с документами в нац. валюте
    def test_17(self):
        rule_17(self, login, password)

    # Нет прав на работу с валютными документами
    # IFMOB-628:Работа с валютными документами
    def test_18(self):
        rule_18(self, login, password)

    # Нет прав на Депозиты
    # IFMOB-630:Просмотр информации по депозитам
    def test_19(self):
        rule_24(self, login, password)

    # Нет прав на Кредиты
    # IFMOB-629:Просмотр информации по кредитам
    def test_20(self):
        rule_23(self, login, password)

    # Нет прав на платежи (выключенны оба права на работу с документами)
    # IFMOB-628:Работа с валютными документами (п.2)
    def test_21(self):
        rule_17and18(self, login, password)

    # Нет прав на Карты
    # IFMOB-632:Подсистема платежных карт
    def test_22(self):
        rule_46(self, login, password)

    # Нет права на открытие депозита
    # IFMOB-631:Право на открытие депозита
    def test_23(self):
        rule_82(self, login, password)

    # IFMOB-2830:Заказ звонка после получения ошибки "BAD_USER_PASSWORD"
    def test_24(self):
        in_login(self, login, password)

    # IFMOB-2833:Заказ звонка на сейчас при переходе из бокового меню "Звонок в банк" в авторизованном режиме
    def test_25(self):
        main_login(self)

    # IFMOB-641:Права на счета-"Счет доступен"
    def test_26(self):
        accounts_cards_rule13(self, login, password)

    # IFMOB-640:Отображения счетов в зависимости от маски
    def test_27(self):
        accounts_mask(self, login, password)

    # IFMOB-664:Отображение карт на брифе и разделе "Карты"
    # IFMOB-665:Маскирование номера карты
    def test_28(self):
        cards_active(self, login, password)

    # IFMOB-639:Отображение не активных счетов.
    def test_29(self):
        account_active(self, login, password)

    # IFMOB-666:Отображение карт при установленном праве "Подсистема платежных карт"
    def test_30(self):
        cards_disable(self, login, password)

    # IFMOB-740:Списание с карты на карту
    def test_31(self):
        c2c(self, login, password)

    # IFMOB-737:Списание со счета на счет
    def test_32(self):
        a2a(self, login, password)

    # IFMOB-739:Списание с карты на счет
    def test_33(self):
        c2a(self, login, password)

    # IFMOB-738:Списание со счета на карту
    def test_34(self):
        a2c(self, login, password)

    # IFMOB-744:Списание с карты
    def test_35(self):
        bank_card(self, login, password)

    # IFMOB-743:Списание со счета
    def test_36(self):
        bank_schet(self, login, password)

    # IFMOB-748:Списание с карты
    def test_37(self):
        ukraine_card(self, login, password)

    # IFMOB-747:Списание со счета
    def test_38(self):
        ukraine_schet(self, login, password)

    # IFMOB-734:Отправка сообщения без темы/текста сообщения
    def test_39(self):
        new_mess(self, login, password)

    # IFMOB-735:Проверка максимальной длины сообщения
    def test_40(self):
        mess_limit(self, login, password)

    # Смена пароля положительный тест
    def test_41(self):
        change_psw(self, login, password)

    # IFMOB-2625:Пустое поле "Новый пароль"/"Подтверждение"
    def test_42(self):
        empty_psw(self, login, password)

    # IFMOB-2626:Разное значение нового пароля и подтверждения
    def test_43(self):
        dif_psw(self, login, password)

    # IFMOB-2637:Проверка на латиницу
    def test_44(self):
        latin_psw(self, login, password)

    # IFMOB-2628:Проверка на ввод пробела.
    def test_45(self):
        space_psw(self, login, password)

    # IFMOB-2627:Новый пароль равен текущему
    def test_46(self):
        same_psw(self, login, password)

    # IFMOB-2802:Смена логина. Новый логин не идентичен
    def test_47(self):
        busy_log(self, login, password)

    # IFMOB-2638:Валидация полей смены логина
    def test_48(self):
        same_log(self, login, password)

    # IFMOB-2638:Валидация полей смены логина
    def test_49(self):
        latin_log(self, login, password)

    def test_50(self):
        validation_log(self, login, password)

    # Неверный код подтверждения между своими счетами
    def test_51(self):
        wrong_sms(self, login, password)

    # Недостаточно средств на счету
    def test_52(self):
        neg_balance(self, login, password)

    # Открытие сберегательного депозита
    def test_53(self):
        dep_save(self, login, password)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Iphonerules)
    unittest.TextTestRunner(verbosity=2).run(suite)
