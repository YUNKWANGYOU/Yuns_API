import pymysql
import warnings
import json
import os

admin_file = open('/home/svcapp_su/Yuns_API/ApplicationInfo.json')
admin_dict = json.load(admin_file)
sql_dict = admin_dict['mysql_db']

sql_host = sql_dict['host']
sql_user = sql_dict['user']
sql_passwd = sql_dict['passwd']
sql_charset = sql_dict['charset']

LIST_MAX_COUNT = 20
DETAIL_MAX_LEN = 700


class DBHandler:
    def __init__(self):
        pass

    def connectiondb(dbname):
        try:
            con = pymysql.connect(host = sql_host,
                       user = sql_user,
                       password = sql_passwd,
                       db = dbname,
                       charset = 'utf8')
            return con
        except Exception as e:
            mylogger.error(str(e))
	
    def input_chat_id(input):
        try:
            sql = f"INSERT INTO yunsdb.telegram_api_chat_id (chat_id) VALUES ('%{input}%');"
            with DBHandler.connectiondb('coreops') as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                    conn.commit()
                    return True
        except Exception as e:
            return False
    
# test
if __name__=='__main__':
    pass
#DBHandler.get_deviceinfo_list('smsc')
#res = DBHandler.get_rm_list("sms")
# print(f"길이 : {len(res)}")
# for data in res:
#     print(data[1])
