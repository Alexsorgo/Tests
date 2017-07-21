# -*- coding: utf-8 -*-
import os
import random
import re
import string
from time import sleep

from selenium.common.exceptions import NoSuchElementException

import main
from database.sms import first_id, find_sms
from login import login
from login_planshet import login_planshet


def del_mess(self):
    th = "".join([random.choice(string.letters) for i in xrange(85)])
    tx = "".join([random.choice(string.letters) for i in xrange(2001)])
    try:
        # f_id = first_id()
        lang = 0
        while lang < 3:
            try:
                # self.driver.find_element_by_id('OK').click()
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
        login_planshet(self, lang)

        if lang == 0:
            self.driver.implicitly_wait(15)
            sleep(4)
            try:
                allert = self.driver.find_element_by_id('No')
                allert.click()
            except NoSuchElementException:
                pass
            menu = self.driver.find_element_by_id('homePage')
            menu.click()
            arrow = self.driver.find_element_by_id('menuArrowBottom')
            arrow.click()
            mes = self.driver.find_element_by_id('Messages')
            mes.click()
            new_ms = self.driver.find_element_by_id('Sent')
            new_ms.click()
            sleep(3)
            msg = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText[2]')
            asrt = str(msg.get_attribute('name'))
            msg.click()
            sleep(2)
            dell = self.driver.find_element_by_id('actioniconMessageDelete')
            dell.click()
            self.assertTrue(self.driver.find_element_by_id('The message has been deleted'))
            self.driver.find_element_by_id('OK').click()
            self.driver.find_element_by_id('navBarBack').click()
            # msg2 = self.driver.find_element_by_xpath(
            #     '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText[2]')
            sleep(3)
            asrt2 = str(self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText[2]'))
            self.assertNotEqual(asrt, asrt2)

        elif lang == 1:
            self.driver.implicitly_wait(15)
            sleep(4)
            try:
                allert = self.driver.find_element_by_id('Нет')
                allert.click()
            except NoSuchElementException:
                pass
            menu = self.driver.find_element_by_id('homePage')
            menu.click()
            arrow = self.driver.find_element_by_id('menuArrowBottom')
            arrow.click()
            mes = self.driver.find_element_by_id('Сообщения')
            mes.click()
            new_ms = self.driver.find_element_by_id('Новое сообщение')
            new_ms.click()
            sleep(3)
            send = self.driver.find_element_by_id('icon send')
            theme = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField')
            text = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextView')

            theme.send_keys(th)
            arr = self.driver.find_element_by_id('arrow right normal')
            arr.click()
            text.send_keys(tx)
            send.click()
            sleep(5)
            self.assertTrue(self.driver.find_element_by_id('ОТПРАВЛЕННЫЕ'))
            msg = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText[2]')
            self.assertEqual(str(msg.get_attribute('name')), str(tx[:1800]))

        elif lang == 2:
            self.driver.implicitly_wait(15)
            sleep(4)
            try:
                allert = self.driver.find_element_by_id('Ні')
                allert.click()
            except NoSuchElementException:
                pass
            menu = self.driver.find_element_by_id('homePage')
            menu.click()
            arrow = self.driver.find_element_by_id('menuArrowBottom')
            arrow.click()
            mes = self.driver.find_element_by_id('Повідомлення')
            mes.click()
            new_ms = self.driver.find_element_by_id('Нове повідомлення')
            new_ms.click()
            sleep(3)
            send = self.driver.find_element_by_id('icon send')
            theme = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField')
            text = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextView')
            theme.send_keys(th)
            arr = self.driver.find_element_by_id('arrow right normal')
            arr.click()
            text.send_keys(tx)
            send.click()
            sleep(5)
            self.assertTrue(self.driver.find_element_by_id('ВІДПРАВЛЕНІ'))
            msg = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText[2]')
            self.assertEqual(str(msg.get_attribute('name')), str(tx[:1800]))


    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_41.png'
        self.driver.save_screenshot(directory + file_name)
        raise

