'''
15. 补充代码实现：
user_list = []
while True:
user = input(“请输入用户名:”)
pwd = input(“请输入密码:”)
email = input(“请输入邮箱:”)
1. while循环提示用户输入：用户名、密码、邮箱（正则满足邮箱格式）
2. 为每个用户创建一个对象，并添加到列表中。
3. 当列表中的添加了3个对象后，跳出循环并以此循环打印所有用户的姓名和邮箱。如：
'''
#import re
#class User:
#    def __init__(self,user,pwd,email):
#        self.user=user
#        self.pwd=pwd
#        self.email=email
#        
#    def message(self):
#        print('用户名为:%s' %self.user)
#        print('邮箱为:%s'%self.email)
#
#user_list=[]
#while True:
#    num=int(input('输入 1 继续创建，输入其他退出'))
#    if num == 1:
#        user = input('请输入用户名:')
#        pwd = input('请输入密码:')
#        email = input('请输入邮箱:')
#        if re.match('\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}',email) == None:
#            print('邮箱格式不正确')
#            break
#        user_list.append(user)
#        user=User(user,pwd,email)
#        user.message()
#        print(user_list)
#    else:
#        break
  
'''
16.补充代码：实现用户注册和登陆
'''
class User:
    def __init__(self,name,pwd):
        self.name=name
        self.pwd=pwd

class Account(User):
    def __init__(self):

        self.user_list=[]
        
    def login(self):
        #用户登陆,输入账号密码，并在self.user_list判断用户是否存在
        name=input('输入您的账号：')
        pawd=input('输入您的密码:')
        flag=False
        for i in self.user_list:
            if name==i.name and pawd == i.pwd:
                flag=True
        if flag:
            print('登陆成功')
        else:
            print('登录失败')
        
    def register(self):
        #用户注册，动态创建User对象，并添加到self.user_list中
        print('注册中。。。。。。。。。。。。。')
        user=input('输入用户名：')
        pawd=input('输入密码：')
        num=User(user,pawd)
        self.user_list.append(num)
        
    def run(self):
        while True:
            choice=input('登陆选择 1，注册选择 2,退出 任意键')
            if choice == '1':
                self.login()
            elif choice == '2':
                self.register()
            else:
                break
            
    def dayin(self):
        print(self.user_list)
if __name__ == '__main__':
    obj=Account()
    obj.run()









          