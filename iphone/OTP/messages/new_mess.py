# -*- coding: utf-8 -*-
import os
import random
import re
import string
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from iphone.OTP.login_planshet import login_planshet


def new_mess(self, login, passowrd):
    th = "".join([random.choice(string.letters) for i in xrange(5)])
    try:
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
        login_planshet(self, login, passowrd, lang)

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
            new_ms = self.driver.find_element_by_id('New message')
            new_ms.click()
            sleep(3)
            send = self.driver.find_element_by_id('icon send')
            theme = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField')
            text = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextView')
            send.click()
            sleep(1)
            error = self.driver.find_element_by_id('The message subject/body is missing')
            dism = self.driver.find_element_by_id('OK')
            self.assertTrue(error)
            dism.click()
            theme.send_keys(th)
            send.click()
            sleep(1)
            self.assertTrue(error)
            dism.click()
            text.send_keys(th)
            send.click()
            sleep(5)
            self.assertTrue(self.driver.find_element_by_id('SENT'))
            msg = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText[2]')
            self.assertEqual(msg.get_attribute('name'), th)

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
            send.click()
            sleep(1)
            error = self.driver.find_element_by_id('Отсутствует тема/текст сообщения')
            dism = self.driver.find_element_by_id('OK')
            self.assertTrue(error)
            dism.click()
            theme.send_keys(th)
            send.click()
            sleep(1)
            self.assertTrue(error)
            dism.click()
            text.send_keys(th)
            send.click()
            sleep(5)
            self.assertTrue(self.driver.find_element_by_id('ОТПРАВЛЕННЫЕ'))
            msg = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText[2]')
            self.assertEqual(msg.get_attribute('name'), th)

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
            send.click()
            sleep(1)
            error = self.driver.find_element_by_id('Відсутня тема/текст повідомлення')
            dism = self.driver.find_element_by_id('OK')
            self.assertTrue(error)
            dism.click()
            theme.send_keys(th)
            send.click()
            sleep(1)
            self.assertTrue(error)
            dism.click()
            text.send_keys(th)
            send.click()
            sleep(5)
            self.assertTrue(self.driver.find_element_by_id('ВІДПРАВЛЕНІ'))
            msg = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText[2]')
            self.assertEqual(msg.get_attribute('name'), th)


    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_39.png'
        self.driver.save_screenshot(directory + file_name)
        raise