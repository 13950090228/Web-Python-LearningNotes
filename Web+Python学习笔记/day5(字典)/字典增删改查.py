#字典键只能放可哈希（不可变的）
dic={'卡尔萨斯':'死歌','盖伦':'大宝剑','诺手':'德莱厄斯','亚索':'风男'}
#dic['诺手']='人头狗'    #新增和修改，强制修改
#dic.setdefault('盖伦','大宝') #如果键字典里存在就不做操作，setdefault(键,值)
#dic.setdefault('火女','火男')
#ret=dic.pop('盖伦')  #通过key删除,可返回被删除的值
#del dic['诺手']
#dic.clear() #全部删除
#ret=dic.popitem();print(ret) #删除最后一个，返回一个元组
#dic1={'暗夜猎手':'薇恩','火女':'安妮','盖伦':'大宝'} #如果原字典有
#dic.update(dic1) #被更新的键，值会被覆盖
#for i in dic:
#    print(i) #for默认获取字典中的键
#print( dic['盖伦'] ) #查看1 找不到会报错
#print(dic.get('盖伦','找不到你傻逼'))  #查看2 找不到则返回None 可以指定返回内容
#print(dic.setdefault('盖','大宝剑'))  #查看3 如果键在字典中存在就不做任何添加否则添加,找不到key则返回None
#print( dic.keys() ) #显示所有键，高仿列表
#print( dic.values() ) #显示所有值，高仿列表
#print( dic.items() ) #显示键值对，高仿列表，键值对是元组
#print(dic)
#for i in dic.keys(): #返回键值对是元组
#    print(i)
#a,b,c=(1,2,3)  #将后边解构打开按位置复制给变量.支持字符串，列表，元组
#for a,b in dic.items():
#   print(a);print(b)
dic1={'name':'汪峰',
      'age':40,
      'wife':
          {'name':'章子怡',
           'age':35,
           'salary':'10000'
           },
       'baby':[
               {'name':'熊大','age':10},
               {'name':'熊二','age':9}
               ]
      }
#print(dic1.get('baby')[0].get('age'))
print(dic1['wife']['age'])






