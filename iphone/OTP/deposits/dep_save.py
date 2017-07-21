# -*- coding: utf-8 -*-
import os
import re
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from iphone.OTP.database.sms import find_sms, first_id
from iphone.OTP.login_planshet import login_planshet


def dep_save(self, login, password):
    try:
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
            self.driver.find_element_by_id('Available on accounts:').click()
            self.driver.find_element_by_id('Available on cards:').click()
            self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[3]').click()
            sleep(1)
            self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[4]').click()
            depop = self.driver.find_element_by_id('OPEN DEPOSIT')
            depop.click()
            saving = self.driver.find_element_by_id('Savings deposit')
            saving.click()
            valuta = self.driver.find_element_by_id('UAH')
            valuta.click()
            sleep(10)
            self.driver.find_element_by_id('bankListicon').click()
            sleep(1)
            deptype = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell')
            deptype.click()
            ok_btn = self.driver.find_element_by_id('navBarOk')
            ok_btn.click()
            f_id = first_id(login)
            third_step = self.driver.find_element_by_id('navBarNext')
            third_step.click()
            sleep(2)
            third_step.click()
            sleep(30)
            ok_btn = self.driver.find_element_by_id('navBarOk')
            ok_btn.click()
            sleep(3)
            sms_code = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeAlert/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTextField')
            sms_code.send_keys(find_sms(f_id, login))
            # sms_code.send_keys(123456)
            conf = self.driver.find_element_by_id('Confirm')
            conf.click()
            sleep(30)
            self.assertTrue(self.driver.find_element_by_id('The request for depositing money sent to the bank. You can check the request state in the list of requests.'))

        elif lang == 1:
            self.driver.implicitly_wait(15)
            sleep(4)
            try:
                allert = self.driver.find_element_by_id('Нет')
                allert.click()
            except NoSuchElementException:
                pass
            self.driver.find_element_by_id('Доступно на счетах:').click()
            self.driver.find_element_by_id('Доступно на картах:').click()
            self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[3]').click()
            sleep(1)
            self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[4]').click()
            depop = self.driver.find_element_by_id('ОТКРЫТЬ ДЕПОЗИТ')
            depop.click()
            saving = self.driver.find_element_by_id('Сберегательный депозит')
            saving.click()
            valuta = self.driver.find_element_by_id('UAH')
            valuta.click()
            sleep(10)
            self.driver.find_element_by_id('bankListicon').click()
            sleep(1)
            deptype = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell')
            deptype.click()
            ok_btn = self.driver.find_element_by_id('navBarOk')
            ok_btn.click()
            f_id = first_id(login)
            third_step = self.driver.find_element_by_id('navBarNext')
            third_step.click()
            sleep(2)
            third_step.click()
            sleep(30)
            ok_btn = self.driver.find_element_by_id('navBarOk')
            ok_btn.click()
            sleep(3)
            sms_code = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeAlert/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTextField')
            sms_code.send_keys(find_sms(f_id, login))
            # sms_code.send_keys(123456)
            conf = self.driver.find_element_by_id('Подтвердить')
            conf.click()
            sleep(30)
            self.assertTrue(self.driver.find_element_by_id(
                'Заявка на открытие депозита отправлена в банк. Статус заявки можно проконтролировать в списке заявок.'))


        elif lang == 2:
            self.driver.implicitly_wait(15)
            sleep(4)
            try:
                allert = self.driver.find_element_by_id('Ні')
                allert.click()
            except NoSuchElementException:
                pass
            self.driver.find_element_by_id('Доступно на рахунках').click()
            self.driver.find_element_by_id('Доступно на картах').click()
            self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[3]').click()
            sleep(1)
            self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[4]').click()
            depop = self.driver.find_element_by_id('ВІДКРИТИ ДЕПОЗИТ')
            depop.click()
            saving = self.driver.find_element_by_id('Ощадний депозит')
            saving.click()
            valuta = self.driver.find_element_by_id('UAH')
            valuta.click()
            sleep(10)
            self.driver.find_element_by_id('bankListicon').click()
            sleep(1)
            deptype = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell')
            deptype.click()
            ok_btn = self.driver.find_element_by_id('navBarOk')
            ok_btn.click()
            f_id = first_id(login)
            third_step = self.driver.find_element_by_id('navBarNext')
            third_step.click()
            sleep(2)
            third_step.click()
            sleep(30)
            ok_btn = self.driver.find_element_by_id('navBarOk')
            ok_btn.click()
            sleep(3)
            sms_code = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeAlert/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTextField')
            sms_code.send_keys(find_sms(f_id, login))
            # sms_code.send_keys(123456)
            conf = self.driver.find_element_by_id('Підтвердити')
            conf.click()
            sleep(30)
            self.assertTrue(self.driver.find_element_by_id(
                'Заявка на відкриття депозиту відправлена в банк. Статус заявки ви можете проконтролювати у списку заявок.'))

    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_53.png'
        self.driver.save_screenshot(directory + file_name)
        raise