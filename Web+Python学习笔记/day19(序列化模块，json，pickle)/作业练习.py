import json
import os
import pickle 
#1、写一个函数，接受一个参数，如果是文件，就执行这个文件，如果是文'夹就执行这个文件夹下的所有python文件。
#def make(file):
#    if os.path.isdir(file):
#        path=os.listdir(file)
#        for i in path:
#            fd=os.path.join(file,i)
#            if fd.endswith('.py'):
#                os.system('python %s'%fd)
#                
#    elif os.path.isfile(file) and file.endswith('.py'):
#        os.system('python %s' % file)
#make(r'D:\老男孩\day14(内置函数)')
#2、写一个copy函数，接受不了两个参数，第一个参数是源文件的位置，第二个参数是目标位置，将源文件copy到目标位置。
#def file(file1,file2):
#    if os.path.exists(file2):
#        print('已有同名文件')
#    else:
#        with open(file1,'rb') as f:
#            ret=f.read()
#        f.close()
#        with open(file2,'wb') as n:
#            n.write(ret)
#        n.close()
#file('json_file','pickle_file')

#3、获取某个文件所在的目录的上一级目录。
#ret=os.path.dirname('E:/QQ/文档数据/506713537/123.py')
#print(ret)

#4.
#os.makedirs('glance/api')
#open('glance/api/int_.py','w').close()

#5.写一个用户注册登陆的程序，每一个用户的注册都要把用户名和密码用字典格式写入文件
#在登陆的时候再从文件读取信息验证
#1.创建一个文件用来存放用户信息
#2.用户能进行注册并以字典类型存入
#3.登陆时若存在且输入正确则显示登陆成功
#4.不存在则提醒注册，密码错误提醒重新输入

#注册
def register():
    print('当前为注册\n')
    dic={}
    user=input('请输入用户名：')
    pawd=input('请输入密码：')
    dic.setdefault(user,pawd)
    
    with open('message','ab') as f:
        pickle.dump(dic,f)
    f.close()
    print('注册成功')
register()    
# 
def login():
    user=str(input('请输入用户名：'))
    pawd=str(input('请输入密码：'))
    with open('message','rb') as f:
        while True:
            try:
                ret=pickle.load(f)
                for i,j in ret.items():
                    if user == i and pawd == j:
                        print('登陆成功')
                        break
            except EOFError:
                print('登录失败')
                break        
    f.close()
login()  









