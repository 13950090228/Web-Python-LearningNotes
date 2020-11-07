import copy
lst1=["黄渤","邓超","白客","孙俪",['张无忌','赵敏','周芷若']]
lst2=lst1[:] #切片时会产生新的列表（浅拷贝）
lst1=lst2  #内存地址复制
lst2=lst1.copy()  #浅拷贝 只拷贝第一层内容
lst2=copy.deepcopy(lst1) #深度拷贝，但是是一个不一样的对象引入copy deepcopy
lst1.append(123)
print(lst1)
print(lst2)
print(id(lst1))
print(id(lst2))