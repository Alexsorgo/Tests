# -*- coding: utf-8 -*-
import os
import re
import xml.etree.ElementTree as ET
import requests
import sys
from requests.packages import urllib3
from iphone.OTP.hash import enc, decd

# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('windows-1251')
print sys.getdefaultencoding()


def credit_req():
    body = """<?xml version="1.0"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"><SOAP-ENV:Body SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><NS1:callService xmlns:NS1="http://ift.webservices.ifobs.cs.com/"><sWebServiceXML xsi:type="xsd:string">H4sIAAAAAAAAA21S70/CMBD9V5p+FrYOBjPpRoREJTGOOJXPZb2x6miXtvzwv7dlRkD8dNe7e3fvvY1ODpsG7UAboWSKST/ECGSpuJDrFO+F5GpveiSKCZ5kVNzn02IJqwL0TpSwYOUn2Ix28REYB53RAqSLc1mpjN61bSNKZt1yxMFjUuwuKJNikRck7If9yB08QLm1bNW47kLsOEj5hc9JRW6OkEGMEWvF+xlZT1eyjcMdqfXEolYSMKqZ5q52fCU3BAeelvEwzwsJ18SIS+ODMlsD2mVu6EmVrAHUMK8epC8FF3q2tu6yN4dBjVoLR6TIXx5yjFpmzF75w5xUnIyjJKzGpCqrEWcVDEfJEBKIB+EwOe497QouDexeU8W/MjpjTeM+xY/hyHSxk+wpLIWtZ6CtqLzNYLCHa9e2zqWOpW/PeRYPRsk4vCWEBmdV+qqZNK3S9nrsb4vO1FZaD85XH1Bakz0rGlwVvZwTg+BSwa/YTl6XF2ItvSP//17foow5QaMCAAA=</sWebServiceXML></NS1:callService></SOAP-ENV:Body></SOAP-ENV:Envelope>"""
    urllib3.disable_warnings()
    r = requests.post(url='https://192.168.7.9:8943/WMService', data=body, verify=False)
    f = open('/Users/admin/PycharmProjects/OTP/xmls/login.xml', 'wb')
    f.write(r.text)
    f.close()

    tree = ET.parse('/Users/admin/PycharmProjects/OTP/xmls/login.xml')
    root = tree.getroot()
    data = root.find('{http://schemas.xmlsoap.org/soap/envelope/}Body').find(
        '{http://ift.webservices.ifobs.cs.com/}callServiceResponse').find('callServiceReturn').text
    dt = enc(data)
    f = open('/Users/admin/PycharmProjects/OTP/xmls/enc_login.xml', 'wb')
    f.write(dt)
    f.close()

    tree = ET.parse('/Users/admin/PycharmProjects/OTP/xmls/enc_login.xml')
    root = tree.getroot()
    w = root.find('SenderInfo').find('SessionInfo').attrib

    credit_tree = ET.parse('/Users/admin/PycharmProjects/OTP/xmls/enc_credits.xml')
    root = credit_tree.getroot()
    root.find('PacketHeader').find('SenderInfo').find('SessionInfo').set('id', w.get('id'))
    credit_tree.write('/Users/admin/PycharmProjects/OTP/xmls/credits.xml')
    f = open('/Users/admin/PycharmProjects/OTP/xmls/credits.xml', 'rb')
    data = f.read()
    f.close()

    body = """<?xml version="1.0"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"><SOAP-ENV:Body SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><NS1:callService xmlns:NS1="http://ift.webservices.ifobs.cs.com/"><sWebServiceXML xsi:type="xsd:string">%s</sWebServiceXML></NS1:callService></SOAP-ENV:Body></SOAP-ENV:Envelope>""" % decd(data)
    r = requests.post(url='https://192.168.7.9:8943/WMService', data=body, verify=False)
    f = open('/Users/admin/PycharmProjects/OTP/xmls/some.xml', 'wb')
    f.write(r.text)
    f.close()

    tree = ET.parse('/Users/admin/PycharmProjects/OTP/xmls/some.xml')
    root = tree.getroot()
    data = root.find('{http://schemas.xmlsoap.org/soap/envelope/}Body').find(
        '{http://ift.webservices.ifobs.cs.com/}callServiceResponse').find('callServiceReturn').text
    dt = enc(data)
    f = open('/Users/admin/PycharmProjects/OTP/xmls/enc_data.xml', 'wb')
    f.write(dt)
    f.close()


