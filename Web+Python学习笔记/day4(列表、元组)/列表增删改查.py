lst=["黄渤","邓超","白客","孙俪","奥尔夫","阿道夫"]
#lst.append('王力宏')
#lst.insert(2,'刘永祺')
#lst.extend(['刘永祺','马云','王健林'])  #会把里面的元素分解,并添加
#lst.pop(4)   #可以返回被删除数
#lst.remove('白客')
#del lst[0:5] 
#lst.clear()#全部删除
#lst[4]="吃鸡吧"
#lst[1:4]='鸡巴给你含'#将元素拆解开来迭代添加
#lst[1:3]=["吃鸡巴"]#先删除后添加
lst[1::]=["麻花疼","鸡巴","地干"]
#for i in lst:
#    print(i)
print(lst)