import socketserver
import json
import os
code_dict={'1001':'上传文件，从头开始上传',
      '1002':'上传文件，断点续传',
      '1003':'上传文件，文件已存在且完整'
    }

def update(cmd_dict,conn,username):
    """
    cmd_dict:客户端传来的字典协议
    conn:self.request
    """
    file_name=cmd_dict['file_name']
    file_size=cmd_dict['file_size']
    file_name_path=os.path.join('home',username,file_name)
    
    exist = os.path.exists(file_name_path)
    if not exist:
        response={'code':1001}
        conn.sendall(json.dumps(response).encode('utf-8'))
        f = open(file_name_path, 'wb')
        recv_size = 0
        while recv_size < file_size:
            data = conn.recv(1024)
            f.write(data)
            f.flush()
            recv_size += len(data)
        f.close()
    else:
        exist_file_size=os.path.getsize(file_name_path)
        response={'code':1002,'size':exist_file_size}
        conn.sendall(json.dumps(response).encode('utf-8'))
        f = open(file_name_path, 'ab')
        recv_size = 0
        while recv_size < file_size:
            data = conn.recv(1024)
            f.write(data)
            f.flush()
            recv_size += len(data)
        f.close()
            
    
    
class NbServer(socketserver.BaseRequestHandler):
    def handle(self):
        """
        self.request=conn
        """
        cmd_bytes=self.request.recv(8096)
        cmd_dict=json.loads(cmd_bytes.decode('utf-8'))
        
        if cmd_dict['cmd'] == 'update':
            update(cmd_dict,self.request,'liuyongqi')
        else:
            pass
        
if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8001),NbServer)
    server.serve_forever()