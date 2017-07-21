# -*- coding: utf-8 -*-
import re
import unittest
import os

import requests
from selenium.common.exceptions import NoSuchElementException
import xml.etree.ElementTree as ET
from hash import decd, enc

from appium import webdriver
from login import login
from time import sleep

from reques.credit import credit_req, cards_req, scheta_req


class Rules(unittest.TestCase):

    mfo = '305299'
    cardno = '4029619999999937'
    name = 'Ivanov'
    inn = '2498510800'

    def setUp(self):
        # set up appium
        app = os.path.abspath('/Users/admin/Desktop/Pivdenny/Pivdenny.ipa')
        # app = os.path.abspath('/Users/admin/Library/Developer/Xcode/DerivedData/Pivdenny-fcnzskefhvzrvxfchcoiershcrfb/Build/Products/Debug-iphonesimulator/Pivdenny.app')
        self.driver = webdriver.Remote(
            command_executor='http://0.0.0.0:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'appium-version': '1.6.3',
                'platformName': 'iOS',
                'platformVersion': '10.0.2',
                # 'deviceName': 'iPhone 7',
                'deviceName': 'iPhone 6s',
                'udid': 'f3b0308a80a4dba925ece9652d9c3159a9af5cb5',
                'launchTimeout': 500000,
                # 'automationName': 'XCUITest'
            })

    def tearDown(self):
        self.driver.quit()

    # Нет прав на вход в систему
    def test_14(self):
        try:
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
            try:
                login(self, lang)
            except NoSuchElementException:
                pass
            if lang == 0:
                self.assertTrue(self.driver.find_element_by_id("No rights to login to the internet bank"))
            elif lang == 1:
                self.assertTrue(self.driver.find_element_by_id('Нет права входа в интернет-банк'))
            elif lang == 2:
                self.assertTrue(self.driver.find_element_by_id('Немає права входу до інтернет-банку'))
        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_14.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # Нет прав на работу с внешними интерфейсами
    def test_15(self):
        try:
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
            try:
                login(self, lang)
            except NoSuchElementException:
                pass
            if lang == 0:
                self.assertTrue(
                    self.driver.find_element_by_id("The user doesn't have enough rights to finish the action"))
            elif lang == 1:
                self.assertTrue(
                    self.driver.find_element_by_id('У пользователя недостаточно прав для завершения данного действия'))
            elif lang == 2:
                self.assertTrue(
                    self.driver.find_element_by_id('У користувача недостатньо прав для завершення даної дії'))
        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_15.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # Пользователь заблокирован
    def test_16(self):
        try:
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
            try:
                login(self, lang)
            except NoSuchElementException:
                pass
            if lang == 0:
                self.assertTrue(
                    self.driver.find_element_by_id("The specified user has been blocked. Contact the bank."))
            elif lang == 1:
                self.assertTrue(
                    self.driver.find_element_by_id('Заданный пользователь заблокирован. Обратитесь в банк.'))
            elif lang == 2:
                self.assertTrue(
                    self.driver.find_element_by_id('Зазначеного користувача заблоковано. Зверніться до банку.'))
        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_16.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # Нет прав на работу с нац валютой
    def test_17(self):
        try:
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
            login(self, lang)

            if lang == 0:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Payments')
                bil.click()
                scheta = self.driver.find_element_by_id('Between own accounts')
                scheta.click()
                new_schet = self.driver.find_element_by_id('New')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Pay from')

                spisanie.click()
                sleep(45)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                cur = []
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')
                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        cur.append(re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' '))

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        cur.append(re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' '))
                self.assertTrue('UAH' not in cur)
                print 'UAH' not in cur

                account = self.driver.find_element_by_id('ACCOUNTS')
                account.click()
                sleep(5)
                spisok2 = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                spisok2.remove(spisok2[0])
                print spisok2
                for i in spisok2:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    cur.append(re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' '))
                print 'UAH' not in cur
                self.assertTrue('UAH' not in cur)

            elif lang == 1:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Платежи')
                bil.click()
                scheta = self.driver.find_element_by_id('Между своими счетами')
                scheta.click()
                new_schet = self.driver.find_element_by_id('Новый')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Выберите счет списания')

                spisanie.click()
                sleep(45)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                cur = []
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')
                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        cur.append(re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' '))

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        cur.append(re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' '))
                self.assertTrue('UAH' not in cur)
                print 'UAH' not in cur

                account = self.driver.find_element_by_id('СЧЕТА')
                account.click()
                sleep(5)
                spisok2 = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                spisok2.remove(spisok2[0])
                print spisok2
                for i in spisok2:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    cur.append(re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' '))
                print 'UAH' not in cur
                self.assertTrue('UAH' not in cur)

            elif lang == 2:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Платежі')
                bil.click()
                scheta = self.driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name = 'Між своїми рахунками']")
                scheta.click()
                new_schet = self.driver.find_element_by_id('Новий')
                new_schet.click()
                self.driver.implicitly_wait(30)
                spisanie = self.driver.find_element_by_id('Виберіть рахунок списання')

                spisanie.click()
                sleep(45)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                cur = []
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')
                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        cur.append(re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' '))

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        cur.append(re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' '))
                self.assertTrue('UAH' not in cur)
                print 'UAH' not in cur

                account = self.driver.find_element_by_id('РАХУНКИ')
                account.click()
                sleep(5)
                spisok2 = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                spisok2.remove(spisok2[0])
                print spisok2
                for i in spisok2:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    cur.append(re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' '))
                print 'UAH' not in cur
                self.assertTrue('UAH' not in cur)

        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_17.png'
            self.driver.save_screenshot(directory + file_name)
            raise


    # Нет прав на работу с валютными документами
    def test_18(self):
        try:
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
            login(self, lang)

            if lang == 0:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Payments')
                bil.click()
                scheta = self.driver.find_element_by_id('Between own accounts')
                scheta.click()
                new_schet = self.driver.find_element_by_id('New')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Pay from')

                spisanie.click()
                sleep(45)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')

                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        self.assertTrue(re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH')

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        self.assertTrue(re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH')

                account = self.driver.find_element_by_id('ACCOUNTS')
                account.click()
                sleep(5)
                spisok2 = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                spisok2.remove(spisok2[0])
                print spisok2
                for i in spisok2:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    self.assertTrue(re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH')

            elif lang == 1:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Платежи')
                bil.click()
                scheta = self.driver.find_element_by_id('Между своими счетами')
                scheta.click()
                new_schet = self.driver.find_element_by_id('Новый')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Выберите счет списания')

                spisanie.click()
                sleep(45)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')
                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        self.assertTrue(re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH')

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        self.assertTrue(re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH')

                account = self.driver.find_element_by_id('СЧЕТА')
                account.click()
                sleep(5)
                spisok2 = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                spisok2.remove(spisok2[0])
                print spisok2
                for i in spisok2:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    self.assertTrue(re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH')

            elif lang == 2:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Платежі')
                bil.click()
                scheta = self.driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name = 'Між своїми рахунками']")
                scheta.click()
                new_schet = self.driver.find_element_by_id('Новий')
                new_schet.click()
                self.driver.implicitly_wait(30)
                spisanie = self.driver.find_element_by_id('Виберіть рахунок списання')

                spisanie.click()
                sleep(45)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')
                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        self.assertTrue(re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH')

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        self.assertTrue(re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH')

                account = self.driver.find_element_by_id('РАХУНКИ')
                account.click()
                sleep(5)
                spisok2 = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                spisok2.remove(spisok2[0])
                print spisok2
                for i in spisok2:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    self.assertTrue(re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH')

        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_18.png'
            self.driver.save_screenshot(directory + file_name)
            raise


    # Нет прав на Депозиты
    def test_19(self):
        try:
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
            login(self, lang)

            if lang == 0:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('My Accounts')
                bil.click()
                try:
                    self.driver.find_element_by_id('Deposits')
                    raise NameError('Deposits present')
                except NoSuchElementException:
                    return True

            elif lang == 1:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Мои счета')
                bil.click()
                try:
                    self.driver.find_element_by_id('Депозиты')
                    raise NameError('Deposits present')
                except NoSuchElementException:
                    return True

            elif lang == 2:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Мої рахунки')
                bil.click()
                try:
                    self.driver.find_element_by_id('Депозити')
                    raise NameError('Deposits present')
                except NoSuchElementException:
                    return True

        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_19.png'
            self.driver.save_screenshot(directory + file_name)
            raise


    # Нет прав на Депозиты
    def test_20(self):
        try:
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
            login(self, lang)

            if lang == 0:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('My Accounts')
                bil.click()
                try:
                    self.driver.find_element_by_id('Loans')
                    raise NameError('Credits present')
                except NoSuchElementException:
                    return True

            elif lang == 1:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Мои счета')
                bil.click()
                try:
                    self.driver.find_element_by_id('Кредиты')
                    raise NameError('Credits present')
                except NoSuchElementException:
                    return True

            elif lang == 2:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Мої рахунки')
                bil.click()
                try:
                    self.driver.find_element_by_id('Кредити')
                    raise NameError('Credits present')
                except NoSuchElementException:
                    return True

        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_20.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # Нет прав на платежи
    def test_21(self):
        try:
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
            login(self, lang)

            if lang == 0:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                try:
                    self.driver.find_element_by_id('Payments')
                    raise NameError('Payments present')
                except NoSuchElementException:
                    return True

            elif lang == 1:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                try:
                    self.driver.find_element_by_id('Платежи')
                    raise NameError ('Payments present')
                except NoSuchElementException:
                    return True

            elif lang == 2:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                try:
                    self.driver.find_element_by_id('Платежі')
                    raise NameError('Payments present')
                except NoSuchElementException:
                    return True

        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_21.png'
            self.driver.save_screenshot(directory + file_name)
            raise


    # Нет прав на Карты
    def test_22(self):
        try:
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
            login(self, lang)

            if lang == 0:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('My Accounts')
                bil.click()
                try:
                    self.driver.find_element_by_id('Cards')
                    raise NameError('Cards present')
                except NoSuchElementException:
                    return True

            elif lang == 1:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Мои счета')
                bil.click()
                try:
                    self.driver.find_element_by_id('Карточные')
                    raise NameError('Cards present')
                except NoSuchElementException:
                    return True

            elif lang == 2:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Мої рахунки')
                bil.click()
                try:
                    self.driver.find_element_by_id('Карткові')
                    raise NameError('Cards present')
                except NoSuchElementException:
                    return True

        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_22.png'
            self.driver.save_screenshot(directory + file_name)
            raise


    # Отображение счетов
    def test_23(self):
        try:
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
            login(self, lang)

            if lang == 0:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('My Accounts')
                bil.click()
                sch = self.driver.find_element_by_id('Current')
                sch.click()
                sleep(10)
                try:
                    self.driver.find_element_by_id('Empty list')
                except:
                    sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                    scheta_req()

                    acc = []
                    unactiv = []
                    tree = ET.parse('xmls/enc_data.xml')
                    root = tree.getroot()
                    for i in root.iter('AccountDetails'):
                        if i.find('Type').text == 'CURRENT':
                            if i.find('Status').text == 'ACTIVE':
                                acc.append(i.find('AccountNo').text)
                            else:
                                unactiv.append(i.find('AccountNo').text)

                    for i in sp:
                        w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[2]')
                        if w.get_attribute('name') in acc:
                            pass
                        else:
                            raise NameError('Not Active in active')

            elif lang == 1:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Мои счета')
                bil.click()
                sch = self.driver.find_element_by_id('Текущие')
                sch.click()
                sleep(10)
                try:
                    self.driver.find_element_by_id('Пустой список')
                except:
                    sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                    scheta_req()

                    acc = []
                    unactiv = []
                    tree = ET.parse('xmls/enc_data.xml')
                    root = tree.getroot()
                    for i in root.iter('AccountDetails'):
                        if i.find('Type').text == 'CURRENT':
                            if i.find('Status').text == 'ACTIVE':
                                acc.append(i.find('AccountNo').text)
                            else:
                                unactiv.append(i.find('AccountNo').text)

                    for i in sp:
                        w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[2]')
                        if w.get_attribute('name') in acc:
                            pass
                        else:
                            raise NameError('Not Active in active')

            elif lang == 2:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Мої рахунки')
                bil.click()
                sch = self.driver.find_element_by_id('Поточні')
                sch.click()
                sleep(10)
                try:
                    self.driver.find_element_by_id('Пустий список')
                except:
                    sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                    scheta_req()

                    acc = []
                    unactiv = []
                    tree = ET.parse('xmls/enc_data.xml')
                    root = tree.getroot()
                    for i in root.iter('AccountDetails'):
                        if i.find('Type').text == 'CURRENT':
                            if i.find('Status').text == 'ACTIVE':
                                acc.append(i.find('AccountNo').text)
                            else:
                                unactiv.append(i.find('AccountNo').text)

                    for i in sp:
                        w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[2]')
                        if w.get_attribute('name') in acc:
                            pass
                        else:
                            raise NameError('Not Active in active')

        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_23.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # Отображение счетов
    def test_23(self):
        try:
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
            login(self, lang)

            if lang == 0:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('My Accounts')
                bil.click()
                sch = self.driver.find_element_by_id('Current')
                sch.click()
                sleep(10)
                try:
                    self.driver.find_element_by_id('Empty list')
                except:
                    sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                    scheta_req()

                    acc = []
                    unactiv = []
                    tree = ET.parse('xmls/enc_data.xml')
                    root = tree.getroot()
                    for i in root.iter('AccountDetails'):
                        if i.find('Type').text == 'CURRENT':
                            if i.find('Status').text == 'ACTIVE':
                                acc.append(i.find('AccountNo').text)
                            else:
                                unactiv.append(i.find('AccountNo').text)

                    for i in sp:
                        w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[2]')
                        if w.get_attribute('name') in acc:
                            pass
                        else:
                            raise NameError('Not Active in active')

            elif lang == 1:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Мои счета')
                bil.click()
                sch = self.driver.find_element_by_id('Текущие')
                sch.click()
                sleep(10)
                try:
                    self.driver.find_element_by_id('Пустой список')
                except:
                    sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                    scheta_req()

                    acc = []
                    unactiv = []
                    tree = ET.parse('xmls/enc_data.xml')
                    root = tree.getroot()
                    for i in root.iter('AccountDetails'):
                        if i.find('Type').text == 'CURRENT':
                            if i.find('Status').text == 'ACTIVE':
                                acc.append(i.find('AccountNo').text)
                            else:
                                unactiv.append(i.find('AccountNo').text)

                    for i in sp:
                        w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[2]')
                        if w.get_attribute('name') in acc:
                            pass
                        else:
                            raise NameError('Not Active in active')

            elif lang == 2:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Мої рахунки')
                bil.click()
                sch = self.driver.find_element_by_id('Поточні')
                sch.click()
                sleep(10)
                try:
                    self.driver.find_element_by_id('Пустий список')
                except:
                    sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                    scheta_req()

                    acc = []
                    unactiv = []
                    tree = ET.parse('xmls/enc_data.xml')
                    root = tree.getroot()
                    for i in root.iter('AccountDetails'):
                        if i.find('Type').text == 'CURRENT':
                            if i.find('Status').text == 'ACTIVE':
                                acc.append(i.find('AccountNo').text)
                            else:
                                unactiv.append(i.find('AccountNo').text)

                    for i in sp:
                        w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[2]')
                        if w.get_attribute('name') in acc:
                            pass
                        else:
                            raise NameError('Not Active in active')

        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_23.png'
            self.driver.save_screenshot(directory + file_name)
            raise


    # Отображение Карт
    def test_24(self):
        try:
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
            login(self, lang)

            if lang == 0:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('My Accounts')
                bil.click()
                sch = self.driver.find_element_by_id('Cards')
                sch.click()
                sleep(30)
                act = self.driver.find_element_by_id('ACTIVE')
                act.click()
                try:
                    self.driver.find_element_by_id('Empty list')
                except:
                    sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                    cards_req()

                    acc = []
                    unacc = []
                    tree = ET.parse('/Users/admin/PycharmProjects/tests/iOS/xmls/enc_data.xml')
                    root = tree.getroot()
                    for i in root.iter('AccountDetails'):
                        if i.find('Type').text == 'CARD':
                            if i.find('Card').find('State').text == 'ACTIVE':
                                acc.append(i.find('Card').find('CardNo').text)
                            else:
                                unacc.append(i.find('Card').find('CardNo').text)

                    for i in sp:
                        w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText')
                        if w.get_attribute('name').replace(' ', '') in acc:
                            pass
                        else:
                            print w.get_attribute('name')
                            raise NameError('Not Active in active')

                    if unacc != []:
                        inac = self.driver.find_element_by_id('INACTIVE')
                        inac.click()
                        sleep(5)
                        sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')

                        for i in sp:
                            w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText')
                            if w.get_attribute('name').replace(' ', '') in unacc:
                                pass
                            else:
                                print w.get_attribute('name')
                                raise NameError('Not Active in active')
                    else:
                        print 'No UnActive cards'
                        pass

            elif lang == 1:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Мои счета')
                bil.click()
                sch = self.driver.find_element_by_id('Карточные')
                sch.click()
                sleep(30)
                act = self.driver.find_element_by_id('АКТИВНЫЕ')
                act.click()
                try:
                    self.driver.find_element_by_id('Пустой список')
                except:
                    act = self.driver.find_element_by_id('АКТИВНЫЕ')
                    act.click()
                    sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                    cards_req()

                    acc = []
                    unacc = []
                    tree = ET.parse('/Users/admin/PycharmProjects/tests/iOS/xmls/enc_data.xml')
                    root = tree.getroot()
                    for i in root.iter('AccountDetails'):
                        if i.find('Type').text == 'CARD':
                            if i.find('Card').find('State').text == 'ACTIVE':
                                acc.append(i.find('Card').find('CardNo').text)
                            else:
                                unacc.append(i.find('Card').find('CardNo').text)

                    for i in sp:
                        w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText')
                        if w.get_attribute('name').replace(' ', '') in acc:
                            pass
                        else:
                            print w.get_attribute('name')
                            raise NameError('Not Active in active')

                    if unacc != []:
                        inac = self.driver.find_element_by_id('НЕАКТИВНЫЕ')
                        inac.click()
                        sleep(5)
                        sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')

                        for i in sp:
                            w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText')
                            if w.get_attribute('name').replace(' ', '') in unacc:
                                pass
                            else:
                                print w.get_attribute('name')
                                raise NameError('Not Active in active')
                    else:
                        print 'No UnActive cards'
                        pass

            elif lang == 2:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Мої рахунки')
                bil.click()
                sch = self.driver.find_element_by_id('Карткові')
                sch.click()
                sleep(30)
                act = self.driver.find_element_by_id('АКТИВНІ')
                act.click()
                try:
                    self.driver.find_element_by_id('Пустий список')
                except:
                    sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                    cards_req()

                    acc = []
                    unacc = []
                    tree = ET.parse('/Users/admin/PycharmProjects/tests/iOS/xmls/enc_data.xml')
                    root = tree.getroot()
                    for i in root.iter('AccountDetails'):
                        if i.find('Type').text == 'CARD':
                            if i.find('Card').find('State').text == 'ACTIVE':
                                acc.append(i.find('Card').find('CardNo').text)
                            else:
                                unacc.append(i.find('Card').find('CardNo').text)

                    for i in sp:
                        w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText')
                        if w.get_attribute('name').replace(' ', '') in acc:
                            pass
                        else:
                            print w.get_attribute('name')
                            raise NameError('Not Active in active')

                    if unacc != []:
                        inac = self.driver.find_element_by_id('НЕАКТИВНІ')
                        inac.click()
                        sleep(5)
                        sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')

                        for i in sp:
                            w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText')
                            if w.get_attribute('name').replace(' ', '') in unacc:
                                pass
                            else:
                                print w.get_attribute('name')
                                raise NameError('Not Active in active')
                    else:
                        print 'No UnActive cards'
                        pass

        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_24.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # Отображение Депозитов
    def test_25(self):
        try:
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
            login(self, lang)

            if lang == 0:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('My Accounts')
                bil.click()
                sch = self.driver.find_element_by_id('Deposits')
                sch.click()
                sleep(30)
                act = self.driver.find_element_by_id('ACTIVE')
                act.click()
                try:
                    self.driver.find_element_by_id('Empty list')
                except:
                    sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                    credit_req()

                    acc = []
                    unacc = []
                    tree = ET.parse('/Users/admin/PycharmProjects/tests/iOS/xmls/enc_data.xml')
                    root = tree.getroot()
                    for i in root.iter('AccountDetails'):
                        if i.find('Type').text == 'DEPOSIT':
                            if i.find('Status').text == 'ACTIVE':
                                acc.append(i.find('Deposit').find('AgreementNo').text)
                            else:
                                unacc.append(i.find('Deposit').find('AgreementNo').text)

                    for i in sp:
                        w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText')
                        if w.get_attribute('name') in acc:
                            pass
                        else:
                            print w.get_attribute('name')
                            raise NameError('Not Active in active')

                    if unacc != []:
                        inac = self.driver.find_element_by_id('INACTIVE')
                        inac.click()
                        sleep(5)
                        sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')

                        for i in sp:
                            w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText')
                            w1 = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[3]')
                            if w.get_attribute('name') or w1.get_attribute('name') in unacc:
                                pass
                            else:
                                print w.get_attribute('name')
                                raise NameError('Not Active in active')
                    else:
                        print 'No UnActive cards'
                        pass

            elif lang == 1:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Мои счета')
                bil.click()
                sch = self.driver.find_element_by_id('Депозиты')
                sch.click()
                sleep(30)
                act = self.driver.find_element_by_id('АКТИВНЫЕ')
                act.click()
                try:
                    self.driver.find_element_by_id('Пустий список')
                except:
                    sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                    credit_req()

                    acc = []
                    unacc = []
                    tree = ET.parse('/Users/admin/PycharmProjects/tests/iOS/xmls/enc_data.xml')
                    root = tree.getroot()
                    for i in root.iter('AccountDetails'):
                        if i.find('Type').text == 'DEPOSIT':
                            if i.find('Status').text == 'ACTIVE':
                                acc.append(i.find('Deposit').find('AgreementNo').text)
                            else:
                                unacc.append(i.find('Deposit').find('AgreementNo').text)

                    for i in sp:
                        w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText')
                        if w.get_attribute('name') in acc:
                            pass
                        else:
                            print w.get_attribute('name')
                            raise NameError('Not Active in active')

                    if unacc != []:
                        inac = self.driver.find_element_by_id('НЕАКТИВНЫЕ')
                        inac.click()
                        sleep(5)
                        sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')

                        for i in sp:
                            w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText')
                            w1 = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[3]')
                            if w.get_attribute('name') or w1.get_attribute('name') in unacc:
                                pass
                            else:
                                print w.get_attribute('name')
                                raise NameError('Not Active in active')
                    else:
                        print 'No UnActive cards'
                        pass

            elif lang == 2:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Мої рахунки')
                bil.click()
                sch = self.driver.find_element_by_id('Депозити')
                sch.click()
                sleep(30)
                act = self.driver.find_element_by_id('АКТИВНІ')
                act.click()
                try:
                    self.driver.find_element_by_id('Пустий список')
                except:
                    sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                    credit_req()

                    acc = []
                    unacc = []
                    tree = ET.parse('/Users/admin/PycharmProjects/tests/iOS/xmls/enc_data.xml')
                    root = tree.getroot()
                    for i in root.iter('AccountDetails'):
                        if i.find('Type').text == 'DEPOSIT':
                            if i.find('Status').text == 'ACTIVE':
                                acc.append(i.find('Deposit').find('AgreementNo').text)
                            else:
                                unacc.append(i.find('Deposit').find('AgreementNo').text)

                    for i in sp:
                        w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText')
                        if w.get_attribute('name').replace(' ', '') in acc:
                            pass
                        else:
                            print w.get_attribute('name')
                            raise NameError('Not Active in active')

                    if unacc != []:
                        inac = self.driver.find_element_by_id('НЕАКТИВНІ')
                        inac.click()
                        sleep(5)
                        sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')

                        for i in sp:
                            w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText')
                            w1 = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[3]')
                            if w.get_attribute('name').replace(' ', '') or w1.get_attribute('name').replace(' ',
                                                                                                            '') in unacc:
                                pass
                            else:
                                print w.get_attribute('name')
                                raise NameError('Not Active in active')
                    else:
                        print 'No UnActive cards'
                        pass

        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_25.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # Отображение Кредиты на владках
    def test_26(self):
        try:
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
            login(self, lang)

            if lang == 0:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('My Accounts')
                bil.click()
                sch = self.driver.find_element_by_id('Loans')
                sch.click()
                sleep(30)
                act = self.driver.find_element_by_id('ACTIVE')
                act.click()
                try:
                    self.driver.find_element_by_id('Empty list')
                except:
                    sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                    credit_req()

                    acc = []
                    unacc = []
                    tree = ET.parse('/Users/admin/PycharmProjects/tests/iOS/xmls/enc_data.xml')
                    root = tree.getroot()
                    for i in root.iter('AccountDetails'):
                        if i.find('Type').text == 'CREDIT':
                            if i.find('Status').text == 'ACTIVE':
                                acc.append(i.find('Credit').find('AgreementNo').text)
                            else:
                                unacc.append(i.find('Credit').find('AgreementNo').text)

                    for i in sp:
                        w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText')
                        if w.get_attribute('name') in acc:
                            pass
                        else:
                            print w.get_attribute('name')
                            raise NameError('Not Active in active')

                    if unacc != []:
                        inac = self.driver.find_element_by_id('INACTIVE')
                        inac.click()
                        sleep(5)
                        sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')

                        for i in sp:
                            w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText')
                            w1 = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[3]')
                            if w.get_attribute('name').replace(' ', '') or w1.get_attribute('name').replace(' ',
                                                                                                            '') in unacc:
                                pass
                            else:
                                print w.get_attribute('name')
                                raise NameError('Not Active in active')
                    else:
                        print 'No UnActive cards'
                        pass

            elif lang == 1:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Мои счета')
                bil.click()
                sch = self.driver.find_element_by_id('Кредиты')
                sch.click()
                sleep(30)
                act = self.driver.find_element_by_id('АКТИВНЫЕ')
                act.click()
                try:
                    self.driver.find_element_by_id('Пустий список')
                except:
                    sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                    credit_req()

                    acc = []
                    unacc = []
                    tree = ET.parse('/Users/admin/PycharmProjects/tests/iOS/xmls/enc_data.xml')
                    root = tree.getroot()
                    for i in root.iter('AccountDetails'):
                        if i.find('Type').text == 'CREDIT':
                            if i.find('Status').text == 'ACTIVE':
                                acc.append(i.find('Credit').find('AgreementNo').text)
                            else:
                                unacc.append(i.find('Credit').find('AgreementNo').text)

                    for i in sp:
                        w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText')
                        if w.get_attribute('name') in acc:
                            pass
                        else:
                            print w.get_attribute('name')
                            raise NameError('Not Active in active')

                    if unacc != []:
                        inac = self.driver.find_element_by_id('НЕАКТИВНЫЕ')
                        inac.click()
                        sleep(5)
                        sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')

                        for i in sp:
                            w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText')
                            w1 = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[3]')
                            if w.get_attribute('name').replace(' ', '') or w1.get_attribute('name').replace(' ',
                                                                                                            '') in unacc:
                                pass
                            else:
                                print w.get_attribute('name')
                                raise NameError('Not Active in active')
                    else:
                        print 'No UnActive cards'
                        pass

            elif lang == 2:
                self.driver.implicitly_wait(15)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Мої рахунки')
                bil.click()
                sch = self.driver.find_element_by_id('Кредити')
                sch.click()
                sleep(30)
                act = self.driver.find_element_by_id('АКТИВНІ')
                act.click()
                try:
                    self.driver.find_element_by_id('Пустий список')
                except:
                    sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                    credit_req()

                    acc = []
                    unacc = []
                    tree = ET.parse('/Users/admin/PycharmProjects/tests/iOS/xmls/enc_data.xml')
                    root = tree.getroot()
                    for i in root.iter('AccountDetails'):
                        if i.find('Type').text == 'CREDIT':
                            if i.find('Status').text == 'ACTIVE':
                                acc.append(i.find('Credit').find('AgreementNo').text)
                            else:
                                unacc.append(i.find('Credit').find('AgreementNo').text)

                    for i in sp:
                        w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText')
                        if w.get_attribute('name') in acc:
                            pass
                        else:
                            print w.get_attribute('name')
                            raise NameError('Not Active in active')

                    if unacc != []:
                        inac = self.driver.find_element_by_id('НЕАКТИВНІ')
                        inac.click()
                        sleep(5)
                        sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')

                        for i in sp:
                            w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText')
                            w1 = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[3]')
                            if w.get_attribute('name').replace(' ', '') or w1.get_attribute('name').replace(' ',
                                                                                                            '') in unacc:
                                pass
                            else:
                                print w.get_attribute('name')
                                raise NameError('Not Active in active')
                    else:
                        print 'No UnActive cards'
                        pass

        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_26.png'
            self.driver.save_screenshot(directory + file_name)
            raise


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Rules)
    unittest.TextTestRunner(verbosity=2).run(suite)
