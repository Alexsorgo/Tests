import os

import cx_Oracle as cx_Oracle

from constants import bduser, bdpassword, dsn, ua_cur, accountNo

os.environ["NLS_LANG"] = ".UTF8"


def rules(rule_id, login):
    conn = cx_Oracle.connect(user=bduser, password=bdpassword, dsn=dsn)
    cursor = conn.cursor()
    cur = cursor.execute("SELECT cr.*, r.name FROM clientright cr, userrights ur, USERS u, RIGHT r WHERE u.id = (select id from users where login=:usr) AND ur.userid = u.id AND cr.id = ur.clientrightid AND r.rightid = cr.rightid", usr=login)
    ids = []
    for rule in cur.fetchall():
        ids.append(rule[2])
    if int(rule_id) in ids:
        cursor.execute("DELETE FROM USERRIGHTS where USERID = (SELECT id FROM users WHERE LOGIN=:usr) and CLIENTRIGHTID = (SELECT id FROM CLIENTRIGHT where RIGHTID = :rule and CLIENTID = (SELECT CLIENTID FROM USERS WHERE LOGIN=:usr))", usr=login, rule=int(rule_id))
        conn.commit()
        conn.close()
        print str(rule_id) + ' rule disable'
    elif int(rule_id) not in ids and int(rule_id) == 20:
        cursor.execute(
            "INsert into USERRIGHTS (USERID ,CLIENTRIGHTID) VALUES ((SELECT id FROM users WHERE LOGIN=:usr), (SELECT id FROM CLIENTRIGHT where RIGHTID = :rule and CLIENTID = (SELECT CLIENTID FROM USERS WHERE LOGIN=:usr)))",
            usr=login, rule=int(rule_id))
        conn.commit()
        cursor.execute(
            "insert into USERRIGHTVALUE (USERID, CLIENTRIGHTID, PARAMID, VALUE) VALUES ((SELECT id FROM users WHERE LOGIN=:usr), (SELECT id FROM CLIENTRIGHT where RIGHTID = 20 and CLIENTID = (SELECT CLIENTID FROM USERS WHERE LOGIN=:usr)), 1113, 1)", usr=login)
        conn.commit()
        conn.close()
        print str(rule_id) + ' rule enable'
    else:
        cursor.execute(
            "INsert into USERRIGHTS (USERID ,CLIENTRIGHTID) VALUES ((SELECT id FROM users WHERE LOGIN=:usr), (SELECT id FROM CLIENTRIGHT where RIGHTID = :rule and CLIENTID = (SELECT CLIENTID FROM USERS WHERE LOGIN=:usr)))", usr=login, rule=int(rule_id))
        conn.commit()
        conn.close()
        print str(rule_id) +' rule enable'


def user_block(login):
    conn = cx_Oracle.connect(user=bduser, password=bdpassword, dsn=dsn)
    cursor = conn.cursor()
    cur = cursor.execute("SELECT statusid FROM users WHERE login=:usr", usr=login)
    result = cur.fetchone()[0]
    if result == 0:
        cursor.execute("update users set statusid=1 where login=:usr", usr=login)
        conn.commit()
        conn.close()
        print 'User blocked'
    elif result == 1:
        cursor.execute(
            "update users set statusid=0 where login=:usr", usr=login)
        conn.commit()
        conn.close()
        print 'User unblocked'


def acc_rule13(login):
    conn = cx_Oracle.connect(user=bduser, password=bdpassword, dsn=dsn)
    cursor = conn.cursor()
    cur = cursor.execute("select * FROM USERACCOUNTRIGHT where userid = (SELECT id FROM USERS WHERE LOGIN=:usr)"
                         "and CLIENTACCOUNTRIGHTID = (select id from CLIENTACCOUNTRIGHT where "
                         "CLIENTID = (SELECT CLIENTID FROM USERS WHERE LOGIN=:usr) and "
                         "ACCOUNTID = (SELECT id FROM ACCOUNT where accountno = :accno and CURRENCYID= :cur)"
                         " and RIGHTID=13)", usr=login, accno=accountNo, cur=ua_cur)
    if not cur.fetchall():
        newid = cursor.execute("select id from USERACCOUNTRIGHT ORDER BY id DESC")
        newid = newid.fetchone()[0] + 1
        cursor.execute("INSERT INTO USERACCOUNTRIGHT (ID, userid, CLIENTACCOUNTRIGHTID) VALUES (:new, (SELECT id FROM USERS WHERE LOGIN=:usr), (select id from CLIENTACCOUNTRIGHT where CLIENTID = (SELECT CLIENTID FROM USERS WHERE LOGIN=:usr) and ACCOUNTID = (SELECT id FROM ACCOUNT where accountno =:accno and CURRENCYID=:cur) and RIGHTID=13))", new=newid, usr=login, accno=accountNo, cur=ua_cur)
        conn.commit()
        conn.close()
        print 'Schet enable'
    else:
        cursor.execute("DELETE FROM USERACCOUNTRIGHT where userid = (SELECT id FROM USERS WHERE LOGIN=:usr) and CLIENTACCOUNTRIGHTID = (select id from CLIENTACCOUNTRIGHT where CLIENTID = (SELECT CLIENTID FROM USERS WHERE LOGIN=:usr) and ACCOUNTID = (SELECT id FROM ACCOUNT where accountno = :accno and CURRENCYID=:cur) and RIGHTID=13)", usr=login, accno=accountNo, cur=ua_cur)
        conn.commit()
        conn.close()
        print 'Schet disable'


def passw_sql(login):
    conn = cx_Oracle.connect(user=bduser, password=bdpassword, dsn=dsn)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET password='885c0668d6f3f6e1be317ac0e8c7eaa4' where login=:usr", usr=login)
    conn.commit()
    conn.close()
    print 'Set password 321'


del os.environ["NLS_LANG"]
