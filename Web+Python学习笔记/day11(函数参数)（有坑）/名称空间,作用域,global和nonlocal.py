#1.内置  2.全局  3.局部
#a=10  #全局名称空间中的内容
#def fn():  #fn也在全局名称空间
#    b=20  #局部名称空间
#    print(a)
#    def gn():
#        print(b)
#    gn()
#    
#def vn():
#    pass
#fn()
# print(globals())#可以查看全局作用域中内容
# print(locals()) # 查看当前作作用域的内容

#def out():
#    print('哈哈')
#    def inner():
#        print('呵呵')
#        def inner1():
#            print('客客')
#        inner1()
#        print('吼吼')
#    def inner2():
#        print('嘿嘿')
#    inner2()
#    inner()            
#out()
#
#a=10  #全局变量本身是不安全的,不能随意修改
#def func():
#    global a  #可以把全局中的内容引入到函数内部 ， 在全局创建一个变量
##    a=20
#    a+=10
#    print(a)
#   
#func()   #在访问fun之后把全局中的a换成20
#print(a)
#
#def outer():
#    a=10
#    print(a)
#    def inner():
#        nonlocal a #寻找外层函数中离他最近的那个变量并修改他的值，但是不会去找全局
#        print(a)
#        a=20
#    inner()
#    print(a)
#outer()
#
#a=1
#def fun_1():
#    a=4
#    def fun_2():
#        a=8
#        def fun_3():
#            global a
#            a=2
#            print(a)
#        print(a)
#        fun_3()
#        print(a)
#    print(a)
#    fun_2()
#    print(a)
#print(a)
#fun_1()
#print(a)
#
#
#
#
#
#
#
#
#
#
