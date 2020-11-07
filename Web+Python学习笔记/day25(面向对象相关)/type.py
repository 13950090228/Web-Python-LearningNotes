class Foo:
    def f1(self):
        pass

obj=Foo()
print(obj,type(obj)) #获取当前对象由哪个类创建的
if type(obj) == Foo:
    print('obj是Foo类型 ')
    
print(isinstance(obj,Foo))  #判断第一个参数（对象）是不是第二个参数（类以及父类）的实例
"""
给你一个参数，判断对象是不是由某一个指定类创建 --> type(obj) == Foo
给你一个参数，判断对象是不是由某一个指定类或其父类的对象 --> isinstance(obj,Foo)
"""
