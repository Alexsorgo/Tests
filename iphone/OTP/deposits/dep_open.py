# -*- coding: utf-8 -*-
import os
import re
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from database.sms import first_id, find_sms
from login import login
from login_planshet import login_planshet


def dep_open(self):
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
            third_step = self.driver.find_element_by_id('navBarNext')
            third_step.click()
            sleep(2)
            third_step.click()
            sleep(30)
            ok_btn = self.driver.find_element_by_id('navBarOk')
            ok_btn.click()
            sleep(3)
            sms_code = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeAlert/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTextField')
            # # sms_code.send_keys(find_sms(f_id))
            sms_code.send_keys(123456)
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
            # # sms_code.send_keys(find_sms(f_id))
            sms_code.send_keys(123456)
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
            schet = self.driver.find_element_by_id('РАХУНОК СПИСАННЯ')
            schet.click()
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
            next = self.driver.find_element_by_id('navBarNext')
            next.click()
            dept = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeTextField/XCUIElementTypeButton')
            dept.click()
            seltype = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell')
            seltype.click()
            ok_btn = self.driver.find_element_by_id('navBarOk')
            ok_btn.click()
            srok = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeTextField/XCUIElementTypeButton')
            srok.click()
            srok2 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeSheet/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton')
            srok2.click()
            minsum = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[5]/XCUIElementTypeStaticText[2]')
            num = int(float(re.findall(r'\d+.\d{2}', minsum.get_attribute('name'))[0]) + float(1))
            sum = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[5]/XCUIElementTypeTextField')
            sum.send_keys(num)
            next.click()
            sleep(2)
            next.click()
            self.driver.implicitly_wait(130)
            # sleep(130)
            ok_btn2 = self.driver.find_element_by_id('navBarOk')
            ok_btn2.click()
            sms_code = self.driver.find_element_by_xpath(
                '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeAlert/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTextField')
            # sms_code.send_keys(find_sms(f_id))
            sms_code.send_keys(123456)
            conf = self.driver.find_element_by_id('Підтвердити')
            conf.click()
            self.driver.implicitly_wait(180)
            # sleep(120)
            self.assertTrue(self.driver.find_element_by_id(
                'Заявка на відкриття депозиту відправлена в банк. Статус заявки ви можете проконтролювати у списку заявок.'))

    except:
        directory = '%s/screenshots/' % os.getcwd()
        file_name = 'test_54.png'
        self.driver.save_screenshot(directory + file_name)
        raise