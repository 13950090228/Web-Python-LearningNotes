#a=10
#b=20
#c=30
#def fun1():
#    print('我是1')
#def fun2():
#    print('我是2')
#def fun3():
#    print('我是3')
#a=fun1()
#b=fun2()
#c=fun3()
#lst=[a,b,c]
#for i in lst:
#    i
#函数是变量名
#函数名可以作为参数传递给函数
#def my():
#    print('my')
#def proxy(fn):
#    print(fn)
#    fn()
#proxy(my)
#print(my)  #把函数名作为参数传递给另一个函数

#def fun1():
#    print('我是func1')
#def fun2():
#    print('我是func2')
#def func(fn,gn):  #函数名可以作为参数名进行传递
#    print('我是func')
#    fn()
#    gn()
#    print('啊啊啊')
#func(fun1,fun2)

#def func():
#    print('我是func')
#    def inner():
#        print('我是inner')
#    return inner()
#func()

#闭包，在内层函数访问外层函数的变量
#闭包的作用
#   1.保护你的变量不受侵害
#   2.可以让一个变量常驻内存
#a=10  #不安全
#def outer():
#    a=10
#    def inner():
#        print(a)
#    inner()
#    print(inner.__closure__)
#outer()

#def func():
#    a=10
#    def inner():
#        print(a)
#    print(inner.__closure__) #如果打印的不是None就是闭包
#func()   
#import time    
#def outer():
#    a=10
#    def inner():
#        print(a)
#    return inner
#outer()()
#outer()()
#ret=outer()  #常驻内存
#ret()
#ret()    
    
    
    
    
    
    
    
    
    
    
    



