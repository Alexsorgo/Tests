# -*- coding: utf-8 -*-
import os
import re
import xml.etree.ElementTree as ET
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from iphone.OTP.login_planshet import login_planshet
from iphone.OTP.reques.credit import scheta_req


def account_active(self, login, password):
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
        scheta_req()

        if lang == 0:
            try:
                allert = self.driver.find_element_by_id('No')
                allert.click()
            except NoSuchElementException:
                pass
            sleep(5)
            sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')

            acc = []
            unactiv = []
            tree = ET.parse('/Users/admin/PycharmProjects/OTP/xmls/enc_data.xml')
            root = tree.getroot()
            for i in root.iter('AccountDetails'):
                if i.find('Status').text == 'ACTIVE':
                    acc.append(i.find('AccountNo').text)
                else:
                    unactiv.append(i.find('AccountNo').text)

            ac_appl = []
            for i in sp:
                self.driver.implicitly_wait(3)

                try:
                    w = re.findall(r'\d{11,}',
                                   i.find_element_by_xpath(
                                       '//XCUIElementTypeCell/XCUIElementTypeStaticText').get_attribute(
                                       'name'))
                    w1 = re.findall(r'\d{11,}', i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[2]').get_attribute('name'))
                    if w:
                        ac_appl.append(w)
                    if w1:
                        ac_appl.append(w1)
                except:
                    pass
            for i in ac_appl:
                if str(i[0]) in acc:
                    pass
                else:
                    print str(i[0])
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
            unactiv = []
            tree = ET.parse('/Users/admin/PycharmProjects/OTP/xmls/enc_data.xml')
            root = tree.getroot()
            for i in root.iter('AccountDetails'):
                if i.find('Status').text == 'ACTIVE':
                    acc.append(i.find('AccountNo').text)
                else:
                    unactiv.append(i.find('AccountNo').text)

            ac_appl = []
            for i in sp:
                self.driver.implicitly_wait(3)

                try:
                    w = re.findall(r'\d{11,}',
                                   i.find_element_by_xpath(
                                       '//XCUIElementTypeCell/XCUIElementTypeStaticText').get_attribute(
                                       'name'))
                    w1 = re.findall(r'\d{11,}', i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[2]').get_attribute('name'))
                    if w:
                        ac_appl.append(w)
                    if w1:
                        ac_appl.append(w1)
                except:
                    pass
            for i in ac_appl:
                if str(i[0]) in acc:
                    pass
                else:
                    print str(i[0])
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
            unactiv = []
            tree = ET.parse('/Users/admin/PycharmProjects/OTP/xmls/enc_data.xml')
            root = tree.getroot()
            for i in root.iter('AccountDetails'):
                if i.find('Status').text == 'ACTIVE':
                    acc.append(i.find('AccountNo').text)
                else:
                    unactiv.append(i.find('AccountNo').text)

            ac_appl = []
            for i in sp:
                self.driver.implicitly_wait(3)

                try:
                    w = re.findall(r'\d{11,}',
                                   i.find_element_by_xpath(
                                       '//XCUIElementTypeCell/XCUIElementTypeStaticText').get_attribute(
                                       'name'))
                    w1 = re.findall(r'\d{11,}', i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[2]').get_attribute('name'))
                    if w:
                        ac_appl.append(w)
                    if w1:
                        ac_appl.append(w1)
                except:
                    pass
            for i in ac_appl:
                if str(i[0]) in acc:
                    pass
                else:
                    print str(i[0])
                    raise NameError('UnActive in active')

    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_29.png'
        self.driver.save_screenshot(directory + file_name)
        raise
