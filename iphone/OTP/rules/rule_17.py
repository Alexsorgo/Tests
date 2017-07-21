# -*- coding: utf-8 -*-
import os
import re

from time import sleep

from selenium.common.exceptions import NoSuchElementException

from iphone.OTP.database.rules import rules
from iphone.OTP.login_planshet import login_planshet


def rule_17(self, login, password):
    try:
        rules(17, login)
        try:
            self.driver.find_element_by_id('Cancel').click()
        except NoSuchElementException:
            pass
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
        # login(self, lang)
        login_planshet(self, login, password, lang)

        if lang == 0:
            self.driver.implicitly_wait(30)
            try:
                allert = self.driver.find_element_by_id('No')
                allert.click()
            except NoSuchElementException:
                pass
            menu = self.driver.find_element_by_id('homePage')
            menu.click()
            bil = self.driver.find_element_by_id('Transfers')
            bil.click()
            new_trans = self.driver.find_element_by_id('New transfers')
            new_trans.click()
            scheta = self.driver.find_element_by_id('Between own accounts')
            scheta.click()
            new_schet = self.driver.find_element_by_id('New')
            new_schet.click()
            sleep(3)
            self.driver.find_element_by_id('Done').click()
            sleep(3)
            sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
            sp.remove(sp[len(sp)-1])
            cur = []
            for i in sp:
                try:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[3]')
                except NoSuchElementException:
                    print i.find_element_by_xpath('//XCUIElementTypeCell').get_attribute('name')
                    print 'exception time'
                w1 = i.find_element_by_xpath(
                    '//XCUIElementTypeCell/XCUIElementTypeStaticText[1]')
                if not re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')):
                    cur.append(re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' '))

                elif not re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')):
                    cur.append(re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' '))
            self.assertTrue('UAH' not in cur)

            account = self.driver.find_element_by_id('From account')
            account.click()
            sleep(5)
            spisok2 = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
            spisok2.remove(spisok2[len(spisok2)-1])
            for i in spisok2:
                w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[3]')
                w1 = i.find_element_by_xpath(
                    '//XCUIElementTypeCell/XCUIElementTypeStaticText[1]')
                if not re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')):
                    cur.append(re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' '))

                elif not re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')):
                    cur.append(re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' '))
            self.assertTrue('UAH' not in cur)

        elif lang == 1:
            self.driver.implicitly_wait(30)
            try:
                allert = self.driver.find_element_by_id('Нет')
                allert.click()
            except NoSuchElementException:
                pass
            menu = self.driver.find_element_by_id('homePage')
            menu.click()
            bil = self.driver.find_element_by_id('Переводы')
            bil.click()
            new_trans = self.driver.find_element_by_id('Новый платеж')
            new_trans.click()
            scheta = self.driver.find_element_by_id('Между своими счетами')
            scheta.click()
            new_schet = self.driver.find_element_by_id('Новый')
            new_schet.click()

            sleep(3)
            self.driver.find_element_by_id('Done').click()
            sleep(3)
            sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
            sp.remove(sp[len(sp) - 1])
            cur = []
            for i in sp:
                try:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[3]')
                except NoSuchElementException:
                    print i.find_element_by_xpath('//XCUIElementTypeCell').get_attribute('name')
                    print 'exception time'
                w1 = i.find_element_by_xpath(
                    '//XCUIElementTypeCell/XCUIElementTypeStaticText[1]')
                if not re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')):
                    cur.append(re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' '))

                elif not re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')):
                    cur.append(re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' '))
            self.assertTrue('UAH' not in cur)

            account = self.driver.find_element_by_id('Со счета')
            account.click()
            sleep(5)
            spisok2 = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
            spisok2.remove(spisok2[len(spisok2) - 1])
            for i in spisok2:
                w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[3]')
                w1 = i.find_element_by_xpath(
                    '//XCUIElementTypeCell/XCUIElementTypeStaticText[1]')
                if not re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')):
                    cur.append(re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' '))

                elif not re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')):
                    cur.append(re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' '))
            self.assertTrue('UAH' not in cur)

        elif lang == 2:
            self.driver.implicitly_wait(30)
            try:
                allert = self.driver.find_element_by_id('Ні')
                allert.click()
            except NoSuchElementException:
                pass
            menu = self.driver.find_element_by_id('homePage')
            menu.click()
            bil = self.driver.find_element_by_id('Перекази')
            bil.click()
            new_trans = self.driver.find_element_by_id('Новий переказ')
            new_trans.click()
            scheta = self.driver.find_element_by_id('Між своїми рахунками')
            scheta.click()
            new_schet = self.driver.find_element_by_id('Новий')
            new_schet.click()

            sleep(3)
            self.driver.find_element_by_id('Done').click()
            sleep(3)
            sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
            sp.remove(sp[len(sp) - 1])
            cur = []
            for i in sp:
                try:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[3]')
                except NoSuchElementException:
                    print i.find_element_by_xpath('//XCUIElementTypeCell').get_attribute('name')
                    print 'exception time'
                w1 = i.find_element_by_xpath(
                    '//XCUIElementTypeCell/XCUIElementTypeStaticText[1]')
                if not re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')):
                    cur.append(re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' '))

                elif not re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')):
                    cur.append(re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' '))
            self.assertTrue('UAH' not in cur)

            account = self.driver.find_element_by_id('З рахунку')
            account.click()
            sleep(5)
            spisok2 = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
            spisok2.remove(spisok2[len(spisok2) - 1])
            for i in spisok2:
                w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[3]')
                w1 = i.find_element_by_xpath(
                    '//XCUIElementTypeCell/XCUIElementTypeStaticText[1]')
                if not re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')):
                    cur.append(re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' '))

                elif not re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')):
                    cur.append(re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' '))
            self.assertTrue('UAH' not in cur)

    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_17.png'
        self.driver.save_screenshot(directory + file_name)
        raise

    finally:
        rules(17, login)