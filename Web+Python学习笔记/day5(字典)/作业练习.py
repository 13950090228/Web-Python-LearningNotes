#1.有如下变量tu(是个元组),请实现要求功能
tu=("alex",[11,22,{'k1':'v1','k2':['age','name'],'k3':(11,23,33)},44])
#a.讲述元组特性
#:不可更改，只读列表
#b."alex"能否被修改
#:不可以
#c. 请问tu变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 "Seven"
#:可以修改
#tu[1][2]['k2'].append('seven')
#d.请问tu变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 "Seven"
#是一个键，不能修改
#2.
dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
#a.请循环输出所有的key
#for i in dic.keys():
#    print(i)
#b.请循环输出所有的value
#for i in dic.values():
#    print(i)
#c.请循环输出所有的key和value
#for a,b in dic.items():
#    print(a)
#    print(b)
#d.请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
#dic['k4']='v4'
#print(dic)
#e.请在修改字典中"k1"对应的值为"alex"，输出修改后的字典 
#dic['k1']='alex'
#print(dic)
#f.请在k3对应的值中追加一个元素44，输出修改后的字典
#dic['k3'].append(44)
#print(dic)
#g.请在k3对应的值的第1个位置插入个元素18，输出修改后的字典
#dic['k3'].insert(0,18)
#print(dic)
#3.
#av_catalog = {
#    "欧美":{
#        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
#        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
#        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
#        "x-art.com":["质量很高,真的很高","全部收费,屌丝请绕过"]
#    },
#    "日韩":{
#        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]
#    },
#    "大陆":{
#        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
#    }
#}
# a,给此 ["很多免费的,世界最大的","质量一般"]列表第二个位置插入一个元素：'量很大'。
#av_catalog['欧美']['www.youporn.com'].insert(1,'量很大')  
    
# b,将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过" 删除。
#av_catalog['欧美']['x-art.com'].pop(1)
    
# c,在此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表中添加"金老板最喜欢这个"。
#av_catalog['欧美']['x-art.com'].append('金老板最喜欢这个')
 
# d,将此["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]列表的 "verygood"全部变成大写
#av_catalog['日韩']["tokyo-hot"][1]=av_catalog['日韩']["tokyo-hot"][1].upper()

# e,给'大陆' 对应的字典添加一个键值对 '1048' :['一天就封了']
#av_catalog['大陆'].setdefault('1048',['一天就封了'])
    
# f,删除此"letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"]键值对
#av_catalog['欧美'].pop('letmedothistoyou.com')
    
# g,给此["全部免费,真好,好人一生平安","服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'
#av_catalog['大陆']['1024'][0]=av_catalog['大陆']['1024'][0]+'可以爬下来'

#4.有字符串 "k:1|k1:2|k2:3|k3:4" 处理成字典 {'k':1,'k1':2....}  (升级题)
#s = "k:1|k1:2|k2:3|k3:4"
#dic={}
#count=0
#s1=s.split('|')
#while count<=3:
#    s1[count]=s1[count].split(':')
#    count+=1
#    for i in s1:
#        dic[i[0]]=int(i[1])
#print(dic)

#5.元素分类
#有如下值li= [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，将
#小于 66 的值保存至第二个key的值中。即： {'k1': 大于66的所有值列表, 'k2': 小于66的所有值列表}
#li= [11,22,33,44,55,66,77,88,99,90]
#dic={}
#li1=[]
#li2=[]
#for i in li:
#    if i>66:
#        li1.append(i)
#for j in li:
#    if j<66:
#        li2.append(j)
#dic['k1']=li1
#dic['k2']=li2
#print(dic)
#6.输出商品列表，用户输入序号，显示用户选中的商品(升级题)
# 商品列表：
goods = [{"name": "电脑", "price": 1999},
         {"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 20},
         {"name": "美女", "price": 998}, ]
# 要求:
# 1：页面显示序号 + 商品名称 + 商品价格，如：
#1 电脑 1999
#2 鼠标 10
# a=[]
# count=0
# for i in goods:
#     count=count+1
#     a.append(str(count)+' '+i['name'] +' '+str(i['price']))
# print("商品的列表为：")
# print(a)
# c=len(a)
# while 1:
#     b=input("请输入商品的序号：")
#     if b.upper()=='Q':
#         break
#     elif int(b)>4:
#         print("输入错误:")
#     else:
#         print(a[int(b)-1])
    
dic = {"code":200,"msg":"success","newslist":[
    {"area":"福州","date":"2020-09-22","week":"星期二","weather":"阴转小雨","real":"26°C"},
    {"area": "福州", "date": "2020-09-23", "week": "星期三", "weather": "中雨", "real": "25°C"}
]}

dic2={}

for i in dic["newslist"]:
    dic2[i["date"]] = i["weather"]
    
    
print(dic2);
    






