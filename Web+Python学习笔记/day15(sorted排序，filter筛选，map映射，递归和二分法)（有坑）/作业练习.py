#用map来处理下述字符串列表，把列表中所有人都变成sb，比方 alex_sb
#name=['oldboy','alex','wusir']
#第一种方法
#n=map(lambda x:x+'_sb',name)
#第二种方法
#def fun(name):
#    name=name+'_sb'
#    return name
#n=map(fun,name)
#print(list(n))

#用map来处理下述1，然后用list得到一个新的列表，列表中每个人的名字都是sb结尾
#l1=[{'name':'alex'},{'name':'y'}]
#n=map(lambda x:x['name']+'_sb',l1)
#print(list(n))

#用filter来处理，得到股票价格大于20的股票名字
#shares={
#        'IBM':36.6,
#        'Lenovo':23.2,
#        'oldboy':21.2,
#        'ocean':10.2
#        }
#f=filter(lambda x:shares[x]>20,shares)
#print(list(f))

#有下面字典，得到购买每只股票的总价格，并放在一个迭代器中。
#结果：list一下[9110.0,27161.0....]
#por=[
#        {'name':'IBM','shares':100,'price':91.1},
#        {'name':'AAPL','shares':50,'price':543.22},
#        {'name':'FB','shares':200,'price':21.09},
#        {'name':'HPQ','shares':35,'price':31.75},
#        {'name':'YHOO','shares':45,'price':16.35},
#        {'name':'ACME','shares':75,'price':115.65}]

#m=map(lambda x:x['shares']*x['price'],por)
#n=list(m)
##放在迭代器中
#def fun(n):
#    for i in n:
#        yield i
#gen=fun(n)

#用上面的字典，用filter过滤出单价大于100的股票
#f=filter(lambda x:x['price']>100,por)
#print(list(f))


#有下列三种数据类型
#l1=[1,2,3,4,5,6]
#l2=['oldboy','alex','wusir','太白','日天']
#tu=('**','***','****','*******')
##写代码，最终得到的是（每个元组第一个元素>2,第三个*至少是4个。）
##    [(3,'wusir','****'),(4,'太白','*******')]这样的数据
#f=filter(lambda x:x[0]>2 and len(x[2])>=4,zip(l1,l2,tu))
#print(list(f))

#有如下下数据类型：
l1=[
    {'sale':0},
    {'sale':657},
    {'sale':2},
    {'sale':3256},
    {'sale':576},
    {'sale':234},
    {'sale':78},
    {'sale':123},
    {'sale':46},
    {'sale':7},
    ]
#将l1按照列表中的每个字典的value大小进行排序，形成一个新的列表
def fun(l1):
    return l1['sale']
print(sorted(l1,key=fun,reverse=True))









