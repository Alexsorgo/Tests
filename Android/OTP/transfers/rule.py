import os
from time import sleep

import re
from selenium.common.exceptions import NoSuchElementException

import xml.etree.ElementTree as ET

from Android.OTP.size import autologin, tap
from Android.OTP.sql.reqst import cards_req
from Android.OTP.sql.rules import acc_rule13


def rule_17(self, login, password):
    self.driver.implicitly_wait(30)
    sleep(10)
    autologin(self, login, password)
    menu = self.driver.find_element_by_xpath('//*[@class="OtpCommonMobileBundle-OtpCommonStyle-headerButtonMenu"]')
    tap(self, menu)
    self.driver.switch_to.context('NATIVE_APP')
    transfer = self.driver.find_element_by_android_uiautomator(
        'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/menuItemName").textMatches("Transfers|TRANSFERS")')
    transfer.click()
    new = self.driver.find_element_by_android_uiautomator(
        'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/menuItemName").textMatches("New transfers|NEW TRANSFERS")')
    new.click()
    self.driver.switch_to.context('WEBVIEW')
    spisok = self.driver.find_elements_by_xpath(
        '//*[@class="OtpPaymentMobileBundle-OtpPaymentStyle-paymentMenuItemLabel"]')
    for i in spisok:
        if i.get_attribute('textContent') == 'Between own accounts':
            tap(self, i)
    self.driver.switch_to.context('NATIVE_APP')
    own = self.driver.find_element_by_android_uiautomator(
        'resourceId("android:id/text1").text("New")')
    own.click()
    self.driver.switch_to.context('WEBVIEW')
    self.driver.hide_keyboard()
    spisok = self.driver.find_elements_by_xpath(
        '//*[@class="OtpPaymentMobileBundle-OtpPaymentStyle-itemAmountContainer"]')
    cur = []
    for i in spisok:
        cur.append(i.find_element_by_xpath(
            './/*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetCurrency"]').get_attribute(
            'textContent'))
    self.assertTrue('UAH' not in cur)


def rule_18(self, login, password):
    self.driver.implicitly_wait(30)
    sleep(10)
    autologin(self, login, password)
    menu = self.driver.find_element_by_xpath('//*[@class="OtpCommonMobileBundle-OtpCommonStyle-headerButtonMenu"]')
    tap(self, menu)
    self.driver.switch_to.context('NATIVE_APP')
    transfer = self.driver.find_element_by_android_uiautomator(
        'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/menuItemName").textMatches("Transfers|TRANSFERS")')
    transfer.click()
    new = self.driver.find_element_by_android_uiautomator(
        'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/menuItemName").textMatches("New transfers|NEW TRANSFERS")')
    new.click()
    self.driver.switch_to.context('WEBVIEW')
    spisok = self.driver.find_elements_by_xpath(
        '//*[@class="OtpPaymentMobileBundle-OtpPaymentStyle-paymentMenuItemLabel"]')
    for i in spisok:
        if i.get_attribute('textContent') == 'Between own accounts':
            tap(self, i)
    self.driver.switch_to.context('NATIVE_APP')
    own = self.driver.find_element_by_android_uiautomator(
        'resourceId("android:id/text1").text("New")')
    own.click()
    self.driver.switch_to.context('WEBVIEW')
    self.driver.hide_keyboard()
    spisok = self.driver.find_elements_by_xpath(
        '//*[@class="OtpPaymentMobileBundle-OtpPaymentStyle-itemAmountContainer"]')
    for i in spisok:
        print i.find_element_by_xpath(
            './/*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetCurrency"]').get_attribute(
            'textContent')
        self.assertTrue(i.find_element_by_xpath(
            './/*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetCurrency"]').get_attribute(
            'textContent') == "UAH")


def rule_24(self, login, password):
    self.driver.implicitly_wait(30)
    sleep(10)
    autologin(self, login, password)
    self.driver.implicitly_wait(60)
    sleep(20)
    menu = self.driver.find_element_by_xpath('//*[@class="OtpCommonMobileBundle-OtpCommonStyle-headerButtonMenu"]')
    tap(self, menu)
    self.driver.switch_to.context('NATIVE_APP')
    try:
        self.driver.find_element_by_android_uiautomator(
            'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/menuItemName").textMatches("Deposits|DEPOSITS|New deposit|NEW DEPOSIT")')
        raise NameError('Deposits present')
    except NoSuchElementException:
        return True


def rule_23(self, login, password):
    self.driver.implicitly_wait(30)
    sleep(10)
    autologin(self, login, password)
    menu = self.driver.find_element_by_xpath('//*[@class="OtpCommonMobileBundle-OtpCommonStyle-headerButtonMenu"]')
    tap(self, menu)
    self.driver.switch_to.context('NATIVE_APP')
    try:
        self.driver.find_element_by_android_uiautomator(
            'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/menuItemName").textMatches("Loans|LOANS")')
        raise NameError('Credits present')
    except NoSuchElementException:
        return True


def rule_17and18(self, login, password):
    self.driver.implicitly_wait(30)
    sleep(10)
    autologin(self, login, password)
    menu = self.driver.find_element_by_xpath('//*[@class="OtpCommonMobileBundle-OtpCommonStyle-headerButtonMenu"]')
    tap(self, menu)
    self.driver.switch_to.context('NATIVE_APP')
    try:
        self.driver.find_element_by_android_uiautomator(
            'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/menuItemName").textMatches("Transfers|TRANSFERS")')
        raise NameError('Payments present')
    except NoSuchElementException:
        return True


