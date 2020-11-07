#print(dir(str)) #dir查看xx类型的数据可以执行哪些方法,__iter__
#print(dir(int))  #没有__iter__
#print(dir(list)) 
#print(dir(tuple))
#print(dir(set))
#print(dir(dict))
#所有的带__iter__可以使用for循环的，可迭代对象
#可迭代对象可以使用__iter__()来获取到迭代器
#迭代器里面有__next__()

#1.不能反复，迭代器只能向前
#2.几乎不占用内存，节省内存（需要明天的生成器）
#3.for循环
#4.惰性机制（面试题,难度较高）

#s='刘永祺大鸡巴'
#it=s.__iter__()
#print(dir(it))
#print(it.__next__()) #__next__()根据索引一个一个推
#print(it.__next__())
#print(it.__next__())
#print(it.__next__())
#print(it.__next__())
#print(it.__next__())

#lt=['鸡巴','懒趴','刘永祺','啊啊啊']
#it=lt.__iter__()  #获取迭代器
#while 1:
#    try:
#        el=it.__next__() #获取下一个元素
#    #    it.__next__()
#    #    it.__next__()
#    #    it.__next__()
#        print(el)
#    except:      #处理错误
#        break
#ls=lt.__iter__()
#print('__iter__'in dir(ls))
#通过dir来判断数据是否可是迭代的，以及数据是否是迭代器

#迭代器一定可迭代
#from collections import Iterable
#from collections import Iterator
#print(isinstance(lt,Iterable)) #Iterable判断是不是可迭代对象
#print(isinstance(lt,Iterator)) #Iterator判断是不是迭代器
#
#lt=['鸡巴','懒趴','刘永祺','啊啊啊']
#ls=lt.__iter__()
#while 1:
#    try:
#        print(ls.__next__())
#    except:
#        break
#
#print(s) #在list中，一定存在for，一定__next__()
#print(isinstance(s,Iterable))
#print(isinstance(s.Iterator))