def cards_req():
    body = """<?xml version="1.0"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"><SOAP-ENV:Body SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><NS1:callService xmlns:NS1="http://ift.webservices.ifobs.cs.com/"><sWebServiceXML xsi:type="xsd:string">H4sIAAAAAAAAA21SYU/CMBD9K00/y7Y6GTMpI0o0khhHsqGfS3uD6myXtoD+e9vNCKif7np37+69t9HZx3uL9mCs1GqKSZRgBIprIdVmig9SCX2wI3I5JnhWUHlf3lYvsK7A7CWHJeNv4Ao6xAdgAkxBK1A+LlSjC3rTda3kzPnlSEDATLG/oO0Uy7IiSZREl/7gB/CdY+vWd8t6iU/5pBGJrvwM6+TzCcvAU7F3D+g5jeRyqxVgtGVG+Fr/yi8IjgMfG2CBEJK+iZFQNgRtdxaMz/zQo+asBdSyIBtUKMVnQnZuO2Qrj0Gt3khP5GZVl/VdVWPUMWsPOtzO8zFPsiwXWZM2GZA1pGTCeAI5nwBjV/3q47r43LzhdavFZ0HnrG39Z/g2G9khDqoDixfptnMwTjbBYrA4wI1vO2/UQDS0F6IYp1k+Sa4JofFJldaGKdtp4/6O/W7Rud4pF8Dl+hW4s8WTpvGfYu/TXAuIe2VHMvG5mB/dg9Ihr+RGBdz/f9kXWQHnXqoCAAA=</sWebServiceXML></NS1:callService></SOAP-ENV:Body></SOAP-ENV:Envelope>"""
    urllib3.disable_warnings()
    r = requests.post(url='https://192.168.7.9:8943/WMService', data=body, verify=False)
    path_login = '%s/sql/xmls/login.xml' % os.getcwd()
    f = open(path_login, 'wb')
    f.write(r.text)
    f.close()

    tree = ET.parse(path_login)
    root = tree.getroot()
    data = root.find('{http://schemas.xmlsoap.org/soap/envelope/}Body').find(
        '{http://ift.webservices.ifobs.cs.com/}callServiceResponse').find('callServiceReturn').text
    dt = enc(data)
    path_enclogin = '%s/sql/xmls/enc_login.xml' % os.getcwd()
    f = open(path_enclogin, 'wb')
    f.write(dt.encode('windows-1251'))
    f.close()

    tree = ET.parse(path_enclogin)
    root = tree.getroot()
    w = root.find('SenderInfo').find('SessionInfo').attrib

    path_enccards = '%s/sql/xmls/enc_cards.xml' % os.getcwd()
    credit_tree = ET.parse(path_enccards)
    root = credit_tree.getroot()
    root.find('PacketHeader').find('SenderInfo').find('SessionInfo').set('id', w.get('id'))
    path_cards = '%s/sql/xmls/cards.xml' % os.getcwd()
    credit_tree.write(path_cards)
    f = open(path_cards, 'rb')
    data = f.read()
    f.close()

    body = """<?xml version="1.0"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"><SOAP-ENV:Body SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><NS1:callService xmlns:NS1="http://ift.webservices.ifobs.cs.com/"><sWebServiceXML xsi:type="xsd:string">%s</sWebServiceXML></NS1:callService></SOAP-ENV:Body></SOAP-ENV:Envelope>""" % decd(data)
    r = requests.post(url='https://192.168.7.9:8943/WMService', data=body, verify=False)
    path_some = '%s/sql/xmls/some.xml' % os.getcwd()
    f = open(path_some, 'wb')
    f.write(r.text)
    f.close()

    tree = ET.parse(path_some)
    root = tree.getroot()
    data = root.find('{http://schemas.xmlsoap.org/soap/envelope/}Body').find(
        '{http://ift.webservices.ifobs.cs.com/}callServiceResponse').find('callServiceReturn').text
    dt = enc(data)
    path_enc = '%s/sql/xmls/enc_data.xml' % os.getcwd()
    f = open(path_enc, 'wb')
    f.write(dt.encode('windows-1251'))
    f.close()


