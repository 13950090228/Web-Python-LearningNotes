class Foo:
    def f1(self):
        pass
    
    def f2(self):
        pass
    
    def f3(self):
        pass
    
    lst=[f1,f2]
obj=Foo()
Foo.lst.append(Foo.f3)   
print(Foo.lst)
def f3():
    pass
#判断是否是方法还是函数
lst=[]
from types import MethodType,FunctionType
def check(arg):
    if isinstance(arg,MethodType):
        print('这是一个方法')
    elif isinstance(arg,FunctionType):
        print('这是一个函数')
    else:
        print('什么都不是')
        
check(obj.f1)
check(f3)
check(lst)
