from time import sleep

from Android.OTP.size import autologin, tap, spisanie
from Android.OTP.sql.sms import first_id, find_sms


def own(self, login, password, valuta, type):
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
    spisanie(self, valuta, type)
    amount = self.driver.find_elements_by_xpath('//*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountPanelInput"]')
    amount[0].send_keys(1)
    f_id = first_id(login)
    tap(self, self.driver.find_element_by_xpath('//*[@class="OtpCommonMobileBundle-OtpCommonStyle-headerButtonNext"]'))
    okbtn = self.driver.find_element_by_xpath('//*[@class="OtpCommonMobileBundle-OtpCommonStyle-headerButtonOk"]')
    tap(self, okbtn)
    self.driver.switch_to.context('NATIVE_APP')
    sms = self.driver.find_element_by_id('ua.com.cs.ifobs.mobile.android.otp:id/inputDialogText')
    sleep(10)
    sms_code = find_sms(f_id,login)
    sms.send_keys(sms_code)
    self.driver.find_element_by_id('ua.com.cs.ifobs.mobile.android.otp:id/dialogOk').click()
    self.assertTrue(self.driver.find_element_by_id('ua.com.cs.ifobs.mobile.android.otp:id/dialogText'))


def ukraine(self, login, password, valuta, type):
    self.driver.implicitly_wait(30)
    sleep(10)
    # f_id = first_id()
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
        if i.get_attribute('textContent') == 'Within Ukraine in UAH':
            tap(self, i)
    self.driver.switch_to.context('NATIVE_APP')
    own = self.driver.find_element_by_android_uiautomator(
        'resourceId("android:id/text1").text("New")')
    own.click()
    spisanie(self, valuta, type)
    amount = self.driver.find_elements_by_xpath('//*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountPanelInput"]')
    if type == 'a2u':
        amount[0].send_keys(2)
    else:
        amount[0].send_keys(1)
    purpos = self.driver.find_element_by_xpath('//*[@class="gwt-TextArea InputAppearance-InputCss-mgwt-InputBox-box"]')
    purpos.send_keys('Within Ukraine')
    f_id = first_id(login)
    nxtbtn = self.driver.find_element_by_xpath(
        '//*[@class="OtpCommonMobileBundle-OtpCommonStyle-headerButtonNext"]')
    tap(self, nxtbtn)
    okbtn = self.driver.find_element_by_xpath('//*[@class="OtpCommonMobileBundle-OtpCommonStyle-headerButtonOk"]')
    tap(self, okbtn)
    self.driver.switch_to.context('NATIVE_APP')
    sms = self.driver.find_element_by_id('ua.com.cs.ifobs.mobile.android.otp:id/inputDialogText')
    sleep(10)
    sms_code = find_sms(f_id,login)
    sms.send_keys(sms_code)
    self.driver.find_element_by_id('ua.com.cs.ifobs.mobile.android.otp:id/dialogOk').click()
    self.assertEqual(self.driver.find_element_by_id('ua.com.cs.ifobs.mobile.android.otp:id/dialogText').get_attribute('text'), 'The payment has been confirmed')
