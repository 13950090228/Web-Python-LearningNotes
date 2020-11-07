#1.开发一个消息提醒的功能（邮件/短信/微信）
#面向对象
#class Message:
#    def email(self,mail):
#        print(mail)
#    
#    def tel(self,num):
#        print(num)
#        
#    def msg(self):
#        print('短信')
#        
#obj=Message()
#obj.email('506713537')
#obj.tel('13950090228')
#obj.msg()
#
##函数式
#def email(mail):
#        print(mail)
#    
#def tel(num):
#    print(num)
#    
#def msg():
#    print('短信')
#
#email('506713537')
#tel('13950090228')
#msg()

class Shagou:
    def __init__(self,name,age,six):
        self.n1=name
        self.n2=age
        self.n3=six
    def run(self):
        print('%s今年%s,性别%s,喜欢跑步'%(self.n1,self.n2,self.n3))
    
    def drink(self):
        print('%s今年%s,性别%s,喜欢喝饮料'%(self.n1,self.n2,self.n3))

    def info(self):
        print('懒趴')
        
#obj=Shagou('傻狗','18','男')
#obj.run()
#obj.drink()



'''
练习：信息管理系统
    1.用户登陆
    2.显示当前用户信息
    3.查看当前用户所有的账单
    4.购买姑娘形状的抱枕
'''

#class User:
#    def __init__(self):
#        self.name=None
#    
#    def info(self):
#        print('%s的个人信息为：'%self.name)
#        
#    def money(self):
#        print('%s的账单为:'%self.name)
#        
#    def pay(self):
#        print('购买人女性抱枕')
#    def login(self):
#        name=input('输入一个账号：')
#        pawd=input('输入密码')
#        self.name=name
#        if pawd == 'sb':
#            print('登陆成功！')
#            while 1:
#                num=int(input("""
#                            输入1 显示个人信息
#                            输入2 显示账单
#                            输入3 购买抱枕
#                            输入其他值退出
#                              """))
#            
#                if num==1:
#                    self.info()
#                elif num == 2:
#                    self.money()
#                elif num == 3:
#                    self.pay()
#                else:
#                    break
#        else:
#            print('登录失败')
#obj=User()
#obj.login()              

class Person:
    def __init__(self,name,gen,age,fig):
        self.name=name
        self.gen=gen
        self.age=age
        self.fig=fig
    
    def gen1(self):
        print(self.name)
        print(self.gen-5)
        
    def age1(self):
        print(self.name)
        print(self.age-10)
        
    def fig1(self):
        print(self.name)
        print(self.fig-100)
        
a=Person('大鸡巴',99,18,1500)
a.age1()
b=Person('小鸡巴',89,28,1000)
b.age1()






