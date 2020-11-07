import socket
import json 
import hashlib

# sock=socket.socket()
# sock.bind(('192.168.31.194',65320))
# sock.listen(5)

# while 1:
#     print('服务器工作中。。。。')
#     conn,addr=sock.accept()
#     while 1:
#         data=conn.recv(1024).decode('utf8')
#         file_info=json.loads(data)
#         print(file_info)
        
#         action=file_info.get('action')
#         filename=file_info.get('filename')
#         filesize=file_info.get('filesize')
        
#         conn.send(b'200')
#         res=filename.split('\\')[-1]
        
        
#         with open('put/'+res,'ab') as f:
#             recv_data_length=0
#             all_data=b''
#             while recv_data_length<filesize:
#                 data=conn.recv(2048)
#                 recv_data_length+=len(data)
#                 all_data+=data
#                 f.write(data)
#                 print('文件总大小为：%sB,已接受%sB'%(filesize,recv_data_length))
                
#         print('文件接收成功!!')
#         conn.send(b'Server file received successfully')
#         res=conn.recv(1024).decode('utf8')
#         res=json.loads(res)
#         print('客户端的加密密文为：%s'%(res))

#         md5=hashlib.md5()
#         md5.update(all_data)
#         md5s=md5.hexdigest()
#         md5s_json=json.dumps(md5s).encode("utf-8")
#         conn.send(md5s_json)
        
#         if md5s == res:
#             print('文件已完整接收')
#         else:
#             print('文件未被完整接收')
            
sock=socket.socket()
sock.bind(('127.0.0.1',8080))
sock.listen(5)
while 1:
    print('服务器运行中------------')
    conn,addr=sock.accept()
    while 1:
        print('开始接收：')
        res=conn.recv(8096)
        print(res)
        if res==b'':
            break


        
        
        
        
        
        
        
        
        
        
              