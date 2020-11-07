import socketserver
import json
import hashlib

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        while 1:
            data=self.request.recv(1024).decode('utf8')
            file_info=json.loads(data)
            print(file_info)
            
            action=file_info.get('action')
            filename=file_info.get('filename')
            filesize=file_info.get('filesize')
            
            self.request.send(b'200')
            res=filename.split('\\')[-1]
            
            
            with open('put/'+res,'ab') as f:
                recv_data_length=0
                all_data=b''
                while recv_data_length<filesize:
                    data=self.request.recv(2048)
                    recv_data_length+=len(data)
                    all_data+=data
                    f.write(data)
                    print('文件总大小为：%sB,已接受%sB'%(filesize,recv_data_length))
                    
            print('文件接收成功!!')
            self.request.send(b'Server file received successfully')
            res=self.request.recv(1024).decode('utf8')
            res=json.loads(res)
            print('客户端的加密密文为：%s'%(res))
    
            md5=hashlib.md5()
            md5.update(all_data)
            md5s=md5.hexdigest()
            md5s_json=json.dumps(md5s).encode("utf-8")
            self.request.send(md5s_json)
            
            if md5s == res:
                print('文件已完整接收')
            else:
                print('文件未被完整接收')
    
server=socketserver.ThreadingTCPServer(('192.168.31.194',65320),Myserver)
server.serve_forever()
    