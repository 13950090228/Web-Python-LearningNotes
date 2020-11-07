#看代码写结果：
'''
class Foo:
    
    a2=22
    def __init__(self):
        self.a1=1
    a1=11
        
obj=Foo()
print(obj.a1)
print(obj.a2)
'''

#看代码打印每个结果
'''
class Foo:
    a1=11
    
    def __init__(self,num):
        self.a2=num
        
obj=Foo(999)
print(obj.a1)
print(obj.a2)
print(Foo.a1)
print(Foo.a2)
'''
'''
class Foo:
    a1=1
    __a2=2
    def __init__(self,num):
        self.num=num
        self.__salary=1000
        
    def get_data(self):
        print(self.__a2)
        print(self.num+self.a1)
        
obj =Foo(666)
print(obj.num)
print(obj.a1)
print(Foo.a1)
#报错
print(Foo.__a2)    
print(obj.__a2)
print(obj.__salary)
'''
'''   
class Foo:
    a1=1
    __a2=2
    def __init__(self,num):
        self.num=num
        self.__salary=1000
        
    def get_data(self):
        print(self.num+self.a1)  
    
obj1=Foo(666)
obj2=Foo(999)
#print(obj1.num)
#print(obj1.a1)  

obj1.num=18
obj1.a1=99
#print(obj1.num)
#print(obj1.a1) 

print(obj2.a1)
print(obj2.num+Foo.a1)
print(obj2.num+obj1.a1)
'''
'''
class Foo:
    hobby='大保健'
    
    def __init__(self,num):
        self.num=num
        self.__salary=1000
    @staticmethod      #静态方法
    def f1():
        print(Foo.hobby)
      
    def f2(self):      #实例方法
        print(Foo.hobby)
    @classmethod
    def f3(cls):       #类方法
        print(cls.hobby)
    
obj=Foo(1)
obj.f1()
obj.f2()
obj.f3()   
'''
'''
class Base:
    
    @classmethod
    def f3(cls):
        print(cls)
        
    def f1(self):
        print('base.f1')
        self.f3()
 
class Foo(Base):
    
    def f2(self):
        print('foo.f2')
        self.f1()
    
obj = Foo()
obj.f2()   
'''
'''
class fun:
    def __init__(self,pag,lst,num=10):
        self.pag=pag
        self.num=num
        self.lst=lst
    def start(self):
        return (self.pag-1)*self.num
    
    def end(self):
        return (self.pag-1)*self.num+self.num
    
    def show(self):
        for j in self.lst[self.start():self.end()]:
            print(j)
lst=[]
for i in range(1,901):
    lst.append('鸡巴 - %i' %i)
while True:
    try:
        num=10
        pag=int(input('请输入您想查看的页数：'))
        obj=fun(pag,lst)
        obj.show()
    except ValueError:
        print('请输入数字！！')
        break
'''
class School:
    def __init__(self,address):
        self.address=address
        
class Course:
    def __inti__(self,name,peroid,price):
        self.name=name
        self.peroid=peroid
        self.price=price
        
class Grade:
    def __init__(self,start,end,people,introduce):
      self.start=start
      self.end=end
      self.people=people
      self.introduce=introduce
      
s1=School('北京')
s2=School('上海')
s3=School('深圳')

c1=Course('linux','linux运维1期',2000)
c2=Course('linux','linux运维2期',2000)
c3=Course('linux','linux运维11期',2000)
c4=Course('linux','linux运维2期',2000)
c5=Course('python','全栈',2000)
      
      


















   
    
    
    
    


