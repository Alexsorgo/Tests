# -*- coding: utf-8 -*-
import os

from selenium.common.exceptions import NoSuchElementException

from iphone.OTP.database.rules import rules
from iphone.OTP.login_planshet import login_planshet


def rule_46(self, login, password):
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
            self.driver.implicitly_wait(15)
            try:
                allert = self.driver.find_element_by_id('No')
                allert.click()
            except NoSuchElementException:
                pass
            menu = self.driver.find_element_by_id('homePage')
            menu.click()
            try:
                self.driver.find_element_by_id('Cards')
                raise NameError('Cards present')
            except NoSuchElementException:
                return True

        elif lang == 1:
            self.driver.implicitly_wait(15)
            try:
                allert = self.driver.find_element_by_id('Нет')
                allert.click()
            except NoSuchElementException:
                pass
            menu = self.driver.find_element_by_id('homePage')
            menu.click()
            try:
                self.driver.find_element_by_id('Карты')
                raise NameError('Cards present')
            except NoSuchElementException:
                return True

        elif lang == 2:
            self.driver.implicitly_wait(15)
            try:
                allert = self.driver.find_element_by_id('Ні')
                allert.click()
            except NoSuchElementException:
                pass
            menu = self.driver.find_element_by_id('homePage')
            menu.click()
            try:
                self.driver.find_element_by_id('Картки')
                raise NameError('Cards present')
            except NoSuchElementException:
                return True

    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_22.png'
        self.driver.save_screenshot(directory + file_name)
        raise

    finally:
        rules(46, login)
