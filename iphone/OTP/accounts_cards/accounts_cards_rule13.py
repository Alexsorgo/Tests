# -*- coding: utf-8 -*-
import os
import re
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from iphone.OTP.database.rules import acc_rule13
from iphone.OTP.login_planshet import login_planshet


def accounts_cards_rule13(self, login, password):
    try:
        # acc_rule13(login)
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
            sleep(3)
            acc = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther/XCUIElementTypeStaticText')
            number = re.findall(r'\(\d+\)', acc.get_attribute('value'))[0]
            count = number.strip(')').lstrip('(')
            acc_rule13(login)
            sleep(5)
            refresh = self.driver.find_element_by_id('buttonRefreshNormal')
            refresh.click()
            sleep(5)
            number2 = re.findall(r'\(\d+\)', self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther/XCUIElementTypeStaticText').get_attribute('Value'))[0]
            count2 = number2.strip(')').lstrip('(')
            if count2 != count:
                return True
            else:
                raise NameError('Account still displayed')

        elif lang == 1:
            self.driver.implicitly_wait(15)
            try:
                allert = self.driver.find_element_by_id('Нет')
                allert.click()
            except NoSuchElementException:
                pass
            sleep(3)
            acc = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther/XCUIElementTypeStaticText')
            number = re.findall(r'\(\d+\)', acc.get_attribute('value'))[0]
            count = number.strip(')').lstrip('(')
            acc_rule13(login)
            sleep(5)
            refresh = self.driver.find_element_by_id('buttonRefreshNormal')
            refresh.click()
            sleep(5)
            number2 = re.findall(r'\(\d+\)', self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther/XCUIElementTypeStaticText').get_attribute(
                'Value'))[0]
            count2 = number2.strip(')').lstrip('(')
            if count2 != count:
                return True
            else:
                raise NameError('Account still displayed')

        elif lang == 2:
            self.driver.implicitly_wait(15)
            try:
                allert = self.driver.find_element_by_id('Ні')
                allert.click()
            except NoSuchElementException:
                pass
            sleep(3)
            acc = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther/XCUIElementTypeStaticText')
            number = re.findall(r'\(\d+\)', acc.get_attribute('value'))[0]
            count = number.strip(')').lstrip('(')
            acc_rule13(login)
            sleep(5)
            refresh = self.driver.find_element_by_id('buttonRefreshNormal')
            refresh.click()
            sleep(5)
            number2 = re.findall(r'\(\d+\)', self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther/XCUIElementTypeStaticText').get_attribute(
                'Value'))[0]
            count2 = number2.strip(')').lstrip('(')
            if count2 != count:
                return True
            else:
                raise NameError('Account still displayed')

    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_26.png'
        self.driver.save_screenshot(directory + file_name)
        raise

    finally:
        acc_rule13(login)
