import cx_Oracle as cx_Oracle
import re

import requests
from requests.packages import urllib3


class OracleDB:
    """
        Usage:
            db = OracleDB("user", "pass", "yourserver.com", 1523, "YOUR_SID")
            db.connect()
            db.cursor.execute("SELECT yourcolumn FROM yourtable")
            result1 = [x[0] for x in db.cursor]
            db.close()
            db.connect()
            db.cursor.execute("SELECT yourothercolumn FROM yourothertable")
            result2 = [x[0] for x in db.cursor]
            db.close()
            # do stuff with result1 and result2 ...
    """
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.commit = None

    def connect(self):
        # PIVD_TEST_1
        self.conn = cx_Oracle.connect(user="IFOBSBF", password="ifobs", dsn="(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=kerberos)(PORT=1521)))(CONNECT_DATA=(SERVER=DEDICATED)(SID=dev)))")
        # PIVD_TEST_2
        # self.connection = cx_Oracle.connect(user="ifobs", password="txs63441",
        #                                     dsn="(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=192.168.91.193)(PORT=1521)))(CONNECT_DATA=(SERVICE_NAME=ifobs)))")
        # OTP
        # self.connection = cx_Oracle.connect(user="IFOBS", password="ifobs",
        #                                             dsn="(DESCRIPTION =(ADDRESS_LIST =(ADDRESS = (PROTOCOL = TCP)(HOST = 10.45.233.68)(PORT = 1521)))(CONNECT_DATA =(SERVER = DEDICATED)(SERVICE_NAME = IFOBSTEST)))")
        self.cursor = self.conn.cursor()
        self.commit = self.conn.commit()


    def close(self):
        self.cursor.close()
        self.conn.close()

user = "IFOBSBF"
password="ifobs"
dsn="(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=kerberos)(PORT=1521)))(CONNECT_DATA=(SERVER=DEDICATED)(SID=dev)))"
# user = "IFOBS"
# password="ifobs"
# dsn="(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=10.247.5.121)(PORT=1521)))(CONNECT_DATA=(SERVER=DEDICATED)(SID=ifobstest)))"


def sql_req(data):
    urllib3.disable_warnings()
    requests.post("http://192.168.1.116:8088/sql2", data=data, verify=False)
