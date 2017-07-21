# -*- coding: utf-8 -*-
import os
import re
import xml.etree.ElementTree as ET
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from iphone.OTP.login_planshet import login_planshet
from iphone.OTP.reques.credit import cards_req


def cards_active(self, login, password):
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
        cards_req()

        if lang == 0:
            try:
                allert = self.driver.find_element_by_id('No')
                allert.click()
            except NoSuchElementException:
                pass
            sleep(5)
            sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')

            acc = []
            unacc = []
            tree = ET.parse('/Users/admin/PycharmProjects/OTP/xmls/enc_data.xml')
            root = tree.getroot()
            for i in root.iter('AccountDetails'):
                if i.find('Type').text == 'CARD':
                    if i.find('Card').find('State').text == 'ACTIVE':
                        acc.append(i.find('Card').find('CardNo').text)
                    else:
                        unacc.append(i.find('Card').find('CardNo').text)
            ac_appl = []
            for i in sp:
                self.driver.implicitly_wait(3)

                try:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[3]')
                    if re.findall(r'\d{6}\*{6}\d{4}', w.get_attribute('name').replace(' ', '')):
                        ac_appl.append(w.get_attribute('name').replace(' ', ''))
                    else:
                        pass
                except:
                    pass
            for i in ac_appl:
                if i in acc:
                    pass
                else:
                    raise NameError('UnActive in active')

        elif lang == 1:
            try:
                allert = self.driver.find_element_by_id('Нет')
                allert.click()
            except NoSuchElementException:
                pass
            sleep(5)
            sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')

            acc = []
            unacc = []
            tree = ET.parse('/Users/admin/PycharmProjects/OTP/xmls/enc_data.xml')
            root = tree.getroot()
            for i in root.iter('AccountDetails'):
                if i.find('Type').text == 'CARD':
                    if i.find('Card').find('State').text == 'ACTIVE':
                        acc.append(i.find('Card').find('CardNo').text)
                    else:
                        unacc.append(i.find('Card').find('CardNo').text)
            ac_appl = []
            for i in sp:
                self.driver.implicitly_wait(3)

                try:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[3]')
                    if re.findall(r'\d{6}\*{6}\d{4}', w.get_attribute('name').replace(' ', '')):
                        ac_appl.append(w.get_attribute('name').replace(' ', ''))
                    else:
                        pass
                except:
                    pass
            for i in ac_appl:
                if i in acc:
                    pass
                else:
                    raise NameError('UnActive in active')

        elif lang == 2:
            try:
                allert = self.driver.find_element_by_id('Ні')
                allert.click()
            except NoSuchElementException:
                pass
            sleep(5)
            sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')

            acc = []
            unacc = []
            tree = ET.parse('/Users/admin/PycharmProjects/OTP/xmls/enc_data.xml')
            root = tree.getroot()
            for i in root.iter('AccountDetails'):
                if i.find('Type').text == 'CARD':
                    if i.find('Card').find('State').text == 'ACTIVE':
                        acc.append(i.find('Card').find('CardNo').text)
                    else:
                        unacc.append(i.find('Card').find('CardNo').text)
            ac_appl = []
            for i in sp:
                self.driver.implicitly_wait(3)

                try:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[3]')
                    if re.findall(r'\d{6}\*{6}\d{4}', w.get_attribute('name').replace(' ', '')):
                        ac_appl.append(w.get_attribute('name').replace(' ', ''))
                    else:
                        pass
                except:
                    pass
            for i in ac_appl:
                if i in acc:
                    pass
                else:
                    raise NameError('UnActive in active')

    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_15.png'
        self.driver.save_screenshot(directory + file_name)
        raise