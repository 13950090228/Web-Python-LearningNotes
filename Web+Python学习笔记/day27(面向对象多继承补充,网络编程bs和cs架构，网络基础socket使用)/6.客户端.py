# by luffycity.com


import socket

sk = socket.socket()

sk.connect(('192.168.31.194',65320))

while True:
    name = input("请输入姓名：")
    sk.send(name.encode('utf-8')) # 字节
    if name == 'exit':
        break

    response = sk.recv(1024) # 字节
    print(response.decode('utf-8'))

sk.close()
