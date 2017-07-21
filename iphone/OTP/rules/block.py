# -*- coding: utf-8 -*-
import os

from selenium.common.exceptions import NoSuchElementException


from iphone.OTP.database.rules import user_block
from iphone.OTP.login_planshet import login_planshet


def block(self, login, password):
    try:
        user_block(login)
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
                self.driver.find_element_by_id("The specified user has been blocked. Contact the bank."))
        elif lang == 1:
            self.assertTrue(
                self.driver.find_element_by_id('Заданный пользователь заблокирован. Обратитесь в банк.'))
        elif lang == 2:
            self.assertTrue(
                self.driver.find_element_by_id('Зазначеного користувача заблоковано. Зверніться до банку.'))
    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_16.png'
        self.driver.save_screenshot(directory + file_name)
        raise
    finally:
        user_block(login)
