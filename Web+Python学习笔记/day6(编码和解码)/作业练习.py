#一，老男孩好声音选秀比赛评委在打分的时候呢, 可以进行输入. 假设, 
#老男孩有10个评委.让10个评委进行打分, 要求, 分数必须大于5分, 小于10分.
#count=0
#a=[]
#for i in range(10):
#    count=count+1
#    num=input('请第%d位评委打分(在5和10之间):' %count)
#    if int(num)>10 or int(num)<5:
#        num=input('请重新打分:')
#        continue
#    a.append(num)
#
#print(a)

#二. 电影投票. 程序先给出一个目前正在上映的电影列表. 由用户给每一个电影投票.
#最终 将该用户投票信息公布出来 
#lst = ['金某梅', '解救吾先生', '美国往事', '西西里的美丽传说']
##结果: {'金某梅': 99, '解救吴先生': 80, '美国往事': 6, '西西里的美丽传说':23}
#print("请为'金瓶梅', '解救吾先生', '美国往事', '西西里的美丽传说' 四部电影投票(十次)")
#dic={}
#jin=[]
#jie=[]
#mei=[]
#xi=[]
#j=0
#ji=0
#m=0
#x=0
#for i in range(10):
#    n=input('请输入你要选择的电影(%d):' %(i+1))
#    if str(n)=='金瓶梅':
#        j=j+1
#        dic['金瓶梅']=j
#    elif str(n)=='解救吾先生':
#        ji=ji+1
#        dic['解救吾先生']=ji
#    elif str(n)=='美国往事':
#        m=m+1
#        dic['美国往事']=m
#    elif str(n)=='西西里的美丽传说':
#        x=x+1
#        dic['西西里的美丽传说']=x
#print(dic)
  
#四.车牌区域划分, 现给出以下车牌. 根据车牌的信息, 分析出各省的车牌持有量. (升级题) 
#car = ['鲁A32444','鲁B12333','京B8989M','黑C40678','黑C46555','沪B25041']
#local = {'沪':"上海",'黑':'黑龙江','鲁':'山东','鄂':'湖北','湘':'湖南','京':'北京'}  
#have = {"上海":'','黑龙江':' ','山东':' ','湖北':' ','湖南':' ','北京':' '}
#a=[]
#count=0
#for n in have.keys():
#    have[n]=0
#for i in car:
#    for j in local.keys():
#        if i[0]==j:
#            a.append(local[j])
#for m in a:
#    if m in have:
#        have[m]=a.count(m)
#print(a)
#print(have)

#五.干掉主播. 现有如下主播收益信息, 按照要求, 完成相应操作:
zhubo = {'卢本伟':122000,'冯提莫':189999,'金老板':99999,'吴老板':25000000,'alex':126}
#list(字典)   将字典的键变成列表
##1.计算各位主播收益的平均值.
#num=[]
#a=0
#sum1=0
#for i in zhubo:
#    a=zhubo[i]
#    num.append(a)
#for j in num:
#    sum1=sum1+int(j)
#m=sum1/len(num)
##print(m)
#
##2.干掉收益小于平均值的主播.
#
#for x in list(zhubo):
#    b=zhubo[x]
#    if b<m:
#        del zhubo[x]
#print(zhubo)
##3.干掉卢本伟
#zhubo.pop('卢本伟')
#print(zhubo)