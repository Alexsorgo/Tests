import os
from time import sleep

import cx_Oracle as cx_Oracle

import re

from constants import bduser, bdpassword, dsn


def first_id(login):
    conn = cx_Oracle.connect(user=bduser, password=bdpassword, dsn=dsn)
    cursor = conn.cursor()
    cur = cursor.execute(
        "select * from IFOBSSMSDELIVERY where userid = (select id from users where login = :usr) order by id desc", usr=login)
    wtf = [x for x in cur]
    print wtf
    return wtf[0][0]


def find_sms(data, login):
    db = cx_Oracle.connect(user=bduser, password=bdpassword, dsn=dsn)
    cursor = db.cursor()
    loop = 0
    try:
        while loop < 50:
            cur = cursor.execute(
                "select * from IFOBSSMSDELIVERY where userid = (select id from users where login = :usr) order by id desc", usr=login)
            result2 = [x for x in cur]
            print loop
            second_id = result2[0][0]
            if data == second_id:
                loop += 1
                sleep(1)
            else:
                # cur = cursor.execute(
                #     "select * from IFOBSSMSDELIVERY where userid = (select id from users where login = :usr) order by id desc", usr=login)
                # state = [x[7] for x in cur]
                # if state == 2:
                cur = cursor.execute(
                    "select * from IFOBSSMSDELIVERY where userid = (select id from users where login = :usr) order by id desc",
                    usr=login)
                result1 = [x[5] for x in cur]
                result = re.findall(r'Kod: \d{6}', result1[0])
                sms = result[0][5:]
                db.close()
                print sms + ' its result'
                return sms
                # else:
                #     loop += 1
                #     sleep(1)
    except:
        raise
