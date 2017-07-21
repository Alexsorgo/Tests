# -*- coding: utf-8 -*-
import os

from selenium.common.exceptions import NoSuchElementException

from iphone.OTP.database.rules import rules
from iphone.OTP.login_planshet import login_planshet


def rule_20(self, login, password):
    try:
        rules(20, login)
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
        try:
            # login(self, lang)
            login_planshet(self, login, password, lang)
        except NoSuchElementException:
            pass
        if lang == 0:
            self.assertTrue(
                self.driver.find_element_by_id("The user doesn't have enough rights to finish the action"))
        elif lang == 1:
            self.assertTrue(
                self.driver.find_element_by_id('У пользователя недостаточно прав для завершения данного действия'))
        elif lang == 2:
            self.assertTrue(
                self.driver.find_element_by_id('У користувача недостатньо прав для завершення даної дії'))
    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_15.png'
        self.driver.save_screenshot(directory + file_name)
        raise
    finally:
        rules(20, login)