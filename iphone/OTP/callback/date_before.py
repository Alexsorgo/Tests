# -*- coding: utf-8 -*-
import os



def date_before(self):
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
            cb_login = self.driver.find_element_by_id('Request a call back')
            cb_login.click()
            self.assertTrue(self.driver.find_element_by_id('Select subject'))
            self.driver.find_element_by_id('Later').click()
            date = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable'
                                                    '/XCUIElementTypeCell[3]/XCUIElementTypeTextField')
            print date.text()
            try:
                date.send_keys('03.04.2017')
            except:
                print 'doesnt send'
                pass
        elif lang == 1:
            cb_login = self.driver.find_element_by_id('CallUp')
            cb_login.click()
            zvonok = self.driver.find_element_by_id('Заказать звонок из банка')
            zvonok.click()
            self.assertTrue(self.driver.find_element_by_id('Выберите тему'))
        elif lang == 2:
            cb_login = self.driver.find_element_by_id('CallUp')
            cb_login.click()
            cb_login = self.driver.find_element_by_id('Замовити дзвінок з банку')
            cb_login.click()
            self.assertTrue(self.driver.find_element_by_id('Виберіть тему'))

    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_14.png'
        self.driver.save_screenshot(directory + file_name)
        raise
