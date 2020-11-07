#第一题
'''
class Foo:
    list_display=[]
    def get_list(self):
        self.list_display.insert(0,33)
        return self.list_display
    
s1=Foo()
result1=s1.get_list()
print(result1)
result2=s1.get_list()
print(result2)
''' 

#第二题
'''
class Foo:
    list_display=[]
    def get_list(self):
        self.list_display.insert(0,33)
        return self.list_display
    
class Foo2(Foo):
    list_display=[11,22]
    
s1=Foo()
s2=Foo()
result1=s1.get_list()
print(result1)
result2=s2.get_list()
print(result2)
print(id(s1.get_list()),id(s2.get_list()))
'''


#第三题
'''
class Foo:
    list_display=[]
    def get_list(self):
        self.list_display.insert(0,33)
        return self.list_display
    
class Foo2(Foo):
    list_display=[11,22]
    
s1=Foo()
s2=Foo2()

result1=s1.get_list()
print(result1)

result2=s2.get_list()
print(result2)
'''

#第四题
'''
class Foo:
    list_display=[]
    def get_list(self):
        self.list_display.insert(0,33)
        return self.list_display
    
class Foo2(Foo):
    list_display=[11,22]
    
s1=Foo2()
s2=Foo2()

result1=s1.get_list()
print(result1)

result2=s2.get_list()
print(result2)
'''


class Foo:
    lst=['','login','logout','register']
    def login(self):
        print('当前为登陆')
        
    def logout(self):
        print('当前为注销')
        
    def resgister(self):
        print('当前为注册')
        
    def run(self):
        print("""
          请输入你要选择的序号:
            1.登陆
            2.注销
            3.注册
              """)
        val=int(input('请输入:'))
        value=Foo.lst[val]
        a=getattr(self,value)
        a()
        
obj=Foo()
obj.run()
        
        







































