# -*- coding: utf-8 -*-
import os
import re
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from iphone.OTP.database.sms import first_id, find_sms
from iphone.OTP.login_planshet import login_planshet


def a2a(self, login, password):
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
            scheta = self.driver.find_element_by_id('Between own accounts')
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
            sleep(7)
            account2 = self.driver.find_element_by_id('To the account')
            account2.click()
            self.driver.find_element_by_id('Done').click()
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
            vvod = self.driver.find_element_by_id('navBarNext')
            vvod.click()
            sleep(2)
            sum = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                '/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther'
                '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField')
            sum.send_keys(1)
            f_id = first_id(login)
            third_step = self.driver.find_element_by_id('navBarNext')
            third_step.click()
            ok_btn = self.driver.find_element_by_id('navBarOk')
            ok_btn.click()
            sleep(5)
            sms_code = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow[3]/XCUIElementTypeOther[2]/XCUIElementTypeAlert/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeSecureTextField')
            sms_code.send_keys(find_sms(f_id, login))
            # sms_code.send_keys(123456)
            conf = self.driver.find_element_by_id('Confirm')
            conf.click()
            self.assertTrue(self.driver.find_element_by_id('The payment has been successfully confirmed'))

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
            scheta = self.driver.find_element_by_id('Между своими счетами')
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
            sleep(7)
            account2 = self.driver.find_element_by_id('На счет')
            account2.click()
            self.driver.find_element_by_id('Done').click()
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
            vvod = self.driver.find_element_by_id('navBarNext')
            vvod.click()
            sleep(2)
            sum = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                '/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther'
                '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField')
            sum.send_keys(1)
            f_id = first_id(login)
            third_step = self.driver.find_element_by_id('navBarNext')
            third_step.click()
            ok_btn = self.driver.find_element_by_id('navBarOk')
            ok_btn.click()
            sleep(5)
            sms_code = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow[3]/XCUIElementTypeOther[2]/XCUIElementTypeAlert/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeSecureTextField')
            sms_code.send_keys(find_sms(f_id, login))
            # sms_code.send_keys(123456)
            conf = self.driver.find_element_by_id('Подтвердить')
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
            scheta = self.driver.find_element_by_id('Між своїми рахунками')
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
            sleep(7)
            account2 = self.driver.find_element_by_id('На рахунок')
            account2.click()
            self.driver.find_element_by_id('Done').click()
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
            vvod = self.driver.find_element_by_id('navBarNext')
            vvod.click()
            sleep(2)
            sum = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                '/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther'
                '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField')
            sum.send_keys(1)
            f_id = first_id(login)
            third_step = self.driver.find_element_by_id('navBarNext')
            third_step.click()
            ok_btn = self.driver.find_element_by_id('navBarOk')
            ok_btn.click()
            sleep(5)
            sms_code = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow[3]/XCUIElementTypeOther[2]/XCUIElementTypeAlert/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeSecureTextField')
            sms_code.send_keys(find_sms(f_id, login))
            # sms_code.send_keys(123456)
            conf = self.driver.find_element_by_id('Підтвердити')
            conf.click()
            self.assertTrue(self.driver.find_element_by_id('Платіж успішно підтверджений'))

    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_32.png'
        self.driver.save_screenshot(directory + file_name)
        raise