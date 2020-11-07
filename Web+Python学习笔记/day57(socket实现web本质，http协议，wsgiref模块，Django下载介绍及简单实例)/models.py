import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password="",
    database='db13',
    port=3306,
    charset='utf8'
)