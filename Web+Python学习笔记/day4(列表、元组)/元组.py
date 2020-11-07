#元组第一层不能变，内部元素无要求
lst=(0,1,3,8,1,6,'sadf',98,1,['wergt','wef',['ewt']])
#print(lst.index(6))   #返回框中元素在列表中的索引
#range(m,n,q)m->n-1 每q个取一个
lst=["黄渤","邓超","白客","孙俪","奥尔夫","阿道夫"]
for i in range(len(lst)):
    print(i,end=' ')
    print(lst[i])
