##按照value的值排列
#lst=[{'mm':333},{'mm':222},{'mm':111}]
#print(sorted(lst,key=lambda a:a['mm']))

#匿名函数
    #和生成器一起考
    #和内置函数一起考
    
#递归函数 — 二分查找
    #函数自己调用自己
    #求阶乘/斐波那契数列（请计算第400个数，不超过4000000的最大的值是第几个数）——练习
    #递归函数：能用循环就不要用递归（深度超过10就要慎用了）

#def fun(n):
#    if n==1:
#        return 1
#    else:
#        return fun(n-1)*n
#print(fun(4))    

#
#import time
#start=time.perf_counter()
#def fun(n):
#    if n==1 or n==2:
#        return 1
#    else:
#        return fun(n-2)+fun(n-1)
#print(fun(30))
















#import time
#start=time.perf_counter()
#def func(n):
#    if n==1 or n==2:
#        return 1
#    else:
#        return func(n-1) + func(n-2)
#for i in range(1,30):
#    print(func(i))
#end=time.perf_counter()-start
#print(end)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    