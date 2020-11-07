#2.写函数，接收n个数字，求这些参数数字的和（动态传参）
#def fun(*args):
#    sum1=0
#    for i in args:
#        sum1=sum1+i
#    print(sum1)
#fun(1,2,3)
#第二种方法
#def func(*args):
#    return sum(args)
#print(func(1,2,3,4,5,6))
#3.读代码，回答：代码中，打印出来的值a，b，c分别是什么
#a=10
#b=20
#def test(a,b):
#    print(a,b)
#c=test(20,10)
#print(c)
#a=20,b=10,因为没有return，所以c=None

#4.读代码，回答：代码中打印出来的值a，b，c分别是什么？
#a=10
#b=20
#def test(a,b):
#    a=3
#    b=5
#print(a,b) #a=10,b=20
#c=test(a,b) 
#print(c)   #None
#print(a,b) #a=10,b=20

#5.写函数，传入函数中多个实参(均为可迭代对象如字符串，列表，元组，集合等)，将
#每个实参的每个元素依次添加到函数的动态参数args里面。
#例如传入函数两个参数[1,2,3](22,33)最终为args为(1,2,3,22,33)
#def fun(*args):
#    print(args)
#fun(*[1,2,3,4,5,6],*(7,8,9),*'鸡巴',*{'啊','和'},*{'name':123})

#6.写函数，传入函数中多个实参(实参均为字典)，将每个实参的键值对依次添加到函数
#的动态参数kwargs
#    例如传入函数两个参数{'name':'alex'} {'age':'100'}最终kwargs为
#{'name':'alex','age':'100'}
#def fun(**kwarg):
#    print(kwarg)
#fun(**{'name':'alex'},**{'age':'100'})

#7.下面代码成立么？如果不成立为什么报错？怎么解决？
#7.1
#a=2
#def wrapper():
#    print(a)
#wrapper()
#成立，输出a
    
#7.2
#a=2
#def wrapper():
#    a+=1
#    print(a)
#成立，但是没有调用不输出内容        
#7.3
#def wrapper():
#    a=1
#    def inner():
#        print(a)
#    inner()
#wrapper()
#成立输出1   
#7.4
#def wrapper():
#    a=1
#    print(a)
#    def inner():
#        nonlocal a
#        a=a+1
#        print(a)
#    inner()
#wrapper()
#报错，需要加个global或者nonlocal

#8.写函数,接收两个数字参数，将较小的数字返回
#def sum1(*args):
#    print(min(args))
#sum1(2,3,4,5,6,1)

#9.写函数，接收一个参数（此参数类型必须是可迭代对象），将可迭代对象的每个元素
#以'_'相连接，形成新的字符串，并返回
#    例如传入的可迭代对象为[1,'老男孩','武sir']返回的结果为'1_老男孩_武sir'
  
#def fun(a):
#    st=''
#    for i in a:
#        st=st+str(i)+'_'
#    return st
#print(fun(a=[1,'老男孩','武sir']))   
#10.写函数，传入n个数，返回字典{'max':'最大值','min':'最小值'}
#例如:min_max(2,5,7,8,4) 返回:{'max':8,'min':2}(此题用到max()和min()内置函数)
#def fun(*args):
#    dic={}
#    dic['max']=max(args)
#    dic['min']=min(args)
#    print(dic)
#fun(8,656,7,2,6,9,5,6,72,2,8)

#def fun(*a):
#    print({'max':max(a),'min':min(a)})
#fun(1,5,4,89,2,2,8,8,6,98,2,7)
    
#11.写函数，传入一个参数n，返回n的阶乘
#def fun(a):
#    sum1=1
#    for i in range(1,a+1):
#        sum1=sum1*i
#    print(sum1)
#fun(5)

#12.写函数,返回一个扑克牌列表，里面有52项，每一项是一个元组
#例如：[('红心',2),('草花',2)....('黑桃','A')]
#def fun():
#    ls=[]
#    ls1=['红心','草花','黑桃','方块']
#    ls2=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
#    for i in ls1:
#        for j in ls2:
#            ls.append((i,j))
#    
#    print(ls)
#fun()

#13.有如下函数
#def wrapper():
#    def inner():
#        print(666)
#    inner()
##    return inner()
#wrapper()
##
#任意添加代码，用两种或以上方式执行inner函数

#14相关面试题(在纸上写好答案，然后再运行)
#(1).有函数定义如下:
#def cale(a,b,c,d=1,e=2):
#    return(a+b)*(c-d)+e
#请分别写出下列标号代码的输出结果，如果出错写出Error。
#print(cale(1,2,3,4,5)) #1
#print(cale(1,2))       #Error
#print(cale(e=4,c=5,a=2,b=3)) #28
#print(cale(1,2,3))     #8
#print(cale(1,2,3,e=4)) #10
#print(cale(1,2,3,d=5,4)) #Error

#(2).(此题有坑)下面代码打印的结果分别是  10 ，123  ， 'a'  。
#def exten(val,list=[]): #默认值如果是可变的数据类型，每次使用都是同一个
#    print(id(list))     
#    list.append(val)
#    return list
#
#list1=exten(10)  
#list2=exten(123,[])
#list3=exten('a')
#
#print('list1=%s' %list1)
#print('list2=%s' %list2)
#print('list3=%s' %list3)
        
#15.写代码完成99乘法表 
#def fun():
##    ls=[1,2,3,4,5,6,7,8,9]
#    for i in range(1,10):
#        print('\n')
#        for j in range(1,10):
#            ls1=i*j
#            print('%d * %d = %d'%(i,j,ls1))
#fun()   
#    

#16.写一个函数，完成三次登录功能，在额一个函数完成注册功能（升级题）
#注册：
#    首先，要从文件中读取用户名和密码，匹配用户输入的用户名和文件
#中的用户名是否一致，如果一直请重新输入。
#    其次，如果上面的判断没有问题，把用户名和密码写入文件中
#def regist():
#    print('欢迎进入注册系统')
#    name=input('请输入用户名:')
#    password=input('请输入密码:')
#    for i in range(len(name)):
#        if name[i] == ' ':
#            print('你的用户名不合法，不能存在空格')
#            return 
#        #校验用户名是否存在
#    f=open('注册系统.txt',mode='r+',encoding='utf-8')
#    for line in f:
#        if name==line.split('@')[0]:
#            print('对不起该用户已存在，请重新注册')
#            break
#    else:
#        f.write('\n'+name+'@'+password)
#        print('注册成功')
#
#    return 
#    f.close()
#regist()  
    
    
