# -*- coding: utf-8 -*-
import os
import re
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from iphone.OTP.login_planshet import login_planshet


def accounts_mask(self, login, password):
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
        # login(self, lang)
        login_planshet(self, login, password, lang)

        if lang == 0:
            self.driver.implicitly_wait(15)
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
            account = self.driver.find_element_by_id('From account')
            account.click()
            sleep(3)
            sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
            sp.remove(sp[len(sp) - 1])
            for i in sp:
                w = re.findall(r'\d{11,}',
                               i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText').get_attribute(
                                   'name'))
                w1 = re.findall(r'\d{11,}', i.find_element_by_xpath(
                    '//XCUIElementTypeCell/XCUIElementTypeStaticText[2]').get_attribute('name'))
                if w:
                    print w[0]
                    if w == re.findall(r'2625\d{6,}', w[0]):
                        raise NameError('we got 2625 acc')
                elif w1:
                    print w1
                    if w1 == re.findall(r'2625\d{6,}', w1[0]):
                        raise NameError('we got 2625 acc')

        elif lang == 1:
            self.driver.implicitly_wait(15)
            try:
                allert = self.driver.find_element_by_id('Нет')
                allert.click()
            except NoSuchElementException:
                pass
            menu = self.driver.find_element_by_id('homePage')
            menu.click()
            perevodi = self.driver.find_element_by_id('Переводы')
            perevodi.click()
            perevodi = self.driver.find_element_by_id('Новый платеж')
            perevodi.click()
            scheta = self.driver.find_element_by_id('Между своими счетами')
            scheta.click()
            new_schet = self.driver.find_element_by_id('Новый')
            new_schet.click()
            schet_switch = self.driver.find_element_by_id('Со счета')
            schet_switch.click()
            sleep(3)
            sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
            sp.remove(sp[len(sp) - 1])
            for i in sp:
                w = re.findall(r'\d{11,}', i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText').get_attribute('name'))
                w1 = re.findall(r'\d{11,}', i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[2]').get_attribute('name'))
                if w:
                    print w[0]
                    if w == re.findall(r'2625\d{6,}', w[0]):
                        raise NameError('we got 2625 acc')
                elif w1:
                    print w1
                    if w1 == re.findall(r'2625\d{6,}', w1[0]):
                        raise NameError('we got 2625 acc')

        elif lang == 2:
            self.driver.implicitly_wait(15)
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
            account = self.driver.find_element_by_id('З рахунку')
            account.click()
            sleep(3)
            sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
            sp.remove(sp[len(sp) - 1])
            for i in sp:
                w = re.findall(r'\d{11,}',
                               i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText').get_attribute(
                                   'name'))
                w1 = re.findall(r'\d{11,}', i.find_element_by_xpath(
                    '//XCUIElementTypeCell/XCUIElementTypeStaticText[2]').get_attribute('name'))
                if w:
                    if w == re.findall(r'2625\d{6,}', w[0]):
                        raise NameError('we got 2625 acc')
                elif w1:
                    if w1 == re.findall(r'2625\d{6,}', w1[0]):
                        raise NameError('we got 2625 acc')

    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_27.png'
        self.driver.save_screenshot(directory + file_name)
        raise