class Foo:
    def __init__(self):
        pass
    
    @property
    def start(self):
        return 1
    
obj=Foo()
print(obj.start)

#总结：
#       1.编写时
#           - 方法上方写 @property
#           - 方法参数:只有一个self
#       2.调用时：无需加括号  对象.方法
#       3.应用场景：对于简单的方法，当无需传参数且有返回值时可以使用



