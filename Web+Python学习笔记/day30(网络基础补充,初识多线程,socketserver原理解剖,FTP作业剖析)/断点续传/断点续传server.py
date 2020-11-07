import socket
import os
import json

server=socket.socket()
server.bind(('192.168.31.194',65320))
server.listen(5)

while 1:
    print('服务器运行中。。。。')
    conn,addr=server.accept()
    
    while True:
        date=conn.recv(1024).decode('utf-8')
        print(date)
        conn.send(b'200')
        filesize=os.path.getsize(date)
        res=date.split('\\')[-1]
        name=conn.recv(1024).decode('utf8')
        name=json.loads(name)

        if os.path.exists(res):
            print('文件存在')
        else:
            print('文件不存在')
            
        Filesize=os.path.getsize(res)
        json_Filesize=json.dumps(Filesize).encode("utf-8")
        conn.send(json_Filesize)
        
        with open(res,mode='ab') as f:
            recv_date_length=Filesize
            all_date=b'' 
            f.seek(Filesize)

            while recv_date_length<filesize:
                date=conn.recv(1024)
                recv_date_length+=len(date)
                all_date+=date
                f.write(date)
        print('文件总大小为：%sB,已接受%sB'%(filesize,recv_date_length))
        

