# by luffycity.com

import socket

client = socket.socket()


client.connect(('192.168.31.194',65320))
while True:
    user=input('请输入账号：')
    client.send(user.encode('utf-8'))
    pawd=input('请输入密码：')
    client.send(pawd.encode('utf-8'))
    if user=='exit':
        break
    data = client.recv(1024)
    print(data.decode('utf-8'))
client.close()