#lst=[12,5,87,23,679,23,1]
#lst.sort()  #list方法
#print(lst)
#lst=['鸡巴','懒趴','啊啊啊啊','刘永祺','啊啊','第三个','帅逼']
#def func(s):
#    return len(s)%2
#
#print(sorted(lst,key=func))
##key:排序方案，sorted函数内部会把可迭代对象中的每一个元素拿出来后交给后面的key
##后面的key计算出一个数字，作为当前这个元素的权重，曾哥函数根据权重来进行排序
#
#print(sorted(lst,reverse=True))  #内置函数的通用排序方法,默认方法
ls=[4,6,7,2,5,68,3,7,68,32,3]
lst=[{'name':'汪峰','age':48},
     {'name':'章子怡','age':38},
     {'name':'alex','age':39},
     {'name':'wusir','age':32},
     {'name':'刘永祺','age':20}]

#print(sorted(ls))

def fun(lst):
    return lst['age']
print(sorted(lst,key=fun))
#print(sorted(lst,key=lambda a:len(a['name'])%2))