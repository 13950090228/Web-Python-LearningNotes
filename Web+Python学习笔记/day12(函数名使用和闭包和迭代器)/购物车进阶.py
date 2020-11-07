goods=[
       {'name':'电脑','price':5000},
       {'name':'手机','price':3000},
       {'name':'平板','price':4000},
       {'name':'零食','price':50},
       {'name':'床上用品','price':250},
       {'name':'避孕套','price':60}
      ]
a,b,c,d=0,0,0,0
shoppingcar={
        '电脑':[1999,a,b,0,0],
        '鼠标':[10,c,d],
        '美女':[50,]
        }
for i in range(len(shoppingcar)):
    print(i+1,goods[i])
num=int(input('请选择你想买的商品序号：'))

#def login():
#    username=input('输入账号：')
#    password=input('输入密码：')
#while 1:
#    s=input('请输入你要执行的操作：登陆，注册，购物，退出：')
#    if s=='登陆':
#        login()
#    elif s=='注册':
#        pass
#    elif s=='购物':
#        pass
#    elif s=='退出':
#        break
#    else:
#        print('请重新输入：')
    




