#生成器的本质就是迭代器，取值方式和迭代器一样(__next__())
#生成器一般由生成器函数或者生成器表达式来创建
#其实就是手写的迭代器
#
#def func():
#    print('哈哈')
#    yield 1   #return和yield都可以返回数据
#    print('呵呵')
#    print('鸡鸡')
#func()  #不会执行你的函数，拿到的是生成器
#gen=func()
#ret=gen.__next__()
#print(ret)
#gen.__next__()
#yield:相当于return 可以返回数据，但是yield不会彻底终端，分段执行函数
#函数中如果有yield，这个函数就是生成器函数，生成器函数（），这个获取的是生成器，这个时候不执行函数
#gen.__next__() #执行函数，执行到下一个yield

#def fun():
#    global ls
#    ls=[]
#    for i in range(10000):
#        ls.append('衣服'+str(i))
#    return ls
##当数据量巨大时，内存可能会被撑爆
#fun()
#print(ls)
#


#def fun():
#    for i in range(10000):  #生成器使用时再取，也有惰性机制
#        yield '衣服'+str(i)
#gen=fun()
#gen.__next__()
#for i in range(10):
#    print(gen.__next__())












