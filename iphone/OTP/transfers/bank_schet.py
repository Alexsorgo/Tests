# -*- coding: utf-8 -*-
import os
import re
from time import sleep

from selenium.common.exceptions import NoSuchElementException

import constants
from iphone.OTP.database.sms import first_id, find_sms
from iphone.OTP.login_planshet import login_planshet


def bank_schet(self, login, password):
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
            menu = self.driver.find_element_by_id('homePage')
            menu.click()
            bil = self.driver.find_element_by_id('Transfers')
            bil.click()
            new_trans = self.driver.find_element_by_id('New transfers')
            new_trans.click()
            scheta = self.driver.find_element_by_id('Within the bank')
            scheta.click()
            new_schet = self.driver.find_element_by_id('New')
            new_schet.click()
            account = self.driver.find_element_by_id('From account')
            account.click()
            sleep(3)
            self.driver.find_element_by_id('Done').click()
            sleep(3)
            sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
            sp.remove(sp[len(sp) - 1])
            for i in sp:
                w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText')
                w1 = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[3]')
                # w = re.findall(r'\d+.\d{2}\s\w{3}', i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText').get_attribute('name'))
                # w1 = re.findall(r'\d+.\d{2}\s\w{3}', i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[3]').get_attribute('name'))
                if not re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')):
                    if len(re.findall(r'\d+.\d{2}', w1.get_attribute('name'))[0]) > 4:
                        print len(re.findall(r'\d+.\d{2}', w1.get_attribute('name'))[0])
                        self.driver.execute_script('mobile: scroll', {"element": w1, "toVisible": True})
                        w1.click()
                        break
                elif not re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')):
                    if len(re.findall(r'\d+.\d{2}', w.get_attribute('name'))[0]) > 4:
                        print re.findall(r'\d+.\d{2}', w.get_attribute('name'))[0]
                        self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                        w.click()
                        break

            credit = self.driver.find_element_by_id('navBarNext')
            credit.click()

            sleep(3)
            poluchat = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField')
            naimenovan = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
            id_poluch = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeTextField')
            id_poluch.send_keys(constants.bank_inn)
            naimenovan.send_keys(constants.name)
            poluchat.send_keys(constants.bank_accno)

            step2 = self.driver.find_element_by_id('navBarNext')
            step2.click()

            sleep(3)
            amount = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField')
            info = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextView')
            amount.send_keys(1)
            f_id = first_id(login)
            self.driver.find_element_by_id('OK').click()
            info.send_keys('some text')
            step2.click()

            sleep(3)
            self.driver.find_element_by_id('navBarOk').click()
            sleep(3)

            sms = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow[3]/XCUIElementTypeOther[2]/XCUIElementTypeAlert/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeSecureTextField')
            conf = self.driver.find_element_by_id('Confirm')
            sms.send_keys(find_sms(f_id, login))
            # sms.send_keys(123456)
            conf.click()
            self.assertTrue(self.driver.find_element_by_id('The payment has been successfully confirmed'))
            """ Нет подтверждения, сервер не работает """

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
            perevodi = self.driver.find_element_by_id('Переводы')
            perevodi.click()
            perevodi = self.driver.find_element_by_id('Новый платеж')
            perevodi.click()
            scheta = self.driver.find_element_by_id('Внутри банка')
            scheta.click()
            new_schet = self.driver.find_element_by_id('Новый')
            new_schet.click()
            account = self.driver.find_element_by_id('Со счета')
            account.click()
            sleep(3)
            self.driver.find_element_by_id('Done').click()
            sleep(3)
            sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
            sp.remove(sp[len(sp) - 1])
            for i in sp:
                w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText')
                w1 = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[3]')
                # w = re.findall(r'\d+.\d{2}\s\w{3}', i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText').get_attribute('name'))
                # w1 = re.findall(r'\d+.\d{2}\s\w{3}', i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[3]').get_attribute('name'))
                if not re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')):
                    if len(re.findall(r'\d+.\d{2}', w1.get_attribute('name'))[0]) > 4:
                        print len(re.findall(r'\d+.\d{2}', w1.get_attribute('name'))[0])
                        self.driver.execute_script('mobile: scroll', {"element": w1, "toVisible": True})
                        w1.click()
                        break
                elif not re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')):
                    if len(re.findall(r'\d+.\d{2}', w.get_attribute('name'))[0]) > 4:
                        print re.findall(r'\d+.\d{2}', w.get_attribute('name'))[0]
                        self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                        w.click()
                        break

            credit = self.driver.find_element_by_id('navBarNext')
            credit.click()

            sleep(3)
            poluchat = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField')
            naimenovan = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
            id_poluch = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeTextField')
            id_poluch.send_keys(constants.bank_inn)
            naimenovan.send_keys(constants.name)
            poluchat.send_keys(constants.bank_accno)

            step2 = self.driver.find_element_by_id('navBarNext')
            step2.click()

            sleep(3)
            amount = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField')
            info = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextView')
            amount.send_keys(1)
            f_id = first_id(login)
            self.driver.find_element_by_id('OK').click()
            info.send_keys('some text')
            step2.click()

            sleep(3)
            self.driver.find_element_by_id('navBarOk').click()
            sleep(3)

            sms = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow[3]/XCUIElementTypeOther[2]/XCUIElementTypeAlert/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeSecureTextField')
            conf = self.driver.find_element_by_id('Подтвердить')
            sms.send_keys(find_sms(f_id, login))
            # sms.send_keys(123456)
            conf.click()
            self.assertTrue(self.driver.find_element_by_id('Платеж успешно подтвержден'))

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
            bil = self.driver.find_element_by_id('Перекази')
            bil.click()
            new_trans = self.driver.find_element_by_id('Новий переказ')
            new_trans.click()
            scheta = self.driver.find_element_by_id('В межах банку')
            scheta.click()
            new_schet = self.driver.find_element_by_id('Новий')
            new_schet.click()
            account = self.driver.find_element_by_id('З рахунку')
            account.click()
            sleep(3)
            self.driver.find_element_by_id('Done').click()
            sleep(3)
            sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
            sp.remove(sp[len(sp) - 1])
            for i in sp:
                w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText')
                w1 = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[3]')
                # w = re.findall(r'\d+.\d{2}\s\w{3}', i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText').get_attribute('name'))
                # w1 = re.findall(r'\d+.\d{2}\s\w{3}', i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[3]').get_attribute('name'))
                if not re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')):
                    if len(re.findall(r'\d+.\d{2}', w1.get_attribute('name'))[0]) > 4:
                        print len(re.findall(r'\d+.\d{2}', w1.get_attribute('name'))[0])
                        self.driver.execute_script('mobile: scroll', {"element": w1, "toVisible": True})
                        w1.click()
                        break
                elif not re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')):
                    if len(re.findall(r'\d+.\d{2}', w.get_attribute('name'))[0]) > 4:
                        print re.findall(r'\d+.\d{2}', w.get_attribute('name'))[0]
                        self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                        w.click()
                        break

            credit = self.driver.find_element_by_id('navBarNext')
            credit.click()

            sleep(3)
            poluchat = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField')
            naimenovan = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
            id_poluch = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeTextField')
            id_poluch.send_keys(constants.bank_inn)
            naimenovan.send_keys(constants.name)
            poluchat.send_keys(constants.bank_accno)

            step2 = self.driver.find_element_by_id('navBarNext')
            step2.click()

            sleep(3)
            amount = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField')
            info = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextView')
            amount.send_keys(1)
            f_id = first_id(login)
            self.driver.find_element_by_id('OK').click()
            info.send_keys('some text')
            step2.click()

            sleep(3)
            self.driver.find_element_by_id('navBarOk').click()
            sleep(3)

            sms = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow[3]/XCUIElementTypeOther[2]/XCUIElementTypeAlert/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeSecureTextField')
            conf = self.driver.find_element_by_id('Підтвердити')
            sms.send_keys(find_sms(f_id, login))
            # sms.send_keys(123456)
            conf.click()
            self.assertTrue(self.driver.find_element_by_id('Платіж успішно підтверджений'))


    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_35.png'
        self.driver.save_screenshot(directory + file_name)
        raise