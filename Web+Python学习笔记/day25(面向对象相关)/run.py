#f#import handler
#val=input('请输入：')
#if hasattr(handler,val):
#    func=getattr(handler,val)
#    func()
#else:
#    print('handler中不存在输入的属性')  
from types import MethodType,FunctionType
import handler
#val=input('请输入参数：')
#if hasattr(handler,val):
#    func=getattr(handler,val)   #根据字符串为参数，去模块中寻找与之同名的成员
#    print(func)
#    if isinstance(func,FunctionType):
#        func()
#    else:
#        print(func)
#else:
#    print('没有这个属性')
def func(): 
    objs = [] 
    name_list = dir(handler) 
    print(name_list) 
    
if __name__ == '__main__': 
    func()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    