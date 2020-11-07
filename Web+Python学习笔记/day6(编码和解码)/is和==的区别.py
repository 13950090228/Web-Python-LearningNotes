#==比较的是两边的值
#a='alex'
#b='alex'
#print(a == b)
#print(id(a),id(b))

# is比较的是内存地址
#a='alex'
#b='alex'
#n=10
#m=10
#print(id(n))  #显示内存地址
#print(n==m) #True
#print(n is m)#True

#li=[1,2,3]
#lis=[1,2,3]
#print(li is lis) #False

#tu=(1,2,3)
#tu1=(1,2,3)
#print(tu is tu1) #True

#dic={'name':'alex'}
#dic1={'name':'alex'}
#print(dic is dic1)   #False

#小数据池
    #数字小数据池-5~256
    #字符串中如果有特殊字符那他们的内存地址就不一样
    #字符串单个*20以内他们的内存地址一样
#a='alex@'
#a1='alex@'
#print(a is a1)
a=-25555
b=-25555
print(a == b)
















