# -*- coding: utf-8 -*-
import os

from selenium.common.exceptions import NoSuchElementException

from iphone.OTP.database.rules import rules
from iphone.OTP.login_planshet import login_planshet


def no_auth(self, login, password):
    try:
        rules(1,login)
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
            self.assertTrue(self.driver.find_element_by_id("It is impossible to log in to the system, because you do not have rights to enter the system."))
        elif lang == 1:
            self.assertTrue(self.driver.find_element_by_id('Подключение к системе невозможно, так как у вас нет прав на вход в систему.'))
        elif lang == 2:
            self.assertTrue(self.driver.find_element_by_id('Підключення до системи неможливе, у вас немає прав на вхід у систему.'))
    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_14.png'
        self.driver.save_screenshot(directory + file_name)
        raise
    finally:
        rules(1, login)