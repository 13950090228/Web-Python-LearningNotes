'''
1.让用户输入金额
2.选择要购买的商品加入购物车
3.当商品的总结超过了你的金额，提示余额不足
4.让用户输入N结算，输入Q退出
'''


goods=[
       {'name':'电脑','price':5000},
       {'name':'手机','price':3000},
       {'name':'平板','price':4000},
       {'name':'零食','price':50},
       {'name':'床上用品','price':250},
       {'name':'避孕套','price':60}
      ]
money=input('请输入您的预算金额(只能输入纯数字):')
lst=[]       #显示商品列表
shop_car={}  #购物车
count=0      #计算购物车商品数量
if money.isdigit():
    for i in range(len(goods)):
        print(f"序号:{i+1}  商品:{goods[i]['name']}  单价:{goods[i]['price']}")
else:
    print('输入错误！')
while 1:
    choose=input('请输入你要添加的商品序号(Q退出，N查看购物车，x结算):')
    if choose.isdigit() and 0<int(choose)<=len(goods):
        index=int(choose)-1
        if shop_car.get(index) == None:
            shop_car[index]=1
        else:
            shop_car[index]=shop_car[index]+1
    elif choose.upper() =='Q':
        break
    elif choose.upper() == 'N':
        for n,m in shop_car.items():
            print(f"序号:{n+1} 商品:{goods[n]['name']} 数量:{m}")
    elif choose.upper() == 'X':
        for j in shop_car:
            count=count+int(goods[j]['price'])*int(shop_car[j])
        print(f'您的商品总价为：{count}元。')
    else:
        print('输入错误请重新输入！')













#shop_car={} #键 ==列表的索引  值 ==商品的数量
#money=input('请输入您的预算金额：')
#count=0
##判断是不是都由数字组成（判断是否都是数字）
#if money.isdigit():  
#    while 1:
#        #==========展示商品=========
#        print('======================================')
#        for i in range(len(goods)):
#            print(i+1,goods[i]['name'],goods[i]['price'])
#        print('======================================')
#        choose=input('请输入您要购买的商品序号(N结算,Q退出,X查看当前购物车)：')
#        #判断用户输入的是不是在正常范围内
#        if (choose.isdigit()) and (0<int(choose)<=len(goods)):
#            int_index=int(choose)-1
#             #=======让用户把商品加入到购物车中=======
#            if shop_car.get(int_index)==None:
#                shop_car[int_index]=1
#            else:
#                shop_car[int_index]=shop_car[int_index]+1
#        #查看购物车
#        elif choose.upper()=='X':
#            for j in shop_car:
#                print(f'您的购物车中商品:{goods[j]["name"]},单价:{goods[j]["price"]},数量:{shop_car[j]}')
#        elif choose.upper()=='N':
#            #结算
#            #... == pass
#            #1.2 - 1.0 == 0.2 获取到的是False
#            for k in shop_car:
#                count=count + shop_car[k]*goods[k]['price']
#            print('您消费一共%d元\n' %count)
#            if int(money)<count:
#                print('您的余额不足：')
##                for n,m in enumerate(shop_car,1):
##                    print(f'{n} {goods[m]["name"]} {shop_car[m]}')
##                shop_del=int(input('您的金额不够支付！,请删除商品对应的序号。'))
##                shop_car[shop_del-1]=shop_car[shop_del-1]-1                                
#        elif choose.upper()=='Q':
#            #退出
#            break
#        else:
#            print('输入有误请重新输入：\n')
#else:
#    print('请正确输入金额！')

#car=[1,2,3,4,5,6]
#for i,j in enumerate(car,100):   #枚举
#    print(i,j)










