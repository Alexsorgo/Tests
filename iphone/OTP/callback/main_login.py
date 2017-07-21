# -*- coding: utf-8 -*-
import os



def main_login(self):
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

        if lang == 0:
            cb_login = self.driver.find_element_by_id('CallUp')
            cb_login.click()
            zvonok = self.driver.find_element_by_id('Request a call back')
        elif lang == 1:
            cb_login = self.driver.find_element_by_id('CallUp')
            cb_login.click()
            zvonok = self.driver.find_element_by_id('Заказать звонок из банка')
        elif lang == 2:
            cb_login = self.driver.find_element_by_id('CallUp')
            cb_login.click()
            zvonok = self.driver.find_element_by_id('Замовити дзвінок з банку')

        self.assertTrue(zvonok)

    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_25.png'
        self.driver.save_screenshot(directory + file_name)
        raise
