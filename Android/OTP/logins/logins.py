from time import sleep

from Android.OTP.size import autologin


def invalid_psw(self, login, password):
    self.driver.implicitly_wait(30)
    sleep(10)
    password += '4'
    autologin(self, login, password)
    self.driver.switch_to.context('NATIVE_APP')
    err = self.driver.find_element_by_id(
        "ua.com.cs.ifobs.mobile.android.otp:id/dialogText").get_attribute('text')
    self.assertEqual(err, 'It is impossible to login. Check if the login and password are correct.')

