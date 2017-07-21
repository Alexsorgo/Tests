# -*- coding: utf-8 -*-
import os
import random
import string
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from database.main import sql_req
from login_planshet import login_planshet

from iphone.OTP.database.rules import passw_sql


def change_psw(self, login, password):
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
        login_planshet(self, login, password, lang)

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
            set = self.driver.find_element_by_id('Settings')
            set.click()
            ch_psw = self.driver.find_element_by_id('Change password')
            ch_psw.click()
            sleep(3)
            new_psw = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeSecureTextField')
            conf_psw = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeSecureTextField')
            conf_psw.send_keys(123)
            new_psw.send_keys(123)
            self.driver.find_element_by_id('navBarOk').click()
            sleep(3)
            self.assertEqual(str(self.driver.find_element_by_id('The password changed successfully').get_attribute('name')), 'The password changed successfully')
            self.driver.find_element_by_id('OK').click()
            sleep(3)
            self.assertTrue(self.driver.find_element_by_id('navigationTitleIcon'))


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
            set = self.driver.find_element_by_id('Настройки')
            set.click()
            ch_psw = self.driver.find_element_by_id('Смена пароля')
            ch_psw.click()
            sleep(3)
            new_psw = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeSecureTextField')
            conf_psw = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeSecureTextField')
            conf_psw.send_keys(123)
            new_psw.send_keys(123)
            self.driver.find_element_by_id('navBarOk').click()
            sleep(3)
            self.assertEqual(
                str(self.driver.find_element_by_id('Пароль успешно изменен').get_attribute('name')), '\xcf\xe0\xf0\xee\xeb\xfc \xf3\xf1\xef\xe5\xf8\xed\xee \xe8\xe7\xec\xe5\xed\xe5\xed')
            self.driver.find_element_by_id('OK').click()
            sleep(3)
            self.assertTrue(self.driver.find_element_by_id('navigationTitleIcon'))

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
            set = self.driver.find_element_by_id('Налаштування')
            set.click()
            ch_psw = self.driver.find_element_by_id('Зміна паролю')
            ch_psw.click()
            sleep(3)
            new_psw = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeSecureTextField')
            conf_psw = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeSecureTextField')
            conf_psw.send_keys(123)
            new_psw.send_keys(123)
            self.driver.find_element_by_id('navBarOk').click()
            sleep(3)
            self.assertEqual(
                str(self.driver.find_element_by_id('Пароль успішно змінено').get_attribute('name')),
                '\xcf\xe0\xf0\xee\xeb\xfc \xf3\xf1\xef\xb3\xf8\xed\xee \xe7\xec\xb3\xed\xe5\xed\xee')
            self.driver.find_element_by_id('OK').click()
            sleep(3)
            self.assertTrue(self.driver.find_element_by_id('navigationTitleIcon'))


    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_41.png'
        self.driver.save_screenshot(directory + file_name)
        raise

    finally:
        passw_sql(login)
