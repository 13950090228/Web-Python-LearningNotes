# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:30:59 2019

@author: 50671
"""

## by luffycity.com
#
import socket
import pymysql

server = socket.socket()
server.bind(('192.168.31.194',65320))
server.listen(5)
con = pymysql.connect(
    host='localhost',
    user='root',
    password="",
    database='db2',
    port=3306,
    charset='utf8'
)
cur=con.cursor()
while True:
    print('服务端准备开始接收客户端的连接')
    conn,addr = server.accept()
    
    while True:
        print('已经有人连接上了：')
        user = conn.recv(1024)
        pawd = conn.recv(1024)
        if user == b'exit':
            print('用户已退出')
            break
        
        print('接收账号为：',user.decode('utf-8'))  
        print('接收密码为：',pawd.decode('utf-8'))
        sql='select * from login where user=%s and pawd=%s'
        res=cur.execute(sql,[user.decode('utf-8'),pawd.decode('utf-8')])

        if res:
            response='登陆成功'
            conn.send(response.encode('utf-8'))
        
        else:
            response='登陆失败'
            conn.send(response.encode('utf-8'))
   
    conn.close()


