#2.写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为
#新列表返回给调用者
#第一种方法:
#def jiancha(lst):
#    ls=[]
#    for i in range(len(lst)):
#        if i%2==1:
#            ls.append(lst[i])
#    return ls
#ret=jiancha(lst=[0,1,2,3,4,5,6,7,8,9])
#print(ret)
#第二种方法:
#def jiancha(lst):
#    return lst[1::2]
#print(jiancha(lst=[0,1,2,3,4,5,6,7,8,9]))

#3. 写函数，判断用户传入的对象(字符串、列表、元组)长度是否大于5
#def panduan(ls):
#    if len(ls) <=5:
#        print('长度没有大于5')
#    else:
#        print('长度大于5')
#最简单的方法
#    return len(ls) > 5
#print(panduan(ls=(1,2,3,4,5,8)))

#4.写函数，检查传入列表的长度，如果大于2，将列表的前两项内容返回给调用者
#def panduan(ls):
#    lst=[]
#    if len(ls)>2:
#        for i in range(2):
#            lst.append(ls[i])
#    else:
#        for i in ls:
#            lst.append(i)
#    return lst
#print(panduan(ls=[1]))

#5.写函数，计算传入函数字符串中数字，字母，空格，以及其他内容的个数，并返回结果
#def count(a):
#    shuzi=0
#    zimu=0
#    kongge=0
#    qita=0
#    for i in a:
#        if i.isdigit(): #isdigit()判断字符串是否为数字  
#            shuzi+=1
#        elif i.isalpha(): #isalpha() 判断字符串是否为字母
#            zimu+=1
#        elif i==' ':
#            kongge+=1
#        else:
#            qita+=1
#    return shuzi,zimu,kongge,qita
#print(count('sdhkjfgbkweb g weio gwe 55%'))

#6.写函数，接受两个数字参数，返回比较大的那个数字
#def func(a,b):
#    if a>b:
#        print(a)
#    elif a<b:
#        print(b)
#    else:
#        print(none)    
#func(5,6)
#a=10;b=20
#c=a if a>b else b
#print(c)

#7.写函数，检查传入字典的每一个value的长度，如果大于2，那么仅保留前两个长度
#的内容，并将新内容返回给调用者
#def zidian(dic):
#    new={}
#    for i,j in dic.items():
#        if len(j) >2:
#            s=j[0:2]
#            new[i]=s
#        else:
#            new[i]=j
#    return new
#print(zidian(dic={'das':'gfeg','dsgsg':'548487','asf':'12'}))
  
#8.写函数，此函数只接受以一个参数且此参数必须是列表数据类型，此函数完成的
#功能是返回给调用者一个字典，此字典的键值对位此列表的索引以及对应的元素。
#例如传入的列表为[11,22,33] 返回字典为 {0:11,1:22,2:33}      

#def zidian(a):
#    dic={}
#    if type(a)==list:  #判断是不是列表
#        for i in range(len(a)):
#            dic[i]=a[i]
#        return dic
#    else:
#        return '你传入的不是列表'
#print(zidian(a=(11,22,33)))
        
#9.写函数，函数接受四个参数分别是:姓名，性别，年龄，学历。用户通过输入这
#四个内容，然后将四个内容传入到函数中，此函数接收到这四个内容，将内容追加到一个
#student.msg文件中    
#def msg(name,sex,age,grade):
#    with open('student.msg',mode='a',encoding='utf-8') as f:
#        f.write(name +',')
#        f.write(sex +',')
#        f.write(str(age) + ',')
#        f.write(grade + '\n')
#
#msg('鸡巴','男',22,'博士')
#msg('懒趴','男',23,'硕士')

#10.对第9题升级:支持用户持续输入，Q或者q退出，
#性别默认为男，如果遇到女学生，则把性别输入女
#def msg(name,age,grade,sex='男'):
#    with open('student.msg',mode='a',encoding='utf-8') as f:
#        f.write(name +',')
#        f.write(sex +',')
#        f.write(str(age) + ',')
#        f.write(grade + '\n')
#
#while(1):
#    content=input('是否继续录入信息？(输入Q退出):')
#    if content.upper()=='Q':
#        break
#    else:
#        name=input('请输入名字：')
#        sex=input('请输入性别：')
#        age=input('请输入年龄：')
#        grade=input('请输入学历：')
#        msg(name,age,grade,sex)
    
    


