# by luffycity.com
import time
import socket
import threading

def task(conn):
    time.sleep(15)
    data=conn.recv(1024)
    print(data.decode('utf-8'))
    conn.close()


sock=socket.socket()
sock.bind(('192.168.31.194',65320))
sock.listen(5)

while True:
    conn,addr=sock.accept()
    t=threading.Thread(target=task,args=(conn,))
    t.start()
    
    





























#
#def task(conn):
#    time.sleep(20)
#    data = conn.recv(1024)
#    print(data)
#    conn.close()
#
#
#server = socket.socket()
#server.bind(('192.168.13.84',8001,))
#server.listen(5)
#
#while True:
#    conn,addr = server.accept()
#    t = threading.Thread(target=task,args=(conn,))
#    t.start()