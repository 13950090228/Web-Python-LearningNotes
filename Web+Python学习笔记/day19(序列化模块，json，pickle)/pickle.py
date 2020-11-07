import pickle
#支持在python中几乎所有的数据类型

#pickle的使用特点
#dump 序列化的结果只能是字节
#只能在python使用
#在和文件操作的时候，需要用 wb，rb的模式打开文件
#可以多次dump和 多次load

dic={(1,2,3):{'a',2},1:'asb'}
dic1={(1,2,3):{'a',2},2:'asb'}
dic2={(1,2,3):{'a',2},3:'asb'}
dic3={(1,2,3):{'a',2},4:'asb'}
dic4={(1,2,3):{'a',2},5:'asb'}
ret=pickle.dumps(dic)

with open('pickle_file','wb') as f:
    pickle.dump(dic,f)
    pickle.dump(dic1,f)
    pickle.dump(dic2,f)
    pickle.dump(dic3,f)
    pickle.dump(dic4,f)
    
f.close()

with open('pickle_file','rb') as f:

    while True:
        try:
            print(pickle.load(f))
        except EOFError:
            break
        
f.close()