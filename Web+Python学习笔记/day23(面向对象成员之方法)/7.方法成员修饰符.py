#私有的实例方法
'''
class Foo:
    def __init__(self):
        pass
    
    def __display(self,arg):
        print('私有静态 方法',arg)
        
    def fun(self):
        self.__display(12)
obj=Foo()
obj.fun()
#obj.__display(12)  无法访问
'''

class Foo:
    def __init__(self):
        pass
    @staticmethod
    def __display(arg):
        print('私有静态 方法',arg)
        
    @classmethod   
    def __fun(cls,x1):
        print(cls,x1)
        
    def func(self):
        Foo.__fun('私有类方法')
    
    

#Foo.__display(123)  #报错
obj=Foo()
obj.func()

 



