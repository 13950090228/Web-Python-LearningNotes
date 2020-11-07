import socket
import json 
import time
import os

cilent=socket.socket()
cilent.connect(('127.0.0.1',8001))

code_dict={'1001':'上传文件，从头开始上传',
      '1002':'上传文件，断点续传',
      '1003':'上传文件，文件已存在且完整'
    }

def Progress(size,total_size):
    """
    进度条功能
    size:当前文件大小
    total_size:文件总大小
    """
    
    val=int(size / total_size * 100)
    time.sleep(0.1)
    print('\r%s%%[%s]'%(val,'#'*val),end='')
          
def send_file(exist_file_size,intact_file_size):
    """
    文件发送功能（含续传）
    exist_file_size:已存在文件的大小
    intact_file_size:完整文件的大小
    """
    
    with open(file_path,'rb') as f:
        f.seek(exist_file_size)
        send_size=exist_file_size
        while send_size<intact_file_size:
            date=f.read(1024)
            cilent.sendall(date)
            send_size+=len(date)
            Progress(send_size,intact_file_size)
    print('上传成功！')

def update(file_path): 
    """
    文件上传功能
    file_path:需要上传的本地文件路径
    """
    file_name=os.path.basename(file_path)
    file_size=os.path.getsize(file_path)
    cmd_dict={'cmd':'update','file_name':file_name,'file_size':file_size}
    json_cmd_dict=json.dumps(cmd_dict)
    cilent.sendall(json_cmd_dict.encode('utf-8'))
    
    response=json.loads(cilent.recv(8096).decode('utf-8'))
    print(response)
    if response['code'] == 1001:
        send_file(0,file_size)
    else:
        exist_file_size=response['size']
        send_file(exist_file_size,file_size)
        
while True:
    res=input('请输入将要执行的操作和文件路径(以空格隔开)：')
    cmd,file_path=res.split(" ")
    if cmd == 'update':
        update(file_path)
    else:
        pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    