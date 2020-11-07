#列表
#s='*'.join(['高花心','大鸡巴','刘永祺'])
#print(s)
#s=s.split('*')
#print(s)
#.join 将列表转换为字符串，每个字符串之间用'_'连接
#ss='高花心*大鸡巴*刘永祺'
#ss=ss.split('*')  #.split 将字符串转化为列表
#print(ss)
#s='_'.join('麻花疼')
#print(s)
#lst=['鸡巴','懒趴','啊啊','防范',1,2]
#lst1=[] #准备要删除的信息
#for i in lst:
#    lst1.append(i)
##循环新列表，删除老列表
#print(lst1)
#for el in lst1:
#    lst.remove(el)

#lst=['鸡巴','杨超越','啊啊','杨迪','杨紫','杨幂']
#lst1=[]
#for i in lst:
#    lst1.append(i)
#for e in lst1:
#    if e.startswith('杨'): #startswith() 判断元素的开头是不是括号里的内容
#        lst.remove(e)
#print(lst)
#字典
#dic={'卡尔萨斯':'死歌','盖伦':'大宝剑','诺手':'德莱厄斯','亚索':'风男'}
#a=[]
#for i in dic:   #字典在循环的时候不能添加不能删除，不允许改变大小
#    a.append(i)
#for j in a:     #循环a，删除dic
#    dic.pop(j)
#    print(dic)
#print(dic)
#返回新字典，和原来没关系
#s=frozenset(['14','af','ef'])  #frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
#n={s:'123'}
#print(n)
dic1={}
a=['呵呵','啊啊','哈哈']
ret=dic1.fromkeys('or',['1','2','3','4','5','6'])#直接用字典去访问fromkeys不会对字典产成影响
print(ret)
ret=dic1.fromkeys('abc',a)
a.append('嘻嘻')
#直接使用类名进行访问
print(ret)














