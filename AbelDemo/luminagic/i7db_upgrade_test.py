from os import environ
from mysql.connector import (connection)

conn = connection.MySQLConnection(user='lumimysql001%sharingan', 
                                 password=environ.get('MYSQLCONNSTR_DB_PWD', 'sharingan'),
                                 host='lumimysql001.mysqldb.chinacloudapi.cn',
                                 database='test')
cur = conn.cursor()
cur.execute('SELECT * FROM test.test0')
rows = cur.fetchall()

print('from azure test db:')
for row in rows:
    print(row)
conn.close()