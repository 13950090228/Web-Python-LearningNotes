import socket
import requests
from bs4 import BeautifulSoup
import greenlet
import gevent
import time
# r=requests.get('https://www.baidu.com/s?wd=alex',headers={
#             'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
#         })

# print(r.text)

# client=socket.socket()
# client.setblocking(False)
# try:   
#     client.connect(('www.baidu.com',80))    
# except BlockingIOError as e:
#     print(e)
# client.sendall(b'GET /s?wd=alex HTTP/1.0\r\nhost:www.baidu.com\r\n\r\n')

# chunk_list = []
# while True:
#     chunk = client.recv(8096)
#     if not chunk:
#         break
#     chunk_list.append(chunk)
    
# body=b''.join(chunk_list)
# print(body.decode('utf-8'))

# import select
# client1=socket.socket()
# client1.setblocking(False)
# try:
#     client1.connect(('www.baidu.com',80))
# except BlockingIOError:
#     pass

# client2=socket.socket()
# client2.setblocking(False)
# try:
#     client2.connect(('www.so.com',80))
# except BlockingIOError:
#     pass

# client3=socket.socket()
# client3.setblocking(False)
# try:
#     client3.connect(('www.sogou.com',80))
# except BlockingIOError:
#     pass

# socket_list=[client1,client2,client3]
# conn_list=[client1,client2,client3]

# while True:
#     rlist,wlist,elist=select.select(socket_list,conn_list,[],0.005)
#     for sk in wlist:
#         if sk == client1:
#             sk.sendall(b'GET /s?wd=alex HTTP/1.1\r\nhost:www.baidu.com\r\n\r\n')
            
#         if sk == client2:
#             sk.sendall(b'GET /s?q=alex HTTP/1.0\r\nhost:www.so.com\r\n\r\n')
            
#         if sk == client3:    
#             sk.sendall(b'GET /web?query=alex HTTP/1.0\r\nhost:www.sogou.com\r\n\r\n')
        
#         conn_list.remove(sk)
        
#     for sk in rlist:
#         chunk_list=[]
#         while True:
#             try:
#                 chunk=sk.recv(8096)
#                 if not chunk:
#                     break
#                 chunk_list.append(chunk)
#             except BlockingIOError:
#                 break
            
#         body=b''.join(chunk_list).decode('utf-8')
#         print('=============================================\n',body)
#         socket_list.remove(sk)
        
#     if not socket_list:
#         break



# def f1():
#     print('-')
#     print('111')
#     gr2.switch()
#     print('--')
#     print('222')
#     gr2.switch()
#     print('f1最后一行')
    
# def f2():
#     print('---')
#     print('333')
#     gr1.switch()
#     print('----')
#     print('444')
#     print('f2最后一行')


# gr1=greenlet.greenlet(f1)
# gr2=greenlet.greenlet(f2)

# f1()
# gr1.switch()


def f1(url):
    r=requests.get(url)
    print('--------------------------------------------',url,r.text[:500])

def f2(url):
    r=requests.get(url)
    print('--------------------------------------------',url,r.text[:500])
    
def f3(url):
    r=requests.get(url)
    print('--------------------------------------------',url,r.text[:500])


gevent.joinall([
    gevent.spawn(f1,'https://www.baidu.com/'),
    gevent.spawn(f2,'https://www.taobao.com/'),
    gevent.spawn(f3,'https://www.sogou.com/')
    ])















