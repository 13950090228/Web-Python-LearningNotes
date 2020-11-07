##普通的函数
#def fun(n):
#    return n*n
#print(fun(7))
##匿名函数,语法：lambda 参数：返回值
#a=lambda n:n*n
#print(a(7))

#print(fun.__name__)  #查函数的名字
#print(a.__name__)    #__name__的值都是<lambda>
#fn=fun
#gn=fn
#print(gn.__name__)

a=lambda x,y:x,11
a=1,2
print(id(a))