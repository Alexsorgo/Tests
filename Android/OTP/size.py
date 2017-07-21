from time import sleep

from appium.webdriver.common.touch_action import TouchAction

from constants import ukraine_mfo, ukraine_accno, name, ukraine_inn


def center(el):
    XCentr = float(el.location['x']) + el.size['width'] / float(2)
    YCentr = float(el.location['y']) + el.size['height'] / float(2)
    return {'XCentr': XCentr, 'YCentr': YCentr}


def tap(self, el):
    cnt = center(el)
    websize = self.driver.find_element_by_xpath('/html').size
    self.driver.switch_to.context('NATIVE_APP')
    window_size = self.driver.get_window_size()
    Xprop = window_size["width"] / float(websize['width'])
    Yprop = window_size["height"] / float(websize['height'])
    action = TouchAction(self.driver)
    action.tap(x=(cnt['XCentr'] * Xprop), y=(cnt['YCentr'] * Yprop) + 60).perform()
    self.driver.switch_to.context('WEBVIEW')


def autologin(self, lgn, password):
    self.driver.switch_to.context('WEBVIEW')
    login = self.driver.find_element_by_xpath(
        '//*[@class="OtpLoginMobileBundle-OtpLoginStyle-loginTextInput OtpLoginMobileBundle-OtpLoginStyle-loginInput"]')
    login.clear()
    login.send_keys(lgn)
    psw = self.driver.find_element_by_xpath(
        '//*[@class="OtpLoginMobileBundle-OtpLoginStyle-loginTextInput OtpLoginMobileBundle-OtpLoginStyle-passwordInput"]')
    psw.send_keys(password)
    next2 = self.driver.find_elements_by_xpath(
        '//*[@class="OtpLoginMobileBundle-OtpLoginStyle-loginButton ButtonAppearance-ButtonCss-mgwt-Button-round"]')
    tap(self, next2[0])
    self.driver.implicitly_wait(30)
    sleep(7)
    # self.assertTrue(self.driver.find_elements_by_xpath(
    #     '//*[@class="OtpDashboardMobileBundle-OtpDashboardStyle-logo"]'))


