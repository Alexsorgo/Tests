# -*- coding: utf-8 -*-
import os
import re
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from database.sms import find_sms, first_id
from login import login
from login_planshet import login_planshet


def c2occ_inc(self):
    in1 = '9898'
    in2 = '9123'
    in3 = '5654'
    in4 = '0023'

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
        login_planshet(self, lang)

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
            scheta = self.driver.find_element_by_id('Transfer to card of another client of bank')
            scheta.click()
            new_schet = self.driver.find_element_by_id('New')
            new_schet.click()
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
                        print re.findall(r'\d+.\d{2}', w1.get_attribute('name'))[0]
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
            inp1 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField')
            inp2 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField[2]')
            inp3 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField[3]')
            inp4 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField[4]')
            inp1.send_keys(in1)
            inp2.send_keys(in2)
            inp3.send_keys(in3)
            inp4.send_keys(in4)
            self.assertTrue(self.driver.find_element_by_id('Transfers can be made only to cards issued by the bank'))
            # vvod = self.driver.find_element_by_id('navBarNext')
            # vvod.click()
            # sleep(2)
            # sum = self.driver.find_element_by_xpath(
            #     '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField')
            # sum.send_keys(1)
            # third_step = self.driver.find_element_by_id('navBarNext')
            # third_step.click()
            # ok_btn = self.driver.find_element_by_id('navBarOk')
            # ok_btn.click()
            # sleep(5)
            # sms_code = self.driver.find_element_by_xpath(
            #     '/XCUIElementTypeApplication/XCUIElementTypeWindow[3]/XCUIElementTypeOther[2]/XCUIElementTypeAlert/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeSecureTextField')
            # # sms_code.send_keys(find_sms(f_id))
            # sms_code.send_keys(123456)
            # conf = self.driver.find_element_by_id('Confirm')
            # conf.click()
            # self.assertTrue(self.driver.find_element_by_id('The payment has been successfully confirmed'))
            # """ Нет подтверждения, сервер не работает """

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
            scheta = self.driver.find_element_by_id('Перевод на карту другого клиента банка')
            scheta.click()
            new_schet = self.driver.find_element_by_id('Новый')
            new_schet.click()
            sleep(3)
            self.driver.find_element_by_id('Done').click()
            sleep(3)
            sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
            sp.remove(sp[len(sp) - 1])
            for i in sp:
                w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText')
                w1 = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[3]')
                if not re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')):
                    if len(re.findall(r'\d+.\d{2}', w1.get_attribute('name'))[0]) > 4:
                        print re.findall(r'\d+.\d{2}', w1.get_attribute('name'))[0]
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
            inp1 = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField')
            inp2 = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField[2]')
            inp3 = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField[3]')
            inp4 = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField[4]')
            inp1.send_keys(in1)
            inp2.send_keys(in2)
            inp3.send_keys(in3)
            inp4.send_keys(in4)
            self.assertTrue(self.driver.find_element_by_id('Перевод можно осуществить только на карту, выпущенную банком'))

            # vvod = self.driver.find_element_by_id('navBarNext')
            # vvod.click()
            # sleep(2)
            # sum = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField')
            # sum.send_keys(1)
            # third_step = self.driver.find_element_by_id('navBarNext')
            # third_step.click()
            # ok_btn = self.driver.find_element_by_id('navBarOk')
            # ok_btn.click()
            # sleep(5)
            # sms_code = self.driver.find_element_by_xpath(
            #     '/XCUIElementTypeApplication/XCUIElementTypeWindow[3]/XCUIElementTypeOther[2]/XCUIElementTypeAlert/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeSecureTextField')
            # # sms_code.send_keys(find_sms(f_id))
            # sms_code.send_keys(123456)
            # conf = self.driver.find_element_by_id('Подтвердить')
            # conf.click()
            # self.assertTrue(self.driver.find_element_by_id('Платеж успешно подтвержден'))
            # """ Нет подтверждения, сервер не работает """


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
            scheta = self.driver.find_element_by_id('Переказ на карту іншого клієнта банку')
            scheta.click()
            new_schet = self.driver.find_element_by_id('Новий')
            new_schet.click()
            sleep(3)
            self.driver.find_element_by_id('Done').click()
            sleep(3)
            sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
            sp.remove(sp[len(sp) - 1])
            for i in sp:
                w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText')
                w1 = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[3]')
                if not re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')):
                    if len(re.findall(r'\d+.\d{2}', w1.get_attribute('name'))[0]) > 4:
                        print re.findall(r'\d+.\d{2}', w1.get_attribute('name'))[0]
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
            inp1 = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField')
            inp2 = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField[2]')
            inp3 = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField[3]')
            inp4 = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField[4]')
            inp1.send_keys(in1)
            inp2.send_keys(in2)
            inp3.send_keys(in3)
            inp4.send_keys(in4)
            self.assertTrue(self.driver.find_element_by_id('Переказ можна здійснити тільки на карту, випущену банком'))

            # vvod = self.driver.find_element_by_id('navBarNext')
            # vvod.click()
            # sleep(2)
            # sum = self.driver.find_element_by_xpath(
            #     '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField')
            # sum.send_keys(1)
            # third_step = self.driver.find_element_by_id('navBarNext')
            # third_step.click()
            # ok_btn = self.driver.find_element_by_id('navBarOk')
            # ok_btn.click()
            # sleep(5)
            # sms_code = self.driver.find_element_by_xpath(
            #     '/XCUIElementTypeApplication/XCUIElementTypeWindow[3]/XCUIElementTypeOther[2]/XCUIElementTypeAlert/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeSecureTextField')
            # # sms_code.send_keys(find_sms(f_id))
            # sms_code.send_keys(123456)
            # conf = self.driver.find_element_by_id('Підтвердити')
            # conf.click()
            # self.assertTrue(self.driver.find_element_by_id('Платіж успішно підтверджений'))
            # """ Нет подтверждения, сервер не работает """

    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_51.png'
        self.driver.save_screenshot(directory + file_name)
        raise