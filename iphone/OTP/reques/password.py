# -*- coding: utf-8 -*-
import os
import re
import xml.etree.ElementTree as ET

import cx_Oracle as cx_Oracle
import requests
import sys
from requests.packages import urllib3

import database.main as main
from hash import enc, decd

# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('windows-1251')
print sys.getdefaultencoding()

os.environ["NLS_LANG"] = ".UTF8"


# def password():
#     body = """<?xml version="1.0"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"><SOAP-ENV:Body SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><NS1:callService xmlns:NS1="http://ift.webservices.ifobs.cs.com/"><sWebServiceXML xsi:type="xsd:string">H4sIAAAAAAAAA21S0U7DMAz8lSjPsDbrWkDKimACgYTopBb27DbuFihJlaQM/p5kRbAxnuz4fM6dE3758daRdzRWajWnbBJTgqrRQqr1nG6lEnprT9k0ZfQy5/K2uC5XWJdo3mWDS2he0eV8jHcIAk3OS1Q+3qtW5/yq7zvZgPPDicDA8XdQou2cyqJk8YRN/BE/sBkc1J1Hi2pJ9/UkoSWbZZRAL5/3dAalCt48ZafqVC43WiElGzDC15YgZieMRkGPDaQgiEgPUSKUDUHbwaLxmW960A10SDoIts0QStGBkcFtxuzJc0in19LLuHqqiuqmrCjpwdqtDjenLUzPU2Q11hhDlk0TTBJom3gGrK1Fuhv9Oy46XN54utbiM+cL6Dr/DN/LJnaMo+egYiXdZoHGyTasGC0NdONh59c0Cg3wvcjTJDs/iy8Y49FelVcGlO21ccdtfyG+0INygVzUL9g4mz9qHh0Vd3taaIHRztmvmOjQzI/v0emYl3KtAu//X/YFIJfgyaoCAAA=</sWebServiceXML></NS1:callService></SOAP-ENV:Body></SOAP-ENV:Envelope>"""
#     urllib3.disable_warnings()
#     r = requests.post(url='https://192.168.7.9:8943/WMService', data=body, verify=False)
#     f = open('/Users/admin/PycharmProjects/OTP/xmls/login.xml', 'wb')
#     f.write(r.text)
#     f.close()
#
#     tree = ET.parse('/Users/admin/PycharmProjects/OTP/xmls/login.xml')
#     root = tree.getroot()
#     data = root.find('{http://schemas.xmlsoap.org/soap/envelope/}Body').find(
#         '{http://ift.webservices.ifobs.cs.com/}callServiceResponse').find('callServiceReturn').text
#     dt = enc(data)
#     f = open('/Users/admin/PycharmProjects/OTP/xmls/enc_login.xml', 'wb')
#     f.write(dt)
#     f.close()
#
#     tree = ET.parse('/Users/admin/PycharmProjects/OTP/xmls/enc_login.xml')
#     root = tree.getroot()
#     w = root.find('SenderInfo').find('SessionInfo').attrib
#
#     credit_tree = ET.parse('/Users/admin/PycharmProjects/OTP/xmls/enc_password.xml')
#     root = credit_tree.getroot()
#     root.find('PacketHeader').find('SenderInfo').find('SessionInfo').set('id', w.get('id'))
#     credit_tree.write('/Users/admin/PycharmProjects/OTP/xmls/password.xml')
#     f = open('/Users/admin/PycharmProjects/OTP/xmls/password.xml', 'rb')
#     data = f.read()
#     f.close()
#
#     body = """<?xml version="1.0"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"><SOAP-ENV:Body SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><NS1:callService xmlns:NS1="http://ift.webservices.ifobs.cs.com/"><sWebServiceXML xsi:type="xsd:string">%s</sWebServiceXML></NS1:callService></SOAP-ENV:Body></SOAP-ENV:Envelope>""" % decd(data)
#     requests.post(url='https://192.168.7.9:8943/WMService', data=body, verify=False)


def password():
    conn = cx_Oracle.connect(user=main.user, password=main.password, dsn=main.dsn)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET password='885c0668d6f3f6e1be317ac0e8c7eaa4' where login='COBEIN'")
    conn.commit()


del os.environ["NLS_LANG"]
