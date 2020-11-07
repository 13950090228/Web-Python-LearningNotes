# by luffycity.com


import  pymysql

# user = input('请输入用户名：')
# pawd = input('请输入密码：')

# 建立连接
conn = pymysql.connect(
    host='localhost',
    user='root',
    password="",
    database='db2',
    port=3306,
    charset='utf8'
)
# 创建游标
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
# sql = 'insert into login(user,pawd) values (%s,%s)'
# sql = 'select * from login where user=%s and pawd=%s'
sql = 'select * from login'
print(sql)

cur.execute(sql)
# print(res)

# result = cur.fetchall()   #获取所有的数据
# result = cur.fetchmany(3)   #获取3行数据
cur.scroll(0,mode='absolute')
cur.scroll(3,mode='relative')
result = cur.fetchone()
print(result)
# 增 删 改 一定要commit()
# conn.commit()

# 游标关闭 连接关闭
cur.close()
conn.close()

res=1
if res:
    print('对')
else:
    print('错')



