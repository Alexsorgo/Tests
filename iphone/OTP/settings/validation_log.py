# -*- coding: utf-8 -*-
import os
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from iphone.OTP.login_planshet import login_planshet


def validation_log(self, login, password):
    new = 'qwerty1'
    conf = 'qwerty2'
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
            appl = self.driver.find_element_by_id('navBarOk')
            appl.click()
            self.assertTrue(self.driver.find_element_by_id(
                'The login should be 6 to 50 characters long (Latin symbols, numbers 0-9, symbols @ _ ~)'))
            self.driver.find_element_by_id('OK').click()
            conf_lgn.send_keys(new)
            new_lgn.send_keys(conf)
            appl.click()
            self.assertTrue(self.driver.find_element_by_id(
                'Make sure that values of the fields «New login» and «Confirm New login» are identical'))


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
            appl = self.driver.find_element_by_id('navBarOk')
            appl.click()
            self.assertTrue(self.driver.find_element_by_id('Логин должен содержать от 6 до 50 символов (латинские буквы, цифры 0-9, символы @ _ ~)'))
            self.driver.find_element_by_id('OK').click()
            conf_lgn.send_keys(new)
            new_lgn.send_keys(conf)
            appl.click()
            self.assertTrue(self.driver.find_element_by_id(
                'Значения полей «Новый логин» и «Подтвердить логин» должны совпадать'))

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
            appl = self.driver.find_element_by_id('navBarOk')
            appl.click()
            sleep(2)
            print self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow[4]/XCUIElementTypeOther[2]/XCUIElementTypeAlert/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText[2]').get_attribute('name')
            self.assertTrue(self.driver.find_element_by_id('Логін має містити від 6 до 50 символів (латинські літери, цифри 0-9, символи  @ _ ~)'))
            self.driver.find_element_by_id('OK').click()
            conf_lgn.send_keys(new)
            new_lgn.send_keys(conf)
            appl.click()
            self.assertTrue(self.driver.find_element_by_id(
                'Значення полів «Новий логін» та «Підтвердити логін» мають співпадати'))


    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_50.png'
        self.driver.save_screenshot(directory + file_name)
        raise
