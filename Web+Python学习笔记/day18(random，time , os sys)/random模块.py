import random as r

#取随机小数：数学计算
#print(random.random()) #取0-1之间的小数
#print(random.uniform(1,10)) #取指定范围之间的小数

#去随机整数
#print(random.randint(1,2)) #[1,2]顾头也顾尾
#print(random.randrange(1,2)) #[1,2)顾头不顾尾
#print(random.randrange(1,200,2)) #取1到200整数，步长为2


#从一个列表中随机抽取值：抽奖
#ls=[1,2,3,4,5,6,7,8,9,10]
#print(random.choice(ls))
#print(random.sample(ls,2)) #在列表里随机抽取n个值（不会重复）  出来一个列表
#打乱一个列表的顺序：洗牌
#random.shuffle(ls)   #打乱原列表，节省空间

#课上练习

#验证码
    #4位数字验证码
#lst=[]
#for i in range(4):
#    lst.append(r.randint(0,9))
#print(lst)
    #6位数字验证码
#lst=[]
#for i in range(6):
#    lst.append(r.randint(0,9))
#print(lst)
    #6位数字+字母验证码
#num=str(r.randint(0,9))
#alpha=chr(r.randint(65,90))
#Alpha=chr(r.randint(97,122))
def fun(n=6,a=True):
    for i in range(n):
        s=''
        num=str(r.randint(0,9))
        if a:
            alpha=chr(r.randint(65,90))
            Alpha=chr(r.randint(97,122))
            num=r.choice([num,alpha,Alpha])
        s+=num
    return s
print(fun())


















#def fun(n=6,aLpha=True):
#    s=''
#    for i in range(n):
#        num=str(r.randint(0,9))
#        if aLpha:
#            alpha=chr(r.randint(65,90))
#            Alpha=chr(r.randint(97,122))
#            num=r.choice([num,alpha,Alpha])
#        s+=num
#    return s
#print(fun())
#发红包 - 作业
    #红包数量 钱数
    #拼手气红包








 
