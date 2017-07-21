import random
import string
from time import sleep

from Android.OTP.size import autologin, tap


def new_mess(self, login, password):
    th = "".join([random.choice(string.letters) for i in xrange(5)])
    self.driver.implicitly_wait(30)
    sleep(10)
    autologin(self, login, password)
    menu = self.driver.find_element_by_xpath('//*[@class="OtpCommonMobileBundle-OtpCommonStyle-headerButtonMenu"]')
    tap(self, menu)
    self.driver.switch_to.context('NATIVE_APP')
    transfer = self.driver.find_element_by_android_uiautomator(
        'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/menuItemName").textMatches("Messages|MESSAGES")')
    transfer.click()
    new = self.driver.find_element_by_android_uiautomator(
        'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/menuItemName").textMatches("New message|NEW MESSAGE")')
    new.click()
    self.driver.switch_to.context('WEBVIEW')
    send = self.driver.find_element_by_xpath('//*[@class="OtpMessageMobileBundle-OtpMessageStyle-sendMessage"]')
    theme = self.driver.find_element_by_xpath('//*[@class="gwt-TextBox InputAppearance-InputCss-mgwt-InputBox-box"]')
    text = self.driver.find_element_by_xpath('//*[@class="gwt-TextArea InputAppearance-InputCss-mgwt-InputBox-box"]')
    tap(self, send)
    sleep(1)
    self.driver.switch_to.context('NATIVE_APP')
    err = self.driver.find_element_by_id('ua.com.cs.ifobs.mobile.android.otp:id/dialogText').get_attribute('text')
    self.assertTrue(err == 'The message subject/body is missing')
    self.driver.find_element_by_id('ua.com.cs.ifobs.mobile.android.otp:id/dialogOk').click()
    self.driver.switch_to.context('WEBVIEW')
    theme.send_keys(th)
    tap(self, send)
    sleep(1)
    self.driver.switch_to.context('NATIVE_APP')
    err = self.driver.find_element_by_id('ua.com.cs.ifobs.mobile.android.otp:id/dialogText').get_attribute('text')
    self.assertTrue(err == 'The message subject/body is missing')
    self.driver.find_element_by_id('ua.com.cs.ifobs.mobile.android.otp:id/dialogOk').click()
    self.driver.switch_to.context('WEBVIEW')
    text.send_keys(th)
    tap(self, send)
    self.driver.switch_to.context('NATIVE_APP')
    err = self.driver.find_element_by_id('ua.com.cs.ifobs.mobile.android.otp:id/dialogText').get_attribute('text')
    self.assertTrue(err == 'The message has been sent')


def mess_limit(self, login, password):
    th = "".join([random.choice(string.letters) for i in xrange(90)])
    tx = "".join([random.choice(string.letters) for i in xrange(2010)])

    self.driver.implicitly_wait(30)
    sleep(10)
    autologin(self, login, password)
    menu = self.driver.find_element_by_xpath('//*[@class="OtpCommonMobileBundle-OtpCommonStyle-headerButtonMenu"]')
    tap(self, menu)
    self.driver.switch_to.context('NATIVE_APP')
    transfer = self.driver.find_element_by_android_uiautomator(
        'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/menuItemName").textMatches("Messages|MESSAGES")')
    transfer.click()
    new = self.driver.find_element_by_android_uiautomator(
        'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/menuItemName").textMatches("New message|NEW MESSAGE")')
    new.click()
    self.driver.switch_to.context('WEBVIEW')
    send = self.driver.find_element_by_xpath('//*[@class="OtpMessageMobileBundle-OtpMessageStyle-sendMessage"]')
    theme = self.driver.find_element_by_xpath('//*[@class="gwt-TextBox InputAppearance-InputCss-mgwt-InputBox-box"]')
    text = self.driver.find_element_by_xpath('//*[@class="gwt-TextArea InputAppearance-InputCss-mgwt-InputBox-box"]')
    w = theme.get_attribute('maxlength')
    self.assertEqual(w, '84')
    theme.send_keys(th)
    text.send_keys(tx)
    self.assertEqual(len(self.driver.find_element_by_xpath('//*[@class="gwt-TextBox InputAppearance-InputCss-mgwt-InputBox-box"]').get_attribute('value')), 84)
    tap(self, send)
    self.driver.switch_to.context('NATIVE_APP')
    err = self.driver.find_element_by_id('ua.com.cs.ifobs.mobile.android.otp:id/dialogText').get_attribute('text')
    self.assertTrue(err == 'The message length exceeds 2000 characters.')
