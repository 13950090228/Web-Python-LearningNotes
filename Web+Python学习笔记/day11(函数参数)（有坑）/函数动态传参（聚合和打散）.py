#* 在这里表示接受位置参数的动态传参，接收到的是元组
#顺序: 位置参数 ——> *args——> 默认值参数
#def chi(name,*food,local='北京',**kraw): #参数名是food *表示动态传参
#    print(name+'在'+local+'吃',food)
#    print(kraw)
#chi('刘永祺','馒头','火锅','披萨',yexiao='夜宵',loca='天津')
#
#关键字的动态传参 以字典形式显示
#def chi(*food1,**food): #无敌传参
#    
#    print(food,food1)
#chi('可乐','鸡腿',good_food='狗不理',no_food='汉堡',drink='雪碧')#必须是变量
#
#顺序：位置参数——>*args——>默认值参数——>**kwargs
#1.实参：
#    位置参数
#    关键字参数
#    混合参数(位置，关键字)
#2.形参：
#    位置参数
#    默认值参数
#    动态传参：
#        *args:位置参数动态传参
#        **kwargs：关键字参数动态传参
#
#def fun(a,b):
#    """
#    这个函数是干嘛的
#    """
#    return a+b
#print(fun.__doc__)  #document文档
#
#接受所有参数
#def func(*argc,**kwargs): #无敌 *argc相当于一个聚合的作用
#    print(argc,kwargs)
#func(1,2,3,4,b=7,c=5)
#
#形参：聚合
#def fun(*food):
#    print(food)
#lst=['鸡蛋','沙茶面','主体','鸡巴']
#实参：打散
#fun(lst)
#print(*lst) #打散，把list，tuple，set，str 进行迭代打散
#
#聚合成关键字参数 

def fun(**a):
    print(a)  
    
dic={'name':'刘永祺','age':20}
fun(**dic) #打散成关键字参数
  
#def chi(a,b,c='啊',*argc):
#    return a,b,c,argc
#print(chi(1,2,3,4))







  