def rule_46(self, login, password):
    self.driver.implicitly_wait(30)
    sleep(10)
    autologin(self, login, password)
    menu = self.driver.find_element_by_xpath(
        '//*[@class="OtpDashboardMobileBundle-OtpDashboardStyle-indicatorTitleWidgetContainer"]')
    tap(self, menu)
    self.driver.switch_to.context('NATIVE_APP')
    try:
        self.driver.find_element_by_android_uiautomator(
            'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/menuItemName").textMatches("Cards|CARDS")')
        raise NameError('Cards present')
    except NoSuchElementException:
        return True


def acc_rule_13(self, login, password):
    self.driver.implicitly_wait(30)
    sleep(10)
    autologin(self, login, password)
    self.assertTrue(self.driver.find_elements_by_xpath(
        '//*[@class="OtpDashboardMobileBundle-OtpDashboardStyle-logo"]'))
    table = self.driver.find_elements_by_xpath(
        '//*[@class="OtpDashboardMobileBundle-OtpDashboardStyle-indicatorTitleWidgetContainer"]')
    for i in table:
        if i.find_element_by_xpath(
                './/*[@class="OtpDashboardMobileBundle-OtpDashboardStyle-nameTitleWidget"]').get_attribute(
            'textContent') == 'Accounts':
            count = i.find_element_by_xpath(
                './/*[@class="OtpDashboardMobileBundle-OtpDashboardStyle-countTitleWidget"]').get_attribute(
                'textContent').strip(')').lstrip('(')
            print count
    acc_rule13(login)
    refresh = self.driver.find_element_by_xpath(
        '//*[@class="OtpCommonMobileBundle-OtpCommonStyle-headerButtonRefresh"]')
    tap(self, refresh)
    sleep(7)
    table2 = self.driver.find_elements_by_xpath(
        '//*[@class="OtpDashboardMobileBundle-OtpDashboardStyle-indicatorTitleWidgetContainer"]')
    for i in table2:
        if i.find_element_by_xpath(
                './/*[@class="OtpDashboardMobileBundle-OtpDashboardStyle-nameTitleWidget"]').get_attribute(
            'textContent') == 'Accounts':
            count2 = i.find_element_by_xpath(
                './/*[@class="OtpDashboardMobileBundle-OtpDashboardStyle-countTitleWidget"]').get_attribute(
                'textContent').strip(')').lstrip('(')
    self.assertNotEqual(count, count2)


def accounts_mask(self, login, password):
    self.driver.implicitly_wait(30)
    sleep(10)
    autologin(self, login, password)
    self.assertTrue(self.driver.find_elements_by_xpath(
        '//*[@class="OtpDashboardMobileBundle-OtpDashboardStyle-logo"]'))
    menu = self.driver.find_element_by_xpath(
        '//*[@class="OtpCommonMobileBundle-OtpCommonStyle-headerButtonMenu"]')
    tap(self, menu)
    self.driver.switch_to.context('NATIVE_APP')
    transfer = self.driver.find_element_by_android_uiautomator(
        'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/menuItemName").textMatches("Transfers|TRANSFERS")')
    transfer.click()
    new = self.driver.find_element_by_android_uiautomator(
        'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/menuItemName").textMatches("New transfers|NEW TRANSFERS")')
    new.click()
    self.driver.switch_to.context('WEBVIEW')
    spisok = self.driver.find_elements_by_xpath(
        '//*[@class="OtpPaymentMobileBundle-OtpPaymentStyle-paymentMenuItemLabel"]')
    for i in spisok:
        if i.get_attribute('textContent') == 'Between own accounts':
            tap(self, i)
    self.driver.switch_to.context('NATIVE_APP')
    own = self.driver.find_element_by_android_uiautomator(
        'resourceId("android:id/text1").text("New")')
    own.click()
    self.driver.switch_to.context('WEBVIEW')
    self.driver.hide_keyboard()
    spisok = self.driver.find_elements_by_xpath(
        '//*[@class="OtpCommonMobileBundle-OtpCommonStyle-groupItemSingleFieldValue"]')
    for i in spisok:
        w = i.get_attribute('textContent')
        print w
        if re.findall(r'2625\d+', w):
            if w == re.findall(r'2625\d+', w)[0]:
                raise NameError('we got 2625 acc')


def cards_active(self, login, password):
    self.driver.implicitly_wait(30)
    sleep(10)
    cards_req()
    autologin(self, login, password)
    self.assertTrue(self.driver.find_elements_by_xpath(
        '//*[@class="OtpDashboardMobileBundle-OtpDashboardStyle-logo"]'))
    card_block = self.driver.find_element_by_xpath('//*[@id="MAIN"]/div[2]/div/div[1]/div[1]/div[2]')
    spisok = card_block.find_elements_by_xpath(
        './/*[@class="OtpDashboardMobileBundle-OtpDashboardStyle-itemAdditionalLabelInfoWidget"]')
    cards_ui = []
    for i in spisok:
        self.assertTrue(re.findall(r'\d{6}\*{6}\d{4}', i.get_attribute('textContent')))
        cards_ui.append(i.get_attribute('textContent'))

    acc = []
    unacc = []
    path_enc = '%s/sql/xmls/enc_data.xml' % os.getcwd()
    tree = ET.parse(path_enc)
    root = tree.getroot()
    for i in root.iter('AccountDetails'):
        if i.find('Type').text == 'CARD':
            if i.find('Card').find('State').text == 'ACTIVE':
                acc.append(i.find('Card').find('CardNo').text)
            else:
                unacc.append(i.find('Card').find('CardNo').text)

    for i in cards_ui:
        if i in acc:
            pass
        else:
            raise NameError('UnActive in active')
