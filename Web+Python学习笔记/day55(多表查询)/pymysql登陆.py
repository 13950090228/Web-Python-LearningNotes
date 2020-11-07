import pymysql as py
# lid=input('请输入序号：')
user = input('请输入用户名：')
pawd = input('请输入密码：')
#建立连接
text = '进入大学以来我就'
conn=py.connect(
        host='localhost', 
        user='root', 
        password="",       
        database='db2', 
        port=3306, 
        unix_socket=None,
        charset='utf8'
)
#创建游标
cur = conn.cursor()
# sql = 'select * from login where user=%s and pawd=%s'
sql = 'insert into login(user,pawd) value(%s,%s)'
res = cur.execute(sql,[user,pawd])
print(res)

conn.commit()
cur.close()
conn.close()

# if res:
#     print('登陆成功')
# else:
#     print('失败')













# cur = conn.cursor(cursor=py.cursors.DictCursor)
# sql = 'select * from login'
# sql='insert into file (id,"") value(%s,%s,%s)'
# res=cur.execute(sql,[lid,user,text])
# #res=cur.execute(sql)
# print(res)
# conn.commit()
# result=cur.fetchmany()
# print(result)

#游标关闭，连接关闭
# cur.close()
# conn.close()





