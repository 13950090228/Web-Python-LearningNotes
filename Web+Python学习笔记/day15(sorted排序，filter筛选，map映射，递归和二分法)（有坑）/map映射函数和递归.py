lst=[1,4,7,5,8,0,4]
#计算列表中每个数字的平方
def func(i):
    return i**2
#m=map(func,lst)  #把后面的可迭代对象中的每一个元素传递给function，结果就是function的返回值
#print('__iter__' in dir(m))
#for j in m:
#    print(j)

#分而治之    
m=map(func,map(func,map(func,lst)))
#m=map(lambda i:i**2,lst)
#print('__iter__' in dir(m))
for i in m:
    print(i)
#lst2=[1,2,3,4,5,6,7]
##也有水桶效应 zip()
#m=map(lambda x,y:x+y,lst,lst2)
#print(list(m))
