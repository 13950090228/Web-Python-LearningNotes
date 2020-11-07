import socket
import json
import os
import hashlib

sock=socket.socket()
sock.connect(('192.168.31.194',65320))

while 1:
    cmd=input('请输入命令：')

    if cmd == 'exit':
        break
    action,filename=cmd.strip().split(" ")
    filesize=os.path.getsize(filename)
    
    file_info={
            "action":action,
            "filename":filename,
            "filesize":filesize,
            }
    
    file_info_json=json.dumps(file_info).encode("utf8")
    sock.send(file_info_json)
    
    code=sock.recv(1024).decode('utf8')
    
    if code == '200':
        with open(filename,'rb') as f:
            f1=b''
            for line in f:
#                print(line)
                sock.send(line)
                f1+=line
            print('文件发送完毕')

    else:
        print('服务器发生异常')
        
    data=sock.recv(1024).decode('utf8')
    print(data)
    md5=hashlib.md5()
    md5.update(f1)
    md5s=md5.hexdigest()
    md5s_json=json.dumps(md5s).encode("utf-8")
    sock.send(md5s_json)
    
    res=sock.recv(1024).decode('utf8')
    res=json.loads(res)
    print('服务端的加密密文为：%s'%(res))
    if md5s == res:
        print('文件已完整接收')
    else:
        print('文件未被完整接收')
        
#filename='C:\\Users\\50671\\Desktop\\111.jpg'
#res=filename.split('\\')[-1]
#print(res)