def spisanie(self, valuta, type):
    if type == 'c2c':
        self.driver.switch_to.context('WEBVIEW')
        self.driver.hide_keyboard()
        spisok = self.driver.find_elements_by_xpath(
            '//*[@class="OtpPaymentMobileBundle-OtpPaymentStyle-itemAmountContainer"]')
        for i in spisok:
            if i.find_element_by_xpath(
                    './/*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetAmount OtpPaymentMobileBundle-OtpPaymentStyle-itemAmountWidgetAmount"]').get_attribute(
                'textContent') != '0.':
                if i.find_element_by_xpath(
                        './/*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetCurrency"]').get_attribute(
                    'textContent') == valuta:
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", i)
                    tap(self,
                        i.find_element_by_xpath(
                            './/*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetCurrency"]'))
                    break
        nxtbtn = self.driver.find_element_by_xpath(
            '//*[@class="OtpCommonMobileBundle-OtpCommonStyle-headerButtonNext"]')
        tap(self, nxtbtn)
        self.driver.hide_keyboard()
        popolnenie = self.driver.find_elements_by_xpath(
            '//*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetAmount OtpPaymentMobileBundle-OtpPaymentStyle-itemAmountWidgetAmount"]')
        tap(self, popolnenie[0])
        tap(self, nxtbtn)
    elif type == 'c2a':
        self.driver.switch_to.context('WEBVIEW')
        self.driver.hide_keyboard()
        spisok = self.driver.find_elements_by_xpath(
            '//*[@class="OtpPaymentMobileBundle-OtpPaymentStyle-itemAmountContainer"]')
        for i in spisok:
            if i.find_element_by_xpath(
                    './/*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetAmount OtpPaymentMobileBundle-OtpPaymentStyle-itemAmountWidgetAmount"]').get_attribute(
                'textContent') != '0.' and i.find_element_by_xpath(
                './/*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetCurrency"]').get_attribute(
                'textContent') == valuta:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", i)
                tap(self,
                    i.find_element_by_xpath(
                        './/*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetCurrency"]'))
                break
        nxtbtn = self.driver.find_element_by_xpath(
            '//*[@class="OtpCommonMobileBundle-OtpCommonStyle-headerButtonNext"]')
        tap(self, nxtbtn)
        self.driver.hide_keyboard()
        to_acc = self.driver.find_element_by_xpath(
            '//*[@class="OtpCommonMobileBundle-OtpCommonStyle-filterPanelTab OtpPaymentMobileBundle-OtpPaymentStyle-paymentItemFilterPanelTab"]')
        tap(self, to_acc)
        sleep(2)
        popolnenie = self.driver.find_elements_by_xpath(
            '//*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetCurrency"]')
        for i in popolnenie:
            if i.is_displayed():
                tap(self, i)
                break
        tap(self, nxtbtn)
    elif type == 'a2a':
        self.driver.switch_to.context('WEBVIEW')
        self.driver.hide_keyboard()
        from_acc = self.driver.find_element_by_xpath(
            '//*[@class="OtpCommonMobileBundle-OtpCommonStyle-filterPanelTab OtpPaymentMobileBundle-OtpPaymentStyle-paymentItemFilterPanelTab"]')
        tap(self, from_acc)
        sleep(2)
        spisok = self.driver.find_elements_by_xpath(
            '//*[@class="OtpPaymentMobileBundle-OtpPaymentStyle-itemAmountContainer"]')
        for i in spisok:
            if i.is_displayed() and i.find_element_by_xpath(
                    './/*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetAmount OtpPaymentMobileBundle-OtpPaymentStyle-itemAmountWidgetAmount"]').get_attribute(
                'textContent') != '0.' and i.find_element_by_xpath(
                './/*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetCurrency"]').get_attribute(
                'textContent') == valuta:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", i)
                tap(self,
                    i.find_element_by_xpath(
                        './/*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetCurrency"]'))
                break
        nxtbtn = self.driver.find_element_by_xpath(
            '//*[@class="OtpCommonMobileBundle-OtpCommonStyle-headerButtonNext"]')
        tap(self, nxtbtn)
        self.driver.hide_keyboard()
        to_acc = self.driver.find_element_by_xpath(
            '//*[@class="OtpCommonMobileBundle-OtpCommonStyle-filterPanelTab OtpPaymentMobileBundle-OtpPaymentStyle-paymentItemFilterPanelTab"]')
        tap(self, to_acc)
        sleep(2)
        popolnenie = self.driver.find_elements_by_xpath(
            '//*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetCurrency"]')
        for i in popolnenie:
            if i.is_displayed():
                tap(self, i)
                break
        tap(self, nxtbtn)
    elif type == 'a2c':
        self.driver.switch_to.context('WEBVIEW')
        self.driver.hide_keyboard()
        from_acc = self.driver.find_element_by_xpath(
            '//*[@class="OtpCommonMobileBundle-OtpCommonStyle-filterPanelTab OtpPaymentMobileBundle-OtpPaymentStyle-paymentItemFilterPanelTab"]')
        tap(self, from_acc)
        sleep(2)
        spisok = self.driver.find_elements_by_xpath(
            '//*[@class="OtpPaymentMobileBundle-OtpPaymentStyle-itemAmountContainer"]')
        for i in spisok:
            if i.is_displayed() and i.find_element_by_xpath(
                    './/*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetAmount OtpPaymentMobileBundle-OtpPaymentStyle-itemAmountWidgetAmount"]').get_attribute(
                'textContent') != '0.' and i.find_element_by_xpath(
                './/*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetCurrency"]').get_attribute(
                'textContent') == valuta:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", i)
                tap(self,
                    i.find_element_by_xpath(
                        './/*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetCurrency"]'))
                break
        nxtbtn = self.driver.find_element_by_xpath(
            '//*[@class="OtpCommonMobileBundle-OtpCommonStyle-headerButtonNext"]')
        tap(self, nxtbtn)
        self.driver.hide_keyboard()
        popolnenie = self.driver.find_elements_by_xpath(
            '//*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetAmount OtpPaymentMobileBundle-OtpPaymentStyle-itemAmountWidgetAmount"]')
        tap(self, popolnenie[0])
        tap(self, nxtbtn)

    elif type == 'c2u':
        self.driver.switch_to.context('WEBVIEW')
        self.driver.hide_keyboard()
        spisok = self.driver.find_elements_by_xpath(
            '//*[@class="OtpPaymentMobileBundle-OtpPaymentStyle-itemAmountContainer"]')
        for i in spisok:
            if i.find_element_by_xpath(
                    './/*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetAmount OtpPaymentMobileBundle-OtpPaymentStyle-itemAmountWidgetAmount"]').get_attribute(
                'textContent') != '0.' and i.find_element_by_xpath(
                './/*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetCurrency"]').get_attribute(
                'textContent') == valuta:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", i)
                tap(self,
                    i.find_element_by_xpath(
                        './/*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetCurrency"]'))
                break
        nxtbtn = self.driver.find_element_by_xpath(
            '//*[@class="OtpCommonMobileBundle-OtpCommonStyle-headerButtonNext"]')
        tap(self, nxtbtn)
        mfo = self.driver.find_element_by_xpath(
            '//*[@class="gwt-TextBox OtpCommonMobileBundle-OtpCommonStyle-clearBackground"]')
        mfo.send_keys(ukraine_mfo)
        accno = self.driver.find_element_by_xpath(
            '//*[@placeholder="Recipient account number"]')
        accno.send_keys(ukraine_accno)
        self.driver.hide_keyboard()
        nam = self.driver.find_element_by_xpath(
            '//*[@class="OtpPaymentMobileBundle-OtpPaymentStyle-recepientPanel"]/input[1]')
        nam.send_keys(name)
        self.driver.hide_keyboard()
        taxid = self.driver.find_element_by_xpath(
            '//*[@class="OtpPaymentMobileBundle-OtpPaymentStyle-recepientPanel"]/input[2]')
        taxid.send_keys(ukraine_inn)
        nxtbtn = self.driver.find_element_by_xpath(
            '//*[@class="OtpCommonMobileBundle-OtpCommonStyle-headerButtonNext"]')
        tap(self, nxtbtn)

    elif type == 'a2u':
        self.driver.switch_to.context('WEBVIEW')
        self.driver.hide_keyboard()
        from_acc = self.driver.find_element_by_xpath(
            '//*[@class="OtpCommonMobileBundle-OtpCommonStyle-filterPanelTab OtpPaymentMobileBundle-OtpPaymentStyle-paymentItemFilterPanelTab"]')
        tap(self, from_acc)
        sleep(2)
        spisok = self.driver.find_elements_by_xpath(
            '//*[@class="OtpPaymentMobileBundle-OtpPaymentStyle-itemAmountContainer"]')
        for i in spisok:
            if i.is_displayed() and i.find_element_by_xpath(
                    './/*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetAmount OtpPaymentMobileBundle-OtpPaymentStyle-itemAmountWidgetAmount"]').get_attribute(
                'textContent') != '0.' and i.find_element_by_xpath(
                './/*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetCurrency"]').get_attribute(
                'textContent') == valuta:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", i)
                tap(self,
                    i.find_element_by_xpath(
                        './/*[@class="OtpCommonMobileBundle-OtpCommonStyle-amountWidgetCurrency"]'))
                break
        nxtbtn = self.driver.find_element_by_xpath(
            '//*[@class="OtpCommonMobileBundle-OtpCommonStyle-headerButtonNext"]')
        tap(self, nxtbtn)
        mfo = self.driver.find_element_by_xpath(
            '//*[@class="gwt-TextBox OtpCommonMobileBundle-OtpCommonStyle-clearBackground"]')
        mfo.send_keys(ukraine_mfo)
        accno = self.driver.find_element_by_xpath(
            '//*[@placeholder="Recipient account number"]')
        accno.send_keys(ukraine_accno)
        self.driver.hide_keyboard()
        nam = self.driver.find_element_by_xpath(
            '//*[@class="OtpPaymentMobileBundle-OtpPaymentStyle-recepientPanel"]/input[1]')
        nam.send_keys(name)
        self.driver.hide_keyboard()
        taxid = self.driver.find_element_by_xpath(
            '//*[@class="OtpPaymentMobileBundle-OtpPaymentStyle-recepientPanel"]/input[2]')
        taxid.send_keys(ukraine_inn)
        nxtbtn = self.driver.find_element_by_xpath(
            '//*[@class="OtpCommonMobileBundle-OtpCommonStyle-headerButtonNext"]')
        tap(self, nxtbtn)