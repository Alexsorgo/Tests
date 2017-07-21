import random
import string
from time import sleep

from Android.OTP.size import autologin, tap


def change_password(self, login, password, new_pass, conf_pass, type):
    self.driver.implicitly_wait(30)
    sleep(10)
    autologin(self, login, password)
    menu = self.driver.find_element_by_xpath('//*[@class="OtpCommonMobileBundle-OtpCommonStyle-headerButtonMenu"]')
    tap(self, menu)
    self.driver.switch_to.context('NATIVE_APP')
    try:
        arrow = self.driver.find_element_by_android_uiautomator(
            'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/bottomIndicator")')
        arrow.click()
    except:
        pass
    sett = self.driver.find_element_by_android_uiautomator(
        'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/menuItemName").textMatches("Settings|SETTINGS")')
    sett.click()
    psw_ch = self.driver.find_element_by_android_uiautomator(
        'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/menuItemName").textMatches("Change password|CHANGE PASSWORD")')
    psw_ch.click()
    new_psw = self.driver.find_element_by_android_uiautomator(
        'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/new_password")')
    conf = self.driver.find_element_by_android_uiautomator(
        'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/repeat_password")')
    new_psw.send_keys(new_pass)
    conf.send_keys(conf_pass)
    self.driver.hide_keyboard()
    if type == 'positive':
        save_btn = self.driver.find_element_by_android_uiautomator(
            'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/savePasswordButton")')
        save_btn.click()
        err = self.driver.find_element_by_id('ua.com.cs.ifobs.mobile.android.otp:id/dialogText').get_attribute('text')
        self.assertTrue(err == 'The password has been changed')
    elif type == 'empty':
        save_btn = self.driver.find_element_by_android_uiautomator(
            'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/savePasswordButton")')
        save_btn.click()
        err = self.driver.find_element_by_android_uiautomator(
            'className("android.widget.TextView").text("CHANGE PASSWORD")')
        self.assertTrue(err)
    elif type == 'latin':
        print self.driver.find_element_by_android_uiautomator(
            'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/new_password")').get_attribute('text')
    elif type == 'space':
        err = self.driver.find_element_by_android_uiautomator(
            'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/new_password")').get_attribute('text')
        self.assertTrue(len(err) == 3)
    elif type == 'same':
        save_btn = self.driver.find_element_by_android_uiautomator(
            'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/savePasswordButton")')
        save_btn.click()
        err = self.driver.find_element_by_id('ua.com.cs.ifobs.mobile.android.otp:id/dialogText').get_attribute('text')
        self.assertTrue(err == "The values of the 'New password' and 'Current password' fields should differ.")


def login_change(self, login, password, new_log, conf_log, type):
    self.driver.implicitly_wait(30)
    sleep(10)
    autologin(self, login, password)
    menu = self.driver.find_element_by_xpath('//*[@class="OtpCommonMobileBundle-OtpCommonStyle-headerButtonMenu"]')
    tap(self, menu)
    self.driver.switch_to.context('NATIVE_APP')
    try:
        arrow = self.driver.find_element_by_android_uiautomator(
            'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/bottomIndicator")')
        arrow.click()
    except:
        pass
    sett = self.driver.find_element_by_android_uiautomator(
        'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/menuItemName").textMatches("Settings|SETTINGS")')
    sett.click()
    psw_ch = self.driver.find_element_by_android_uiautomator(
        'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/menuItemName").textMatches("Change login|CHANGE THE LOGIN")')
    psw_ch.click()
    new_psw = self.driver.find_element_by_android_uiautomator(
        'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/new_login")')
    conf = self.driver.find_element_by_android_uiautomator(
        'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/new_login_confirm")')
    if type == 'busy':
        new_psw.send_keys(new_log)
        conf.send_keys(conf_log)
        self.driver.hide_keyboard()
        save_btn = self.driver.find_element_by_android_uiautomator(
            'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/dialogOk")')
        save_btn.click()
        err = self.driver.find_element_by_id('ua.com.cs.ifobs.mobile.android.otp:id/dialogText').get_attribute('text')
        self.assertTrue(err == "The user with such login has already registered in the system")
    elif type == 'same':
        new_psw.send_keys(new_log)
        conf.send_keys(conf_log)
        self.driver.hide_keyboard()
        save_btn = self.driver.find_element_by_android_uiautomator(
            'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/dialogOk")')
        save_btn.click()
        err = self.driver.find_element_by_id('ua.com.cs.ifobs.mobile.android.otp:id/dialogTitle').get_attribute('text')
        self.assertTrue(err == "Change the login")
    elif type == 'validation':
        new_psw.send_keys('Some new + . login')
        self.assertTrue(self.driver.find_element_by_android_uiautomator(
            'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/new_login")').get_attribute('text')== 'Somenewlogin')
        new_psw.clear()
        new_psw.send_keys('to')
        conf.send_keys('to')
        self.driver.hide_keyboard()
        save_btn = self.driver.find_element_by_android_uiautomator(
            'resourceId("ua.com.cs.ifobs.mobile.android.otp:id/dialogOk")')
        save_btn.click()
        err = self.driver.find_element_by_id('ua.com.cs.ifobs.mobile.android.otp:id/dialogTitle').get_attribute('text')
        self.assertTrue(err == "Change the login")