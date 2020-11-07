#1.用推导式做下列小题

#(1) 过滤掉小于3的字符串列表，并将剩下的转换成大写字母
#ls=['sdf','dsfdg','af','edgg']
#lst=[i.upper() for i in ls if len(i)>=3]
#print(lst)

#(2)求(x,y)其中x是0-5之间的偶数，y是0-5之间的奇数组成元组
#ls=[(i,j) for i in range(5) for j in range(5) if i%2==0 and j%2==1 ]
#print(ls)

#(3)求M中3，6，9组成的列表M=[[1,2,3],[4,5,6],[7,8,9]]
#M=[[1,2,3],[4,5,6],[7,8,9]]
#ls=[i[2] for i in M]
#print(ls)

#(4)求出50以内能被3整除的数的平方，并放入到一个列表中
#ls=[i*i for i in range(1,51) if i%3==0]
#print(ls)

#(5)构建一个列表：['python1期','python2期'......,'python3期']
#ls=['python'+str(i)+'期' for i in range(1,11)]
#print(ls)

#(6)构建一个列：[(0,1),(1,2),(2,3),(3,4),(4,5),(5,6)]
#ls=[(i,i+1) for i in range(6)]
#print(ls)

#(7)构建一个列表：[0,2,4,6,8,10,12,14,16,18]
#ls=[i for i in range(1,19) if i%2==0]
#print(ls)

#(8)有一个列表l1=['alex','wusir','老男孩','太白']将其构建成这种列表
#['alex0','wusir1','老男孩2','太白3']
#l1=['alex','wusir','老男孩','太白']
#ls=[l1[i]+str(i) for i in range(4)]
#print(ls)

#(9)有以下数据类型:
x={
   'name':'alex',
   'Value':[{'timestamp':1517991992.94,'value':100},
            {'timestamp':1517992000.94,'value':200},
            {'timestamp':1517992014.94,'value':300},
            {'timestamp':1517992744.94,'value':400},
            {'timestamp':1517992800.94,'value':500}]
   }
#将上面的数据转换为[[1517991992.94,100].........]
lst=[[x['Value'][i]['timestamp'],x['Value'][i]['value']] for i in range(5)]
print(lst)









