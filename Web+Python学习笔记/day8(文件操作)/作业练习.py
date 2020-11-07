#import os
#import time
#with open('懒趴.txt', mode='r',encoding='utf-8') as f1,\
#    open('a2.txt', mode='w',encoding='utf-8')as f2:
#        for i in f1:
#            if i == '慢慢你会发现\n':
#                
#                f2.write('哈哈哈\n')
#                
#            f2.write(i)
#os.remove('懒趴.txt')
#time.sleep(3)
#os.rename('a2.txt','懒趴.txt')

#升级题
#文件a.txt内容为name:apple price:10 amount:3 year:2012
#name:tesla price:10000 amount:1 year:2013
#通过代码，将其构建成这种数据类型:
#[{'name': 'apple', 'price': '10', 'amount': '3', 'year': '2012'},
# {'name': 'tesla', 'price': '10000', 'amount': '1', 'year': '2013'}]
#
ls=[]
with open('a.txt', mode='r', encoding='utf-8') as f1:
    for f in f1:
        dic={}
        f=f.strip().split(' ')
        for i in f:
            i=i.split(':')
            dic[i[0]]=i[1]
        ls.append(dic)
sum1=0
for j in ls:
    sum1=sum1+int(j['price'])*int(j['amount'])
print(ls)  

lst=[]
with open('第六题.txt', mode='r', encoding='utf-8') as f:
    first=f.readline().strip().split('  ')
    for line in f:
        dic={}
        ls=line.strip().split('  ')
        for i in range(len(ls)):
            dic[first[i]]=ls[i]
        lst.append(dic)
print(lst)
##        
#



