def scheta_req():
    body = """<?xml version="1.0"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"><SOAP-ENV:Body SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><NS1:callService xmlns:NS1="http://ift.webservices.ifobs.cs.com/"><sWebServiceXML xsi:type="xsd:string">H4sIAAAAAAAAA21SYU/CMBD9K00/y7Y6GTMpI0o0khhHsqGfS3uD6myXtoD+e9vNCKif7np37+69t9HZx3uL9mCs1GqKSZRgBIprIdVmig9SCX2wI3I5JnhWUHlf3lYvsK7A7CWHJeNv4Ao6xAdgAkxBK1A+LlSjC3rTda3kzPnlSEDATLG/oO0Uy7IiSZREl/7gB/CdY+vWd8t6iU/5pBGJrvwM6+TzCcvAU7F3D+g5jeRyqxVgtGVG+Fr/yi8IjgMfG2CBEJK+iZFQNgRtdxaMz/zQo+asBdSyIBtUKMVnQnZuO2Qrj0Gt3khP5GZVl/VdVWPUMWsPOtzO8zFPsiwXWZM2GZA1pGTCeAI5nwBjV/3q47r43LzhdavFZ0HnrG39Z/g2G9khDqoDixfptnMwTjbBYrA4wI1vO2/UQDS0F6IYp1k+Sa4JofFJldaGKdtp4/6O/W7Rud4pF8Dl+hW4s8WTpvGfYu/TXAuIe2VHMvG5mB/dg9Ihr+RGBdz/f9kXWQHnXqoCAAA=</sWebServiceXML></NS1:callService></SOAP-ENV:Body></SOAP-ENV:Envelope>"""
    urllib3.disable_warnings()
    r = requests.post(url='https://192.168.7.9:8943/WMService', data=body, verify=False)
    path_login = '%s/sql/xmls/login.xml' % os.getcwd()
    f = open(path_login, 'wb')
    f.write(r.text)
    f.close()

    tree = ET.parse(path_login)
    root = tree.getroot()
    data = root.find('{http://schemas.xmlsoap.org/soap/envelope/}Body').find(
        '{http://ift.webservices.ifobs.cs.com/}callServiceResponse').find('callServiceReturn').text
    dt = enc(data)
    path_enclogin = '%s/sql/xmls/enc_login.xml' % os.getcwd()
    f = open(path_enclogin, 'wb')
    f.write(dt)
    f.close()

    tree = ET.parse(path_enclogin)
    root = tree.getroot()
    w = root.find('SenderInfo').find('SessionInfo').attrib

    path_encschet = '%s/sql/xmls/enc_scheta.xml' % os.getcwd()
    credit_tree = ET.parse(path_encschet)
    root = credit_tree.getroot()
    root.find('PacketHeader').find('SenderInfo').find('SessionInfo').set('id', w.get('id'))
    path_schet = '%s/sql/xmls/scheta.xml' % os.getcwd()
    credit_tree.write(path_schet)
    f = open(path_schet, 'rb')
    data = f.read()
    f.close()

    body = """<?xml version="1.0"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"><SOAP-ENV:Body SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><NS1:callService xmlns:NS1="http://ift.webservices.ifobs.cs.com/"><sWebServiceXML xsi:type="xsd:string">%s</sWebServiceXML></NS1:callService></SOAP-ENV:Body></SOAP-ENV:Envelope>""" % decd(
        data)
    r = requests.post(url='https://192.168.7.9:8943/WMService', data=body, verify=False)
    path_some = '%s/sql/xmls/some.xml' % os.getcwd()
    f = open(path_some, 'wb')
    f.write(r.text)
    f.close()

    tree = ET.parse(path_some)
    root = tree.getroot()
    data = root.find('{http://schemas.xmlsoap.org/soap/envelope/}Body').find(
        '{http://ift.webservices.ifobs.cs.com/}callServiceResponse').find('callServiceReturn').text
    dt = enc(data)
    path_enc = '%s/sql/xmls/enc_data.xml' % os.getcwd()
    f = open(path_enc, 'wb')
    f.write(dt)
    f.close()



