import handler
from types import FunctionType,MethodType
class Foo:
#    def __call__(self,*args,**kwargs):
#        pass
    def func(self):
        pass

def func(*args):
    pass
obj=Foo()
getattr(handler,'参数')   #根据字符串的形式，去对象中找成员
#v1=getattr(handler,'f1')
#v1()

hasattr(handler,'参数')   #根据字符串的形式，去判断对象中是否有成员
#v2=hasattr(handler,'f1')
#print(v2)

setattr(handler,'b',777)   #根据字符串的形式，去对象动态的设置一个成员（内存）
setattr(handler,'f4',lambda x:x+1)   #创建函数会把原来同名的覆盖
#只会在内存增加不会显示在模块中

delattr(handler,'f1')   #根据字符串的形式，去对象动态的删除一个成员（内存）

print(callable(func)) #判断输入的参数是否可以调用
print(isinstance(obj.func,MethodType))
















