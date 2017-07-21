# -*- coding: utf-8 -*-
import re
import unittest
import os

from selenium.webdriver.support.wait import WebDriverWait

from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
from login import login
from time import sleep
from databse import OracleDB, find_sms


class Version(unittest.TestCase):

    vbanke = '28095000017689'
    mfo = '305299'
    accno = '26200603301352'
    name = 'Ivanov'
    inn = '2498510800'
    cardno = '4029619999999937'

    def setUp(self):
        # set up appium
        app = os.path.abspath('/Users/admin/Desktop/Pivdenny/Pivdenny.ipa')
        # app = os.path.abspath('/Users/admin/Library/Developer/Xcode/DerivedData/Pivdenny-fcnzskefhvzrvxfchcoiershcrfb/Build/Products/Debug-iphonesimulator/Pivdenny.app')
        self.driver = webdriver.Remote(
            command_executor='http://0.0.0.0:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'appium-version': '1.6.3',
                'platformName': 'iOS',
                'platformVersion': '10.0.2',
                # 'deviceName': 'iPhone 7',
                'deviceName': 'iPhone 6s',
                'udid': 'f3b0308a80a4dba925ece9652d9c3159a9af5cb5',
                'launchTimeout': 500000,
                # 'automationName': 'XCUITest'
            })

    def tearDown(self):
        self.driver.quit()

    # Логин с невалидными значениями
    # def test_02(self):
    #     lang = 0
    #     try:
    #         self.driver.implicitly_wait(10)
    #         log = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther[2]/XCUIElementTypeTextField')
    #         while lang < 3:
    #             try:
    #                 if lang == 0:
    #                     self.driver.find_element_by_id('Remember login?')
    #                 elif lang == 1:
    #                     self.driver.find_element_by_id('Запомнить логин?')
    #                 elif lang == 2:
    #                     self.driver.find_element_by_id("Запам'ятати логін?")
    #                 break
    #             except:
    #                 lang += 1
    #         if lang == 0:
    #             log.clear()
    #             log.send_keys('SORGO')
    #             pas = self.driver.find_element_by_xpath(
    #                 '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
    #                 '/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther['
    #                 '2]/XCUIElementTypeSecureTextField')
    #             pas.send_keys('555556')
    #             self.driver.find_element_by_id('Log in').click()
    #             self.assertTrue(self.driver.find_element_by_id(
    #                 'It is impossible to login. Check if the login and password are correct.'))
    #         elif lang == 1:
    #             log.clear()
    #             log.send_keys('SORGO')
    #             pas = self.driver.find_element_by_xpath(
    #                 '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
    #                 '/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther['
    #                 '2]/XCUIElementTypeSecureTextField')
    #             pas.send_keys('555556')
    #             self.driver.find_element_by_id('Войти').click()
    #             self.assertTrue(self.driver.find_element_by_id(
    #                 'Подключение к системе невозможно. Проверьте корректность логина и пароля.'))
    #         elif lang == 2:
    #             log.clear()
    #             log.send_keys('SORGO')
    #             pas = self.driver.find_element_by_xpath(
    #                 '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
    #                 '/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeOther['
    #                 '2]/XCUIElementTypeSecureTextField')
    #             pas.send_keys('555556')
    #             self.driver.find_element_by_id('Увійти').click()
    #             self.assertTrue(self.driver.find_element_by_id(
    #                 'Підключення до системи неможливе. Перевірте коректність логіна і паролю.'))
    #         else:
    #             directory = '%s/screenshots/' % os.getcwd()
    #             file_name = 'test_02.png'
    #             self.driver.save_screenshot(directory + file_name)
    #             raise
    #     except:
    #         directory = '%s/screenshots/' % os.getcwd()
    #         file_name = 'test_02.png'
    #         self.driver.save_screenshot(directory + file_name)
    #         raise
    #
    #
    # Проверка версии
    def test_01(self):
        try:
            self.driver.implicitly_wait(15)
            check = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                      '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                      '/XCUIElementTypeOther/XCUIElementTypeImage'
                                                      '/XCUIElementTypeOther[3]/XCUIElementTypeStaticText')
            print check.get_attribute('value').split(' ')[2]
            self.assertEqual(check.get_attribute('value').split(' ')[2], '1.2.0.1131')
        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_01.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # Логин с валидным значением
    def test_03(self):
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
        login(self, lang)

    # Перевод между своими счетами с карты на карту
    def test_04(self):
        try:
            db = OracleDB()
            db.connect()
            db.cursor.execute(
                "select * from IFOBSSMSDELIVERY where userid = (select id from users where login ='SORGO') order by id desc")
            wtf = [x for x in db.cursor]
            print
            first_id = wtf[0][0]
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
            login(self, lang)
            print lang

            if lang == 0:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Payments')
                bil.click()
                scheta = self.driver.find_element_by_id('Between own accounts')
                scheta.click()
                new_schet = self.driver.find_element_by_id('New')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Pay from')
                popolnenie = self.driver.find_element_by_id('Pay to')
                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeTextField')

                spisanie.click()
                sleep(45)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')

                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        print re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w1.get_attribute('name'))[0].lstrip(' ')) > 5

                        if re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w1.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w1, "toVisible": True})
                            w1.click()
                            break
                        else:
                            pass

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        print re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5

                        if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                            w.click()
                            break
                        else:
                            pass

                popolnenie.click()
                sleep(45)
                spisok2 = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                spisok2.remove(spisok2[0])
                print spisok2
                for i in spisok2:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')

                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH':
                            self.driver.execute_script('mobile: scroll', {"element": w1, "toVisible": True})
                            w1.click()
                            break
                        else:
                            pass

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH':
                            self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                            w.click()
                            break
                        else:
                            pass
                summa.send_keys(50)
                dal = self.driver.find_element_by_id('Next')
                dal.click()
                sleep(2)
                sen = self.driver.find_element_by_id('Pay')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Confirm')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'The payment has been confirmed'))

            elif lang == 1:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Платежи')
                bil.click()
                scheta = self.driver.find_element_by_id('Между своими счетами')
                scheta.click()
                new_schet = self.driver.find_element_by_id('Новый')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Выберите счет списания')
                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeTextField')

                spisanie.click()
                sleep(45)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')

                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w1.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w1, "toVisible": True})
                            w1.click()
                            break
                        else:
                            pass

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                            w.click()
                            break
                        else:
                            pass
                popolnenie = self.driver.find_element_by_id('Выберите счет пополнения')
                popolnenie.click()
                sleep(45)
                spisok2 = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                spisok2.remove(spisok2[0])
                print spisok2
                for i in spisok2:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')

                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH':
                            self.driver.execute_script('mobile: scroll', {"element": w1, "toVisible": True})
                            w1.click()
                            break
                        else:
                            pass

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH':
                            self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                            w.click()
                            break
                        else:
                            pass
                summa.send_keys(50)
                dal = self.driver.find_element_by_id('Далее')
                dal.click()
                sen = self.driver.find_element_by_id('Оплатить')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                             '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                             '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                             '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                             '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                             '/XCUIElementTypeCell/XCUIElementTypeTable'
                                                             '/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Подтвердить')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                        'Платеж подтвержден'))

            elif lang == 2:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Платежі')
                bil.click()
                scheta = self.driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name = 'Між своїми рахунками']")
                scheta.click()
                new_schet = self.driver.find_element_by_id('Новий')
                new_schet.click()
                self.driver.implicitly_wait(30)
                spisanie = self.driver.find_element_by_id('Виберіть рахунок списання')
                popolnenie = self.driver.find_element_by_id('Виберіть рахунок поповнення')
                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeTextField')

                spisanie.click()
                # self.driver.page_source
                self.driver.implicitly_wait(45)
                sleep(40)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')
                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w1.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w1, "toVisible": True})
                            w1.click()
                            break
                        else:
                            pass

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                            w.click()
                            break
                        else:
                            pass

                popolnenie.click()
                self.driver.implicitly_wait(45)
                sleep(45)
                spisok2 = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                spisok2.remove(spisok2[0])
                print spisok2
                for i in spisok2:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')

                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH':
                            self.driver.execute_script('mobile: scroll', {"element": w1, "toVisible": True})
                            w1.click()
                            break
                        else:
                            pass

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH':
                            self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                            w.click()
                            break
                        else:
                            pass
                summa.send_keys(50)
                dal = self.driver.find_element_by_id('Далі')
                dal.click()
                sen = self.driver.find_element_by_id('Сплатити')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Підтвердити')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                'Платіж підтверджено'))
        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_04.png'
            self.driver.save_screenshot(directory + file_name)
            raise


    # Перевод в пределах банка
    def test_05(self):
        db = OracleDB()
        db.connect()
        db.cursor.execute(
            "select * from IFOBSSMSDELIVERY where userid = (select id from users where login ='SORGO') order by id desc")
        wtf = [x for x in db.cursor]
        print
        first_id = wtf[0][0]

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
            login(self, lang)
            print lang

            if lang == 0:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Payments')
                bil.click()
                scheta = self.driver.find_element_by_id('Within the Bank')
                scheta.click()
                new_schet = self.driver.find_element_by_id('New')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Pay from')
                pay_to = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeTextField')
                naznachenie = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[8]/XCUIElementTypeTextView')
                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[9]/XCUIElementTypeTextField')
                spisanie.click()
                sleep(45)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')

                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w1.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w1, "toVisible": True})
                            w1.click()
                            break
                        else:
                            pass

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                            w.click()
                            break
                        else:
                            pass
                self.driver.implicitly_wait(30)
                try:
                    pay_to.send_keys(Version.vbanke)
                except:
                    pass

                self.driver.execute_script('mobile: scroll', {"element": summa, "toVisible": True})
                naznachenie.send_keys('some text here')
                summa.send_keys(50)
                dal = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name = 'Next']")
                dal.click()
                sen = self.driver.find_element_by_id('Pay')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Confirm')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'The payment has been confirmed'))

            elif lang == 1:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Платежи')
                bil.click()
                scheta = self.driver.find_element_by_id('Внутри банка')
                scheta.click()
                new_schet = self.driver.find_element_by_id('Новый')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Выберите счет списания')
                pay_to = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeTextField')
                naznachenie = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[8]/XCUIElementTypeTextView')
                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[9]/XCUIElementTypeTextField')
                spisanie.click()
                sleep(45)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')

                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w1.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w1, "toVisible": True})
                            w1.click()
                            break
                        else:
                            pass

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                            w.click()
                            break
                        else:
                            pass
                self.driver.implicitly_wait(30)
                try:
                    pay_to.send_keys(Version.vbanke)
                except:
                    pass
                self.driver.execute_script('mobile: scroll', {"element": summa, "toVisible": True})
                naznachenie.send_keys('some text here')
                summa.send_keys(50)
                dal = self.driver.find_element_by_id('Далее')
                dal.click()
                sen = self.driver.find_element_by_id('Оплатить')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Подтвердить')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'Платеж подтвержден'))

            elif lang == 2:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Платежі')
                bil.click()
                scheta = self.driver.find_element_by_id('В межах банку')
                scheta.click()
                new_schet = self.driver.find_element_by_id('Новий')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Виберіть рахунок списання')
                pay_to = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                           '/XCUIElementTypeCell[4]/XCUIElementTypeTextField')
                naznachenie = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                                '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                                '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                                '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                                '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                                '/XCUIElementTypeCell[8]/XCUIElementTypeTextView')
                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[9]/XCUIElementTypeTextField')
                spisanie.click()
                sleep(45)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')

                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w1.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w1, "toVisible": True})
                            w1.click()
                            break
                        else:
                            pass

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                            w.click()
                            break
                        else:
                            pass
                self.driver.implicitly_wait(30)
                try:
                    pay_to.send_keys(Version.vbanke)
                except:
                    pass
                self.driver.execute_script('mobile: scroll', {"element": summa, "toVisible": True})
                naznachenie.send_keys('some text here')
                summa.send_keys(50)
                dal = self.driver.find_element_by_id('Далі')
                dal.click()
                sen = self.driver.find_element_by_id('Сплатити')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Підтвердити')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'Платіж підтверджено'))
        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_05.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # Перевод между своими счетами с карты на счет
    def test_06(self):
        db = OracleDB()
        db.connect()
        db.cursor.execute(
            "select * from IFOBSSMSDELIVERY where userid = (select id from users where login ='SORGO') order by id desc")
        wtf = [x for x in db.cursor]
        first_id = wtf[0][0]
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
            login(self, lang)
            print lang

            if lang == 0:
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Payments')
                bil.click()
                scheta = self.driver.find_element_by_id('Between own accounts')
                scheta.click()
                new_schet = self.driver.find_element_by_id('New')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Pay from')
                popolnenie = self.driver.find_element_by_id('Pay to')
                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeTextField')

                spisanie.click()
                sleep(45)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')

                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w1.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w1, "toVisible": True})
                            w1.click()
                            break
                        else:
                            pass

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                            w.click()
                            break
                        else:
                            pass

                popolnenie.click()
                sleep(15)
                account = self.driver.find_element_by_id('ACCOUNTS')
                account.click()
                sleep(10)
                spisok2 = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                spisok2.remove(spisok2[0])
                for i in spisok2:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH':
                        self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                        w.click()
                        break
                    else:
                        pass

                summa.send_keys(50)
                dal = self.driver.find_element_by_id('Next')
                dal.click()
                sen = self.driver.find_element_by_id('Pay')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Confirm')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'The payment has been confirmed'))

            elif lang == 1:
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Платежи')
                bil.click()
                scheta = self.driver.find_element_by_id('Между своими счетами')
                scheta.click()
                new_schet = self.driver.find_element_by_id('Новый')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Выберите счет списания')
                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeTextField')

                spisanie.click()
                sleep(45)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')

                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w1.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w1, "toVisible": True})
                            w1.click()
                            break
                        else:
                            pass

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                            w.click()
                            break
                        else:
                            pass

                popolnenie = self.driver.find_element_by_id('Выберите счет пополнения')
                popolnenie.click()
                sleep(15)
                account = self.driver.find_element_by_id('СЧЕТА')
                account.click()
                sleep(10)
                spisok2 = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                spisok2.remove(spisok2[0])
                for i in spisok2:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH':
                        self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                        w.click()
                        break
                    else:
                        pass
                summa.send_keys(50)
                dal = self.driver.find_element_by_id('Далее')
                dal.click()
                sen = self.driver.find_element_by_id('Оплатить')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                             '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                             '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                             '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                             '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                             '/XCUIElementTypeCell/XCUIElementTypeTable'
                                                             '/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Подтвердить')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'Платеж подтвержден'))

            elif lang == 2:
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Платежі')
                bil.click()
                scheta = self.driver.find_element_by_id('Між своїми рахунками')
                scheta.click()
                new_schet = self.driver.find_element_by_id('Новий')
                new_schet.click()
                self.driver.implicitly_wait(45)
                spisanie = self.driver.find_element_by_id('Виберіть рахунок списання')
                popolnenie = self.driver.find_element_by_id('Виберіть рахунок поповнення')
                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeTextField')

                spisanie.click()
                sleep(45)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')

                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w1.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w1, "toVisible": True})
                            w1.click()
                            break
                        else:
                            pass

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                            w.click()
                            break
                        else:
                            pass

                popolnenie.click()
                sleep(15)
                account = self.driver.find_element_by_id('РАХУНКИ')
                account.click()
                sleep(10)
                spisok2 = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                spisok2.remove(spisok2[0])
                for i in spisok2:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH':
                        self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                        w.click()
                        break
                    else:
                        pass

                summa.send_keys(50)
                dal = self.driver.find_element_by_id('Далі')
                dal.click()
                sen = self.driver.find_element_by_id('Сплатити')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Підтвердити')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                'Платіж підтверджено'))
        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_06.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # Перевод между своими счетами со счета на счет
    def test_07(self):
        db = OracleDB()
        db.connect()
        db.cursor.execute(
            "select * from IFOBSSMSDELIVERY where userid = (select id from users where login ='SORGO') order by id desc")
        wtf = [x for x in db.cursor]
        print wtf
        first_id = wtf[0][0]
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
            login(self, lang)
            print lang

            if lang == 0:
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Payments')
                bil.click()
                scheta = self.driver.find_element_by_id('Between own accounts')
                scheta.click()
                new_schet = self.driver.find_element_by_id('New')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Pay from')
                popolnenie = self.driver.find_element_by_id('Pay to')
                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeTextField')

                spisanie.click()
                sleep(45)
                account = self.driver.find_element_by_id('ACCOUNTS')
                account.click()
                sleep(10)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                        self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                        w.click()
                        break
                    else:
                        pass

                popolnenie.click()
                sleep(15)
                account = self.driver.find_element_by_id('ACCOUNTS')
                account.click()
                sleep(10)
                spisok2 = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                spisok2.remove(spisok2[0])
                for i in spisok2:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH':
                        self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                        w.click()
                        break
                    else:
                        pass

                summa.send_keys(50)
                dal = self.driver.find_element_by_id('Next')
                dal.click()
                sen = self.driver.find_element_by_id('Pay')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Confirm')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'The payment has been confirmed'))

            elif lang == 1:
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Платежи')
                bil.click()
                scheta = self.driver.find_element_by_id('Между своими счетами')
                scheta.click()
                new_schet = self.driver.find_element_by_id('Новый')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Выберите счет списания')
                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeTextField')

                spisanie.click()
                sleep(45)
                account = self.driver.find_element_by_id('СЧЕТА')
                account.click()
                sleep(10)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                        self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                        w.click()
                        break
                    else:
                        pass

                popolnenie = self.driver.find_element_by_id('Выберите счет пополнения')
                popolnenie.click()
                sleep(15)
                account = self.driver.find_element_by_id('СЧЕТА')
                account.click()
                sleep(10)
                spisok2 = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                spisok2.remove(spisok2[0])
                for i in spisok2:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH':
                        self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                        w.click()
                        break
                    else:
                        pass
                summa.send_keys(50)
                dal = self.driver.find_element_by_id('Далее')
                dal.click()
                sen = self.driver.find_element_by_id('Оплатить')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                             '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                             '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                             '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                             '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                             '/XCUIElementTypeCell/XCUIElementTypeTable'
                                                             '/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Подтвердить')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'Платеж подтвержден'))

            elif lang == 2:
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Платежі')
                bil.click()
                scheta = self.driver.find_element_by_id('Між своїми рахунками')
                scheta.click()
                new_schet = self.driver.find_element_by_id('Новий')
                new_schet.click()
                self.driver.implicitly_wait(45)
                spisanie = self.driver.find_element_by_id('Виберіть рахунок списання')
                popolnenie = self.driver.find_element_by_id('Виберіть рахунок поповнення')
                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeTextField')

                spisanie.click()
                sleep(45)
                account = self.driver.find_element_by_id('РАХУНКИ')
                account.click()
                sleep(10)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    print re.findall(r'\s\w{3}', w.get_attribute('name'))[0]
                    print re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0]
                    print re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5
                    if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                        self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                        w.click()
                        break
                    else:
                        pass

                popolnenie.click()
                sleep(15)
                account = self.driver.find_element_by_id('РАХУНКИ')
                account.click()
                sleep(10)
                spisok2 = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                spisok2.remove(spisok2[0])
                for i in spisok2:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH':
                        self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                        w.click()
                        break
                    else:
                        pass

                summa.send_keys(50)
                dal = self.driver.find_element_by_id('Далі')
                dal.click()
                sen = self.driver.find_element_by_id('Сплатити')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Підтвердити')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'Платіж підтверджено'))
        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_07.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # Перевод между своими счетами со счета на карту
    def test_08(self):
        db = OracleDB()
        db.connect()
        db.cursor.execute(
            "select * from IFOBSSMSDELIVERY where userid = (select id from users where login ='SORGO') order by id desc")
        wtf = [x for x in db.cursor]
        print wtf
        first_id = wtf[0][0]
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
            login(self, lang)
            print lang

            if lang == 0:
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Payments')
                bil.click()
                scheta = self.driver.find_element_by_id('Between own accounts')
                scheta.click()
                new_schet = self.driver.find_element_by_id('New')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Pay from')
                popolnenie = self.driver.find_element_by_id('Pay to')
                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeTextField')

                spisanie.click()
                sleep(45)
                account = self.driver.find_element_by_id('ACCOUNTS')
                account.click()
                sleep(10)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(
                            re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                        self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                        w.click()
                        break
                    else:
                        pass

                popolnenie.click()
                sleep(15)
                spisok2 = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                spisok2.remove(spisok2[0])
                for i in spisok2:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')

                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH':
                            self.driver.execute_script('mobile: scroll', {"element": w1, "toVisible": True})
                            w1.click()
                            break
                        else:
                            pass

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH':
                            self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                            w.click()
                            break
                        else:
                            pass

                summa.send_keys(50)
                dal = self.driver.find_element_by_id('Next')
                dal.click()
                sen = self.driver.find_element_by_id('Pay')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Confirm')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'The payment has been confirmed'))

            elif lang == 1:
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Платежи')
                bil.click()
                scheta = self.driver.find_element_by_id('Между своими счетами')
                scheta.click()
                new_schet = self.driver.find_element_by_id('Новый')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Выберите счет списания')
                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeTextField')

                spisanie.click()
                sleep(45)
                account = self.driver.find_element_by_id('СЧЕТА')
                account.click()
                sleep(10)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(
                            re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                        self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                        w.click()
                        break
                    else:
                        pass

                popolnenie = self.driver.find_element_by_id('Выберите счет пополнения')
                popolnenie.click()
                sleep(15)
                spisok2 = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                spisok2.remove(spisok2[0])
                for i in spisok2:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')

                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH':
                            self.driver.execute_script('mobile: scroll', {"element": w1, "toVisible": True})
                            w1.click()
                            break
                        else:
                            pass

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH':
                            self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                            w.click()
                            break
                        else:
                            pass
                summa.send_keys(50)
                dal = self.driver.find_element_by_id('Далее')
                dal.click()
                sen = self.driver.find_element_by_id('Оплатить')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                             '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                             '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                             '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                             '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                             '/XCUIElementTypeCell/XCUIElementTypeTable'
                                                             '/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Подтвердить')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'Платеж подтвержден'))

            elif lang == 2:
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Платежі')
                bil.click()
                scheta = self.driver.find_element_by_id('Між своїми рахунками')
                scheta.click()
                new_schet = self.driver.find_element_by_id('Новий')
                new_schet.click()
                self.driver.implicitly_wait(45)
                spisanie = self.driver.find_element_by_id('Виберіть рахунок списання')
                popolnenie = self.driver.find_element_by_id('Виберіть рахунок поповнення')
                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeTextField')

                spisanie.click()
                sleep(45)
                account = self.driver.find_element_by_id('РАХУНКИ')
                account.click()
                sleep(10)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(
                            re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                        self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                        w.click()
                        break
                    else:
                        pass

                popolnenie.click()
                sleep(15)
                spisok2 = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                spisok2.remove(spisok2[0])
                for i in spisok2:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')

                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH':
                            self.driver.execute_script('mobile: scroll', {"element": w1, "toVisible": True})
                            w1.click()
                            break
                        else:
                            pass

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH':
                            self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                            w.click()
                            break
                        else:
                            pass

                summa.send_keys(50)
                dal = self.driver.find_element_by_id('Далі')
                dal.click()
                sen = self.driver.find_element_by_id('Сплатити')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Підтвердити')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'Платіж підтверджено'))
        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_08.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # Перевод в пределах банка со счета
    def test_09(self):
        db = OracleDB()
        db.connect()
        db.cursor.execute(
            "select * from IFOBSSMSDELIVERY where userid = (select id from users where login ='SORGO') order by id desc")
        wtf = [x for x in db.cursor]
        print
        first_id = wtf[0][0]

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
            login(self, lang)
            print lang

            if lang == 0:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Payments')
                bil.click()
                scheta = self.driver.find_element_by_id('Within the Bank')
                scheta.click()
                new_schet = self.driver.find_element_by_id('New')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Pay from')
                pay_to = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeTextField')
                naznachenie = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[8]/XCUIElementTypeTextView')
                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[9]/XCUIElementTypeTextField')
                spisanie.click()
                sleep(45)
                account = self.driver.find_element_by_id('ACCOUNTS')
                account.click()
                sleep(10)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                        self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                        w.click()
                        break
                    else:
                        pass

                self.driver.implicitly_wait(30)
                try:
                    pay_to.send_keys(Version.vbanke)
                except:
                    pass

                self.driver.execute_script('mobile: scroll', {"element": summa, "toVisible": True})
                naznachenie.send_keys('some text here')
                summa.send_keys(50)
                dal = self.driver.find_element_by_id('Next')
                dal.click()
                sen = self.driver.find_element_by_id('Pay')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Confirm')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'The payment has been confirmed'))

            elif lang == 1:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Платежи')
                bil.click()
                scheta = self.driver.find_element_by_id('Внутри банка')
                scheta.click()
                new_schet = self.driver.find_element_by_id('Новый')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Выберите счет списания')
                pay_to = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeTextField')
                naznachenie = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[8]/XCUIElementTypeTextView')
                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[9]/XCUIElementTypeTextField')
                spisanie.click()
                sleep(45)
                account = self.driver.find_element_by_id('СЧЕТА')
                account.click()
                sleep(10)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                        self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                        w.click()
                        break
                    else:
                        pass
                self.driver.implicitly_wait(30)
                try:
                    pay_to.send_keys(Version.vbanke)
                except:
                    pass
                self.driver.execute_script('mobile: scroll', {"element": summa, "toVisible": True})
                naznachenie.send_keys('some text here')
                summa.send_keys(50)
                dal = self.driver.find_element_by_id('Далее')
                dal.click()
                sen = self.driver.find_element_by_id('Оплатить')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[2]/XCUIElementTypeTextField') 
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Подтвердить')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'Платеж подтвержден'))

            elif lang == 2:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Платежі')
                bil.click()
                scheta = self.driver.find_element_by_id('В межах банку')
                scheta.click()
                new_schet = self.driver.find_element_by_id('Новий')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Виберіть рахунок списання')
                pay_to = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeTextField')
                naznachenie = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[8]/XCUIElementTypeTextView')
                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[9]/XCUIElementTypeTextField')
                spisanie.click()
                sleep(45)
                account = self.driver.find_element_by_id('РАХУНКИ')
                account.click()
                sleep(10)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    # if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                    if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                        self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                        w.click()
                        break
                    else:
                        pass

                self.driver.implicitly_wait(30)
                try:
                    pay_to.send_keys(Version.vbanke)
                except:
                    pass
                self.driver.execute_script('mobile: scroll', {"element": summa, "toVisible": True})
                naznachenie.send_keys('some text here')
                summa.send_keys(50)
                dal = self.driver.find_element_by_id('Далі')
                dal.click()
                sen = self.driver.find_element_by_id('Сплатити')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Підтвердити')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'Платіж підтверджено'))
        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_09.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # Перевод по Украине с карты
    def test_10(self):
        db = OracleDB()
        db.connect()
        db.cursor.execute(
            "select * from IFOBSSMSDELIVERY where userid = (select id from users where login ='SORGO') order by id desc")
        wtf = [x for x in db.cursor]
        print
        first_id = wtf[0][0]

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
            login(self, lang)
            print lang

            if lang == 0:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Payments')
                bil.click()
                scheta = self.driver.find_element_by_id('Within Ukraine')
                scheta.click()
                new_schet = self.driver.find_element_by_id('New')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Pay from')
                pay_to = self.driver.find_element_by_id('Not selected')
                schet_poluch = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[5]/XCUIElementTypeTextField')
                name_poluch = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[6]/XCUIElementTypeTextField')
                inn_poluch = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[7]/XCUIElementTypeTextField')

                naznachenie = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[9]/XCUIElementTypeTextView')
                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[10]/XCUIElementTypeTextField')
                spisanie.click()
                sleep(45)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')

                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(
                                re.findall(r'\d+\.\d{2}', w1.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w1, "toVisible": True})
                            w1.click()
                            break
                        else:
                            pass

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(
                                re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                            w.click()
                            break
                        else:
                            pass

                self.driver.implicitly_wait(30)
                pay_to.click()
                sleep(5)
                search = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeSearchField ')
                search.send_keys(Version.mfo)
                sleep(2)
                bank = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell')
                bank.click()
                acept = self.driver.find_element_by_id('buttonDane')
                acept.click()
                self.driver.execute_script('mobile: scroll', {"element": summa, "toVisible": True})
                schet_poluch.send_keys(Version.accno)
                name_poluch.send_keys(Version.name)
                self.driver.find_element_by_id('Ok').click()
                inn_poluch.send_keys(Version.inn)
                self.driver.execute_script('mobile: scroll', {"element": summa, "toVisible": True})
                summa.send_keys(50)
                naznachenie.send_keys('some text here')
                dal = self.driver.find_element_by_id('Next')
                dal.click()
                sen = self.driver.find_element_by_id('Pay')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Confirm')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'The payment has been confirmed'))

            elif lang == 1:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Платежи')
                bil.click()
                scheta = self.driver.find_element_by_id('По Украине')
                scheta.click()
                new_schet = self.driver.find_element_by_id('Новый')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Выберите счет списания')
                pay_to = self.driver.find_element_by_id('Не выбран')
                schet_poluch = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[5]/XCUIElementTypeTextField')
                name_poluch = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[6]/XCUIElementTypeTextField')
                inn_poluch = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[7]/XCUIElementTypeTextField')

                naznachenie = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[9]/XCUIElementTypeTextView')
                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[10]/XCUIElementTypeTextField')
                spisanie.click()
                sleep(45)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')

                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(
                                re.findall(r'\d+\.\d{2}', w1.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w1, "toVisible": True})
                            w1.click()
                            break
                        else:
                            pass

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(
                                re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                            w.click()
                            break
                        else:
                            pass

                self.driver.implicitly_wait(30)
                pay_to.click()
                sleep(5)
                search = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeSearchField ')
                search.send_keys(Version.mfo)
                sleep(2)
                bank = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell')
                bank.click()
                acept = self.driver.find_element_by_id('buttonDane')
                acept.click()
                self.driver.execute_script('mobile: scroll', {"element": summa, "toVisible": True})
                schet_poluch.send_keys(Version.accno)
                name_poluch.send_keys(Version.name)
                self.driver.find_element_by_id('Ok').click()
                inn_poluch.send_keys(Version.inn)
                self.driver.execute_script('mobile: scroll', {"element": summa, "toVisible": True})
                summa.send_keys(50)
                naznachenie.send_keys('some text here')
                dal = self.driver.find_element_by_id('Далее')
                dal.click()
                sen = self.driver.find_element_by_id('Оплатить')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Подтвердить')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'Платеж подтвержден'))

            elif lang == 2:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Платежі')
                bil.click()
                scheta = self.driver.find_element_by_id('По Україні')
                scheta.click()
                new_schet = self.driver.find_element_by_id('Новий')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Виберіть рахунок списання')
                pay_to = self.driver.find_element_by_id('Не вибрано')
                schet_poluch = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[5]/XCUIElementTypeTextField')
                name_poluch = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[6]/XCUIElementTypeTextField')
                inn_poluch = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[7]/XCUIElementTypeTextField')

                naznachenie = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[9]/XCUIElementTypeTextView')
                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[10]/XCUIElementTypeTextField')
                spisanie.click()
                sleep(45)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')

                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(
                                re.findall(r'\d+\.\d{2}', w1.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w1, "toVisible": True})
                            w1.click()
                            break
                        else:
                            pass

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(
                                re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                            w.click()
                            break
                        else:
                            pass

                self.driver.implicitly_wait(30)
                pay_to.click()
                sleep(5)
                search = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeSearchField ')
                search.send_keys(Version.mfo)
                sleep(2)
                bank = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell')
                bank.click()
                acept = self.driver.find_element_by_id('buttonDane')
                acept.click()
                self.driver.execute_script('mobile: scroll', {"element": summa, "toVisible": True})
                schet_poluch.send_keys(Version.accno)
                name_poluch.send_keys(Version.name)
                self.driver.find_element_by_id('Ok').click()
                inn_poluch.send_keys(Version.inn)
                self.driver.execute_script('mobile: scroll', {"element": summa, "toVisible": True})
                summa.send_keys(50)
                naznachenie.send_keys('some text here')
                dal = self.driver.find_element_by_id('Далі')
                dal.click()
                sen = self.driver.find_element_by_id('Сплатити')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Підтвердити')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'Платіж підтверджено'))
        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_10.png'
            self.driver.save_screenshot(directory + file_name)
            raise


    # Перевод по Украине со счета
    def test_11(self):
        db = OracleDB()
        db.connect()
        db.cursor.execute(
            "select * from IFOBSSMSDELIVERY where userid = (select id from users where login ='SORGO') order by id desc")
        wtf = [x for x in db.cursor]
        print
        try:
            first_id = wtf[0][0]
        except:
            first_id = 0

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
            login(self, lang)
            print lang

            if lang == 0:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Payments')
                bil.click()
                scheta = self.driver.find_element_by_id('Within Ukraine')
                scheta.click()
                new_schet = self.driver.find_element_by_id('New')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Pay from')
                pay_to = self.driver.find_element_by_id('Not selected')
                schet_poluch = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                                 '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                                 '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                                 '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                                 '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                                 '/XCUIElementTypeCell[5]/XCUIElementTypeTextField')
                name_poluch = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                                '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                                '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                                '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                                '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                                '/XCUIElementTypeCell[6]/XCUIElementTypeTextField')
                inn_poluch = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                               '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                               '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                               '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                               '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                               '/XCUIElementTypeCell[7]/XCUIElementTypeTextField')

                naznachenie = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[9]/XCUIElementTypeTextView')
                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[10]/XCUIElementTypeTextField')
                spisanie.click()
                sleep(45)
                account = self.driver.find_element_by_id('ACCOUNTS')
                account.click()
                sleep(5)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(
                            re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                        self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                        w.click()
                        break
                    else:
                        pass

                self.driver.implicitly_wait(30)
                pay_to.click()
                sleep(5)
                search = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeSearchField ')
                search.send_keys(Version.mfo)
                sleep(2)
                bank = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell')
                bank.click()
                acept = self.driver.find_element_by_id('buttonDane')
                acept.click()
                self.driver.execute_script('mobile: scroll', {"element": summa, "toVisible": True})
                schet_poluch.send_keys(Version.accno)
                name_poluch.send_keys(Version.name)
                self.driver.find_element_by_id('Ok').click()
                inn_poluch.send_keys(Version.inn)
                self.driver.execute_script('mobile: scroll', {"element": summa, "toVisible": True})
                summa.send_keys(50)
                naznachenie.send_keys('some text here')
                dal = self.driver.find_element_by_id('Next')
                dal.click()
                sen = self.driver.find_element_by_id('Pay')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Confirm')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'The payment has been confirmed'))

            elif lang == 1:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Платежи')
                bil.click()
                scheta = self.driver.find_element_by_id('По Украине')
                scheta.click()
                new_schet = self.driver.find_element_by_id('Новый')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Выберите счет списания')
                pay_to = self.driver.find_element_by_id('Не выбран')
                schet_poluch = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                                 '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                                 '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                                 '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                                 '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                                 '/XCUIElementTypeCell[5]/XCUIElementTypeTextField')
                name_poluch = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                                '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                                '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                                '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                                '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                                '/XCUIElementTypeCell[6]/XCUIElementTypeTextField')
                inn_poluch = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                               '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                               '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                               '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                               '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                               '/XCUIElementTypeCell[7]/XCUIElementTypeTextField')

                naznachenie = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[9]/XCUIElementTypeTextView')
                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[10]/XCUIElementTypeTextField')
                spisanie.click()
                sleep(45)
                account = self.driver.find_element_by_id('СЧЕТА')
                account.click()
                sleep(5)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(
                            re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                        self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                        w.click()
                        break
                    else:
                        pass

                self.driver.implicitly_wait(30)
                pay_to.click()
                sleep(5)
                search = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeSearchField ')
                search.send_keys(Version.mfo)
                sleep(2)
                bank = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell')
                bank.click()
                acept = self.driver.find_element_by_id('buttonDane')
                acept.click()
                self.driver.execute_script('mobile: scroll', {"element": summa, "toVisible": True})
                schet_poluch.send_keys(Version.accno)
                name_poluch.send_keys(Version.name)
                self.driver.find_element_by_id('Ok').click()
                inn_poluch.send_keys(Version.inn)
                self.driver.execute_script('mobile: scroll', {"element": summa, "toVisible": True})
                summa.send_keys(50)
                naznachenie.send_keys('some text here')
                dal = self.driver.find_element_by_id('Далее')
                dal.click()
                sen = self.driver.find_element_by_id('Оплатить')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Подтвердить')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'Платеж подтвержден'))

            elif lang == 2:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Платежі')
                bil.click()
                scheta = self.driver.find_element_by_id('По Україні')
                scheta.click()
                new_schet = self.driver.find_element_by_id('Новий')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Виберіть рахунок списання')
                pay_to = self.driver.find_element_by_id('Не вибрано')
                schet_poluch = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                                 '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                                 '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                                 '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                                 '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                                 '/XCUIElementTypeCell[5]/XCUIElementTypeTextField')
                name_poluch = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                                '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                                '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                                '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                                '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                                '/XCUIElementTypeCell[6]/XCUIElementTypeTextField')
                inn_poluch = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                               '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                               '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                               '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                               '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                               '/XCUIElementTypeCell[7]/XCUIElementTypeTextField')

                naznachenie = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[9]/XCUIElementTypeTextView')
                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[10]/XCUIElementTypeTextField')
                spisanie.click()
                sleep(45)
                account = self.driver.find_element_by_id('РАХУНКИ')
                account.click()
                sleep(5)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(
                            re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                        self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                        w.click()
                        break
                    else:
                        pass

                self.driver.implicitly_wait(30)
                pay_to.click()
                sleep(5)
                search = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                           '/XCUIElementTypeSearchField ')
                search.send_keys(Version.mfo)
                sleep(2)
                bank = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell')
                bank.click()
                acept = self.driver.find_element_by_id('buttonDane')
                acept.click()
                self.driver.execute_script('mobile: scroll', {"element": summa, "toVisible": True})
                schet_poluch.send_keys(Version.accno)
                name_poluch.send_keys(Version.name)
                self.driver.find_element_by_id('Ok').click()
                inn_poluch.send_keys(Version.inn)
                self.driver.execute_script('mobile: scroll', {"element": summa, "toVisible": True})
                summa.send_keys(50)
                naznachenie.send_keys('some text here')
                dal = self.driver.find_element_by_id('Далі')
                dal.click()
                sen = self.driver.find_element_by_id('Сплатити')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                try:
                    sms_code.send_keys(find_sms(first_id))
                except:
                    raise NameError("sms doesn't send")
                conf = self.driver.find_element_by_id('Підтвердити')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'Платіж підтверджено'))
        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_11.png'
            self.driver.save_screenshot(directory + file_name)
            raise

    # Перевод на карту Банка с карты
    def test_12(self):
        db = OracleDB()
        db.connect()
        db.cursor.execute(
            "select * from IFOBSSMSDELIVERY where userid = (select id from users where login ='SORGO') order by id desc")
        wtf = [x for x in db.cursor]
        print
        try:
            first_id = wtf[0][0]
        except:
            first_id = 0

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
            login(self, lang)
            print lang

            if lang == 0:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Payments')
                bil.click()
                scheta = self.driver.find_element_by_id('To card within the bank')
                scheta.click()
                new_schet = self.driver.find_element_by_id('New')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Pay from')

                car1 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell[4]/XCUIElementTypeTextField')
                car2 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell[4]/XCUIElementTypeTextField[2]')
                car3 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell[4]/XCUIElementTypeTextField[3]')
                car4 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell[4]/XCUIElementTypeTextField[4]')

                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[6]/XCUIElementTypeTextField')
                spisanie.click()
                sleep(45)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')

                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(
                                re.findall(r'\d+\.\d{2}', w1.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w1, "toVisible": True})
                            w1.click()
                            break
                        else:
                            pass

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(
                                re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                            w.click()
                            break
                        else:
                            pass

                self.driver.implicitly_wait(30)
                car1.send_keys(Version.cardno[0:4])
                car2.send_keys(Version.cardno[4:8])
                car3.send_keys(Version.cardno[8:12])
                car4.send_keys(Version.cardno[12:16])
                self.driver.execute_script('mobile: scroll', {"element": summa, "toVisible": True})
                summa.send_keys(50)

                dal = self.driver.find_element_by_id('Next')
                dal.click()
                sen = self.driver.find_element_by_id('Pay')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Confirm')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'The payment has been confirmed'))

            elif lang == 1:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Платежи')
                bil.click()
                scheta = self.driver.find_element_by_id('На карту Банка')
                scheta.click()
                new_schet = self.driver.find_element_by_id('Новый')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Выберите счет списания')
                car1 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell[4]/XCUIElementTypeTextField')
                car2 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell[4]/XCUIElementTypeTextField[2]')
                car3 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell[4]/XCUIElementTypeTextField[3]')
                car4 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell[4]/XCUIElementTypeTextField[4]')

                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[6]/XCUIElementTypeTextField')
                spisanie.click()
                sleep(45)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')

                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(
                                re.findall(r'\d+\.\d{2}', w1.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w1, "toVisible": True})
                            w1.click()
                            break
                        else:
                            pass

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(
                                re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                            w.click()
                            break
                        else:
                            pass

                self.driver.implicitly_wait(30)
                car1.send_keys(Version.cardno[0:4])
                car2.send_keys(Version.cardno[4:8])
                car3.send_keys(Version.cardno[8:12])
                car4.send_keys(Version.cardno[12:16])
                self.driver.execute_script('mobile: scroll', {"element": summa, "toVisible": True})
                summa.send_keys(50)

                dal = self.driver.find_element_by_id('Далее')
                dal.click()
                sen = self.driver.find_element_by_id('Оплатить')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Подтвердить')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'Платеж подтвержден'))

            elif lang == 2:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Платежі')
                bil.click()
                scheta = self.driver.find_element_by_id('На карту Банку')
                scheta.click()
                new_schet = self.driver.find_element_by_id('Новий')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Виберіть рахунок списання')
                car1 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell[4]/XCUIElementTypeTextField')
                car2 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell[4]/XCUIElementTypeTextField[2]')
                car3 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell[4]/XCUIElementTypeTextField[3]')
                car4 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell[4]/XCUIElementTypeTextField[4]')

                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[6]/XCUIElementTypeTextField')
                spisanie.click()
                sleep(45)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[7]')
                    w1 = i.find_element_by_xpath(
                        '//XCUIElementTypeCell/XCUIElementTypeStaticText[9]')

                    if re.findall(r'\d+\.\d{2}\s\w{3}', w.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w1.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(
                                re.findall(r'\d+\.\d{2}', w1.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w1, "toVisible": True})
                            w1.click()
                            break
                        else:
                            pass

                    elif re.findall(r'\d+\.\d{2}\s\w{3}', w1.get_attribute('name')) == []:
                        if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(
                                re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                            self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                            w.click()
                            break
                        else:
                            pass

                self.driver.implicitly_wait(30)
                car1.send_keys(Version.cardno[0:4])
                car2.send_keys(Version.cardno[4:8])
                car3.send_keys(Version.cardno[8:12])
                car4.send_keys(Version.cardno[12:16])
                self.driver.execute_script('mobile: scroll', {"element": summa, "toVisible": True})
                summa.send_keys(50)

                dal = self.driver.find_element_by_id('Далі')
                dal.click()
                sen = self.driver.find_element_by_id('Сплатити')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Підтвердити')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'Платіж підтверджено'))
        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_12.png'
            self.driver.save_screenshot(directory + file_name)
            raise


    # Перевод на карту Банка со счета
    def test_13(self):
        db = OracleDB()
        db.connect()
        db.cursor.execute(
            "select * from IFOBSSMSDELIVERY where userid = (select id from users where login ='SORGO') order by id desc")
        wtf = [x for x in db.cursor]
        print
        try:
            first_id = wtf[0][0]
        except:
            first_id = 0

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
            login(self, lang)
            print lang

            if lang == 0:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Payments')
                bil.click()
                scheta = self.driver.find_element_by_id('To card within the bank')
                scheta.click()
                new_schet = self.driver.find_element_by_id('New')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Pay from')

                car1 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell[4]/XCUIElementTypeTextField')
                car2 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell[4]/XCUIElementTypeTextField[2]')
                car3 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell[4]/XCUIElementTypeTextField[3]')
                car4 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell[4]/XCUIElementTypeTextField[4]')

                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[6]/XCUIElementTypeTextField')
                spisanie.click()
                sleep(45)
                account = self.driver.find_element_by_id('ACCOUNTS')
                account.click()
                sleep(5)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(
                            re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                        self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                        w.click()
                        break
                    else:
                        pass

                self.driver.implicitly_wait(30)
                car1.send_keys(Version.cardno[0:4])
                car2.send_keys(Version.cardno[4:8])
                car3.send_keys(Version.cardno[8:12])
                car4.send_keys(Version.cardno[12:16])
                self.driver.execute_script('mobile: scroll', {"element": summa, "toVisible": True})
                summa.send_keys(50)

                dal = self.driver.find_element_by_id('Next')
                dal.click()
                sen = self.driver.find_element_by_id('Pay')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Confirm')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'The payment has been confirmed'))

            elif lang == 1:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Платежи')
                bil.click()
                scheta = self.driver.find_element_by_id('На карту Банка')
                scheta.click()
                new_schet = self.driver.find_element_by_id('Новый')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Выберите счет списания')
                car1 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell[4]/XCUIElementTypeTextField')
                car2 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell[4]/XCUIElementTypeTextField[2]')
                car3 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell[4]/XCUIElementTypeTextField[3]')
                car4 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell[4]/XCUIElementTypeTextField[4]')

                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[6]/XCUIElementTypeTextField')
                spisanie.click()
                sleep(45)
                account = self.driver.find_element_by_id('СЧЕТА')
                account.click()
                sleep(5)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(
                            re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                        self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                        w.click()
                        break
                    else:
                        pass

                self.driver.implicitly_wait(30)
                car1.send_keys(Version.cardno[0:4])
                car2.send_keys(Version.cardno[4:8])
                car3.send_keys(Version.cardno[8:12])
                car4.send_keys(Version.cardno[12:16])
                self.driver.execute_script('mobile: scroll', {"element": summa, "toVisible": True})
                summa.send_keys(50)

                dal = self.driver.find_element_by_id('Далее')
                dal.click()
                sen = self.driver.find_element_by_id('Оплатить')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable'
                    '/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Подтвердить')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'Платеж подтвержден'))

            elif lang == 2:
                self.driver.implicitly_wait(30)
                menu = self.driver.find_element_by_id('homePage')
                menu.click()
                bil = self.driver.find_element_by_id('Платежі')
                bil.click()
                scheta = self.driver.find_element_by_id('На карту Банку')
                scheta.click()
                new_schet = self.driver.find_element_by_id('Новий')
                new_schet.click()
                spisanie = self.driver.find_element_by_id('Виберіть рахунок списання')
                car1 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell[4]/XCUIElementTypeTextField')
                car2 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell[4]/XCUIElementTypeTextField[2]')
                car3 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell[4]/XCUIElementTypeTextField[3]')
                car4 = self.driver.find_element_by_xpath('/XCUIElementTypeApplication/XCUIElementTypeWindow'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                         '/XCUIElementTypeOther/XCUIElementTypeTable'
                                                         '/XCUIElementTypeCell[4]/XCUIElementTypeTextField[4]')

                summa = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                    '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[6]/XCUIElementTypeTextField')
                spisanie.click()
                sleep(45)
                account = self.driver.find_element_by_id('РАХУНКИ')
                account.click()
                sleep(5)
                sp = self.driver.find_elements_by_xpath('//XCUIElementTypeCell')
                pg = self.driver.page_source
                lang = re.findall(r'\d+\.\d{2}\s\w{3}', pg)
                for i in lang:
                    valuta = re.findall(r'\s\w{3}', i)[0].lstrip(' ')
                    if valuta not in ['UAH', 'USD', 'EUR']:
                        raise NameError('Wrong valuta')
                    else:
                        pass

                sp.remove(sp[0])
                print sp
                for i in sp:
                    w = i.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeStaticText[4]')
                    if re.findall(r'\s\w{3}', w.get_attribute('name'))[0].lstrip(' ') == 'UAH' and len(
                            re.findall(r'\d+\.\d{2}', w.get_attribute('name'))[0].lstrip(' ')) > 5:
                        self.driver.execute_script('mobile: scroll', {"element": w, "toVisible": True})
                        w.click()
                        break
                    else:
                        pass

                self.driver.implicitly_wait(30)
                car1.send_keys(Version.cardno[0:4])
                car2.send_keys(Version.cardno[4:8])
                car3.send_keys(Version.cardno[8:12])
                car4.send_keys(Version.cardno[12:16])
                self.driver.execute_script('mobile: scroll', {"element": summa, "toVisible": True})
                summa.send_keys(50)

                dal = self.driver.find_element_by_id('Далі')
                dal.click()
                sen = self.driver.find_element_by_id('Сплатити')
                sen.click()
                self.driver.implicitly_wait(60)
                sleep(10)

                sms_code = self.driver.find_element_by_xpath(
                    '/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
                sms_code.send_keys(find_sms(first_id))
                conf = self.driver.find_element_by_id('Підтвердити')
                conf.click()
                self.assertTrue(self.driver.find_element_by_id(
                    'Платіж підтверджено'))
        except:
            directory = '%s/screenshots/' % os.getcwd()
            file_name = 'test_13.png'
            self.driver.save_screenshot(directory + file_name)
            raise


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Version)
    unittest.TextTestRunner(verbosity=2).run(suite)
