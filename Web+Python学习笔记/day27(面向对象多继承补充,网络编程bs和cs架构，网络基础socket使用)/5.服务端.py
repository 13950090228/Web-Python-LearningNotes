# by luffycity.com

import socket

server = socket.socket()

server.bind(('192.168.31.194',65320))

server.listen(5)

while True:
    conn,addr = server.accept()
    print(conn)
    print(addr)
    # 字节类型
    while True:
        data = conn.recv(1024) # 阻塞
        if data == b'exit':
            break
        response = data + b' SB'
        conn.send(response)

    conn.close()