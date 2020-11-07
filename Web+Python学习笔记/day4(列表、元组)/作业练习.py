#第一部分
#li=["alex","WuSir","ritian","barry","wenzhou"]
#l2=[1,"a",3,4,"heart"]
#1.计算长度并输出
#print(len(li))
#2.列表中追加元素"seven"，并输出添加后的列表
#li.append("seven")
#print(li)
#3.请在列表的第一个位置插入元素"Tony"
#li.insert(1,"Tony")
#print(li)
#4.请修改列表第2个位置的元素为"Kelly"
#li[2]="Kelly"
#5.请将列表l2的每一个元素添加到列表li
#li.extend(l2)
#6.请将字符串s="qwert"的每一个元素添加倒列表li中，一行代码实现，不允许循环添加
#s="qwert"
#li.extend(s)
#7.请删除列表中的"eric"元素
#li.remove("eric")
#8.请删除列表中的第二个元素
#li.pop(2)
#print(li.pop(2))
#9.请删除列表中的第2个至第4个元素
#del li[2:4]
#10.请将列表中所有元素翻转
#li.sort(reverse=True)
#11.请计算出"alex"元素在列表li中出现的次数
#print(li.count("alex"))
#
#第二部分
#li=[1,3,2,"a",4,"b",5,"c"]
#1.通过切片形成新的列表l1=[1,3,2]
#print(li[0:3])
#2.通过切片形成新的列表l2=["a",4,"b"]
#print(li[3:6])
#3.通过切片形成新的列表l3=[1,2,4,5]
#print(li[0::2])
#4.通过切片形成新的列表l4=[3,"a","b"]
#print(li[1:6:2])
#5.通过切片形成新的列表l5=["c"]
#print(li[7::])
#6.通过切片形成新的列表l6=["b","a",3]
#print(li[-3:-8:-2])
#
#
#第三部分
#lis=[2,3,"k",["qwe",20,["k1",["tt",3,"1"]],89],"ab","abv"]
#1.将tt变成大写(两种方法)
#lis[3][2][1][0]="TT"
#print(lis)
#print(lis[3][2][1][0].upper())
#2.将列表中的数字3变成字符串"100"(两种方法)
#lis[1]="100";lis[3][2][1][1]="100"
#str(lis[3][2][1][1]+97)
#3.将列表中的字符串"1"变成数字101
#lis[3][2][1][2]=101
#int(lis[3][2][1][2])+100)
#第四部分
#li=["alex","eric","rain"]
#li1=li[0]+"_"+li[1]+"_"+li[2]
#print(li1)
#
#第五部分
#用for循环和range打印出下列列表
#li=["alex","WuSir","ritian","barry","wenzhou"]
#for i in li:
#    print(i)
#    
#for i in range(len(li)):
#    print(li[i])
#
#第六部分
#用for循环和range找出100以内所有的偶数并插入到新的列表
#li=[]
#for i in range(101):
#    if i%2==0:
#        li.append(i)
#print(li)
#
#第七部分
#利用for和range找出50以内能被3整除的数,并将这些数插入到新列表中
#li=[]
#for i in range(50):
#    if i%3==0:
#        li.append(i)
#print(li)
#
#第八部分
#for循环和range从100~1,倒序打印
#for i in range(100,-1,-1):
#    print(i)
#count=100
#while count>0:
#    print(count)
#    count-=1
#第九部分
#for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，
#然后对列表的元素进行筛选，将能被4整除的数留下来
#li=[]
#for i in range(100,9,-1):
#    if i %4==0:
#        li.append(i)
#print(li)
#
#第十部分
#用for循环和range循环，将1-30的数字一次添加到一个列表中，
#并循环这个列表，将能被3整除的数换成*
#li=[]
#for i in range(1,31):
#    li.append(i)
#for j in range(len(li)):
#    if li[j] % 3 ==0:
#        li[j]="*"
#print(li)
#
#第十一部分
#查找列表li中的元素，移除每个元素的空格，并找出以"A"开头或者"a"，并以"c"结尾的所有
#元素，并添加到一个新的列表最后循环打印出
#li=["TaiBai","ale xC","AbC ","egon","ri TiAn","WuSir"," apc"]
#la=[]
#for i in range(len(li)):
#    li[i]=li[i].replace(' ','')
#    if li[i][1]=="A"or"a" and li[i][-1]=="c":
#        la.append(li[i])
#print(la)
#第十二部分
#li=['苍井空','加藤鹰','波多野结衣','小泽玛利亚']
#a=input("请输入内容:")
#a1=[]
#for i in li:
#    if i in a:
#        a=a.replace(i,'*'*len(i))
#a1.append(a)
#print(a1) 
    
#第十三部分
#li=[1,3,4,"alex",[3,7,"TaiBai"],5,"RiTiAn"]
##循环打印列表每个元素 与到列表则再打印出里面的元素
#for i in li:
#    if type(i)==list:
#        for e in i:
#            if type(e)==str:
#                print(e.lower())
#            else:
#                print(e)
#    else:
#        if type(i)==str:
#            print(i.lower())
#        else:
#            print(i)

#第十四部分
#把班级学生数学考试成绩录入到一个列表中，并求平均值。要求录入的时候
#要带着任命录入，例如张三_44
#a=[]
#sum1=0
#while(1):
#    name=input("请输入名字(输入Q或者q时退出程序):");
#    if name.lower()=="q":
#        
#        break
#    else:
#        score=input("请输入分数:")
#        sum1=sum1+int(score)
#        a.append(name+"_"+score)
#print(a)
#print("平均分为：%d" %(sum1/len(a)))
#
#第十五部分
#敲7游戏，碰到7或者7的倍数,则更换成*
#a=[]
#for i in range(50):
#    if i%7==0 or '7' in str(i):
#        i='*'
#    a.append(i)
#print(a)
#
#第十六部分
#(升级题) 编写程序. 完成心动女生的筛选. (升级题)
#首先. 程序会提示用户录入10位心仪女生的姓名. 然后把10位女生的名
#字和序号展示出来. 由用户选择心动女生. 此时用户可以选择3个心动女生. 把用
#户选中的三个心动女生的名字打印出来. 供用户继续选择. 这次选择. 只能选
#择一名女生. 然后输出用户的心动女生是xxx
print("请输入10名心动女生:")
a=[]
for i in range(10):
    e=input("输入你心动女生的名字：")
    b=i+1
    a.append(str(b)+"_"+e)
print(a)      
#请用户输入3名心动女生的序号
n=[]
for j in range(3):
    name=input("请输入你心动女生的序号(输入三次)：")
    n.append(a[int(name)-1])
print(n)

k=input("我选择的心动女生是:")
print(a[int(k)-1])
#    
#
#
#
#
