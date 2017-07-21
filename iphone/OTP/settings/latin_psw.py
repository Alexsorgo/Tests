# -*- coding: utf-8 -*-
import os
import random
import string
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from iphone.OTP.login_planshet import login_planshet


def latin_psw(self, login, password):
    try:
        dt = u'Лат123'
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
            new_psw = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeSecureTextField')
            conf_psw = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeSecureTextField')
            conf_psw.send_keys(dt)
            new_psw.send_keys(dt)
            conf = self.driver.find_element_by_id('navBarOk')
            conf.click()
            sleep(3)
            self.assertTrue(self.driver.find_element_by_id('Password contains invalid characters: “Л, а, т”'))


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
            conf_psw.send_keys(dt)
            new_psw.send_keys(dt)
            conf = self.driver.find_element_by_id('navBarOk')
            conf.click()
            sleep(3)
            self.assertTrue(self.driver.find_element_by_id('Пароль содержит недопустимые символы: “Л, а, т”'))

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
            conf_psw.send_keys(dt)
            new_psw.send_keys(dt)
            conf = self.driver.find_element_by_id('navBarOk')
            conf.click()
            sleep(3)
            self.assertTrue(self.driver.find_element_by_id('Пароль містить неприпустимі символи: “Л, а, т”'))


    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_44.png'
        self.driver.save_screenshot(directory + file_name)
        raise
