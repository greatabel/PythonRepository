from os import environ
import pymysql.cursors

# 连接数据库
connect = pymysql.Connect(
    host='lumimysql001.mysqldb.chinacloudapi.cn',
    port=3306,
    user='lumimysql001%sharingan',
    passwd=environ.get('MYSQLCONNSTR_DB_PWD', 'sharingan'),
    db='test'
)

# 获取游标
cursor = connect.cursor()




# 查询数据
sql = "SELECT * FROM test.test0"

cursor.execute(sql )
for row in cursor.fetchall():
    print("Name:%s" % row)
print('共查找出', cursor.rowcount, '条数据')