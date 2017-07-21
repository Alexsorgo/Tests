# -*- coding: utf-8 -*-
import os

from iphone.OTP.login_planshet import login_planshet


def in_login(self, login, password):
    try:
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

        login_planshet(self, login, password+'4', lang)

        if lang == 0:
            zvonok = self.driver.find_element_by_id('Request a call back')
        elif lang == 1:
            zvonok = self.driver.find_element_by_id('Заказать звонок из банка')
        elif lang == 2:
            zvonok = self.driver.find_element_by_id('Замовити дзвінок з банку')
        self.assertTrue(zvonok)

    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_24.png'
        self.driver.save_screenshot(directory + file_name)
        raise
