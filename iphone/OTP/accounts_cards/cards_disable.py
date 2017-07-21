# -*- coding: utf-8 -*-
import os
import re

import sys
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from iphone.OTP.database.rules import rules
from iphone.OTP.login_planshet import login_planshet


def cards_disable(self, login, password):
    try:
        rules(46, login)
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
            self.driver.implicitly_wait(10)
            try:
                allert = self.driver.find_element_by_id('No')
                allert.click()
            except NoSuchElementException:
                pass
            sleep(4)
            try:
                cards = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[3]')
                s = cards.get_attribute('name')
                if s.split(' ')[0].encode('utf-8') == 'CARDS':
                    raise NameError('Cards present')
                else:
                    return True
            except NoSuchElementException:

                return True

        elif lang == 1:
            self.driver.implicitly_wait(10)
            try:
                allert = self.driver.find_element_by_id('Нет')
                allert.click()
            except NoSuchElementException:
                pass
            sleep(4)
            try:
                cards = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[3]')
                s = cards.get_attribute('name')
                if s.split(' ')[0].encode('utf-8') == 'КАРТЫ':
                    raise NameError('Cards present')
                else:
                    return True
            except NoSuchElementException:

                return True


        elif lang == 2:
            self.driver.implicitly_wait(5)
            try:
                allert = self.driver.find_element_by_id('Ні')
                allert.click()
            except NoSuchElementException:
                pass
            sleep(4)
            try:
                cards = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[3]')
                s = cards.get_attribute('name')
                if s.split(' ')[0].encode('utf-8') == 'КАРТИ':
                    raise NameError('Cards present')
                else:
                    return True
            except NoSuchElementException:

                return True

    except:

        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_22.png'
        self.driver.save_screenshot(directory + file_name)
        raise

    finally:
        rules(46, login)
