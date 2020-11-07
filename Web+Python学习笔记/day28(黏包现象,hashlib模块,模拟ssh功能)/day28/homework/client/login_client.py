

import socket

sock=socket.socket() # TCP
sock.connect(('192.168.31.194',65320))

while 1:
    user=input("用户名>>>>")
    pwd=input("密码>>>>")
    val=("%s|%s"%(user,pwd)).encode("utf8")
    sock.send(val)
    response=sock.recv(1024)
    print(response.decode("utf8"))
    if response.decode("utf8")=="success":
        break
    else:
        print("用户名或者密码错误！")
        continue

