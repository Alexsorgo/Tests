# -*- coding: utf-8 -*-
import os
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from iphone.OTP.login_planshet import login_planshet


def busy_log(self, login, password):
    dt = 'HENDRIX'
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
            ch_psw = self.driver.find_element_by_id('Change login')
            ch_psw.click()
            sleep(3)
            new_lgn = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField')
            conf_lgn = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField[2]')
            conf_lgn.send_keys(dt)
            new_lgn.send_keys(dt)
            self.driver.find_element_by_id('navBarOk').click()
            sleep(3)
            self.assertTrue(self.driver.find_element_by_id("Such login has already been registered in the system. Please create another login."))


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
            ch_lgn = self.driver.find_element_by_id('Смена логина')
            ch_lgn.click()
            sleep(3)
            new_lgn = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField')
            conf_lgn = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField[2]')
            conf_lgn.send_keys(dt)
            new_lgn.send_keys(dt)
            self.driver.find_element_by_id('navBarOk').click()
            sleep(3)
            self.assertTrue(self.driver.find_element_by_id("Такой логин уже зарегистрирован в системе. Пожалуйста, придумайте другой логин."))

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
            ch_psw = self.driver.find_element_by_id('Зміна логін')
            ch_psw.click()
            sleep(3)
            new_lgn = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField')
            conf_lgn = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField[2]')
            conf_lgn.send_keys(dt)
            new_lgn.send_keys(dt)
            self.driver.find_element_by_id('navBarOk').click()
            sleep(3)
            self.assertTrue(self.driver.find_element_by_id("Такий логін вже зареєстровано в системі. Будь ласка, придумайте інший логин."))


    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_47.png'
        self.driver.save_screenshot(directory + file_name)
        raise
