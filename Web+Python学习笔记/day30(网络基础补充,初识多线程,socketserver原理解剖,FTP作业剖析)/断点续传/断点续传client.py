import socket
import os
import json

client=socket.socket()
client.connect(('192.168.31.194',65320))

while True:
    filename=input('请输入要传输的文件名：')
    if filename == 'exit':
        break
    filesize=os.path.getsize(filename)
    client.send(filename.encode('utf-8'))
    res=client.recv(1024).decode('utf-8')
    name=filename.split('\\')[-1]
    print('响应为：%s'%(res))
    json_name=json.dumps(name).encode("utf-8")
    client.send(json_name)
    Filesize=client.recv(1024).decode('utf-8')
    Filesize=json.loads(Filesize)
    
    if Filesize == filesize:
        print('目标文件完整')
    elif Filesize < filesize:
        print('文件不完整：%s'%(Filesize))
        with open(filename,mode='rb') as f:
            f.seek(Filesize)
            for line in f:
                client.send(line)
            print('文件发送完毕！')
    else:
        print('文件大小有误')
    
    
        
        