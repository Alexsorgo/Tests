import getopt
import inspect
import os

import sys
import unittest

import constants
from Android.OTP.main import Androidrules
from iphone.OTP.main import Iphonerules

project = constants.project
platform = constants.platform
login = constants.login
password = constants.password


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hb:o:l:p:", ["bank=", "os=", "login=", "password="])
    except getopt.GetoptError:
        print """launch.py takes next args:
            -h - help
            -o - platform name, iOS or Android (default Android)
            -b - bank name (default OTP)
            -l - login specific user (default = AUTOTEST)
            -p - password for this user (default = 321)"""
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print """launch.py takes next args:
            -h - help
            -o - platform name, iOS or Android (default Android)
            -b - bank name (default OTP)
            -l - login specific user (default = AUTOTEST)
            -p - password for this user (default = 321) """
            sys.exit()
        elif opt in ("-b", "--bank"):
            global project
            project = arg.upper()
        elif opt in ("-o", "--os"):
            global platform
            platform = arg.upper()
        elif opt in ("-l", "--login"):
            global login
            login = arg.upper()
        elif opt in ("-p", "--password"):
            global password
            password = arg


def fil():
    print platform + ' ' + project
    if platform == 'ANDROID':
        if project == 'OTP':
            if __name__ == '__main__':
                suite = unittest.TestLoader().loadTestsFromTestCase(Androidrules)
                unittest.TextTestRunner(verbosity=2).run(suite)
        elif project == 'PIB':
            execfile('/Users/admin/PycharmProjects/autotest/Android/OTP/pib_bank.py')

    if platform == 'IOS':
        if project == 'OTP':
            if __name__ == '__main__':
                suite = unittest.TestLoader().loadTestsFromTestCase(Iphonerules)
                unittest.TextTestRunner(verbosity=2).run(suite)
        elif project == 'PIB':
            print 'pib ios'



if __name__ == '__main__':
    main(sys.argv[1:])
    fil()
