#class Base(object):
#    def send(self,x):
#        raise NotImplementedError('子类中必须实现send方法')
#
#class Foo(Base):
#    def send(self):
#        print('234')
# 
#
#obj = Foo()
#obj.send()

#from abc import ABCMeta,abstractmethod
#
#class Base(metaclass=ABCMeta):
#    def f1(self):
#        print(123)
#    @abstractmethod  
#    def f2(self):
#        pass
#
#class Foo(Base):
#    def f2(self):
#        print(666)
#
#obj=Foo()
#obj.f1()

 
#import hashlib
#
#obj=hashlib.md5()
#obj.update('懒趴给你含'.encode('utf8'))
#v=obj.hexdigest()
#print(v)


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def message(self):
        return "全栈15期%s,年龄:%s"%(self.name,self.age)
    

user=[person('大鸡哥',18),person('懒趴',88)]

for obj in user:
    print(obj.message())



























