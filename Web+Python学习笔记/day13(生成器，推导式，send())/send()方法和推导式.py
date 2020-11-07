#send() 和 __next__()是一样的，可以执行到下一个yield，可以给上一个yield位置传值
#def fun():
#    print('我是第一个段:')
#    a=yield 123
#    print(a)
#    print('我是第二段')
#    b=yield 456
#    print(b)
#    print('我是第三段')
#    c=yield 789  
#    print(c)
#    print('我是第四段')
#    d=yield 10
#    print(d)
#    yield 20#最后收尾一定是yield 不然会报错
#g=fun()
#print(g.__next__())
##print(g.__next__())
##print(g.__next__())
##print(g.__next__())
##print(g.__next__())   #没有上一个yield，所以不能用send(),开头必须是__next__()
#print(g.send('鸡巴'))
#print(g.send('懒趴'))
#print(g.send('啊啊'))
#print(g.send('啊啊'))

#def eat():
#    print('我吃什么啊')
#    a= yield '馒头'
#    print('a=',a)
#    b= yield '肠粉'
#    print('b=',b)
#    c= yield '肉片'
#    print('c=',c)
#    d= yield '结束'
#    print('d=',d)  
#    yield       
#g=eat()
#ret=g.__next__()
#print(ret) 
#ret1=g.send('大懒趴')   #sent可以给上一个yield的位置传递值，不能给最后一个yield发送值
#print(ret1)
#ret2=g.send('中懒趴')
#print(ret2)
#ret3=g.send('小懒趴')
#print(ret3)  
#ret4=g.send('傻逼')
#print(ret4)
#from collections import Iterable
#from collections import Iterator
#
#def fun():
#    yield 1
#    yield 2
#    yield 3
#    yield 4
#    yield 5
#    yield 6
#    yield 7
#    yield 8
#for i in fun():  #for内部一定有__next__()
#    
#    print(i)
#
#print(list(fun()))

#=========================================================
#推导式：用一句话来生成一个列表
#语法：[结果 for循环 判断]
#lst=['python'+str(i) for i in range(16)]
#lst=[i for i in range(1,101) if i%2!=0]
#lst=[i*i for i in range(100) if i%3==0] 

#字典推导式语法:{k:v for循环 条件筛选} 
#lst=[11,22,33,44]
#dic={i:lst[i] for i in range(len(lst)) if lst[i]>22}
##print(dic)
#dic={'jj':'林俊杰','jay':'周杰伦','zs':'赵四','barry':'刘永祺'}
#di={j:i for i,j in dic.items() }
#print(di)
#dic={for i,j in dic.items()}

#d1={}
#for i,j in dic.items():
#    d1[j]=i
#print(d1)

#集合推导式
#lst=[1,2,3,4,7,9,2,1,63,98,4,2,9,5]
#s={i for i in lst}
#print(s)

#没有元组推导式，元组不能增删改
#tu=(i for i in range(10))  #生成器,惰性机制
#print(tu[1])  
#for j in range(10):
#    print(tu.__next__())

#生成器函数      #惰性机制，你不主动拿值它不会给你
#def fun():    #但是你一旦拿了，后面的想拿就拿不到了
#    print('111')
#    yield 222
#
#g=fun()  #获取生成器
#g3=fun()
#g1=(i for i in g)  #生成器
#g2=(i for i in g3) #生成器
#
#print(list(g))  #源头，从源头把数据拿走了
#print('------------------------------')
#print(list(g2)) #这里也没有了
#print('------------------------------')
#print(list(g1)) #这里已经没有值了，被拿走了

#求和
def add(a,b):
    return a+b

#生成器函数  #0-3
def test():
    for j in range(4): 
        yield j
g=test()

#n=2
#g=(add(2,i) for i in g)  #n没有往里带值
##print(list(g))    #这里才会带值
#n=10
#g=(add(n,i) for i in g)
#print(list(g))
for n in [1,10,5]: 
    g=(add(n,i) for i in g)
print(list(g))









