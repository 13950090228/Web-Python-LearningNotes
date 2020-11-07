#count=0
#def fun():
#    global count
#    count=count+1
#    print('大鸡巴',count)
#    fun()
#fun()
#try:
#    fun()
#except:
#    print(count-1)
#递归深度，你可以自己用掉自己的次数
#官方文档中递归最大深度是1000，在这之前就会报错

#遍历文件夹
import os
def fun(filepath,n):
    #1.打开文件夹
    file=os.listdir(filepath)
    #2.遍历文件夹的内容
    for i in file:
        #3.获取文件夹里的路径
        fd=os.path.join(filepath,i)
        #4.判断是不是文件夹
        if os.path.isdir(fd):
            #5.如果是文件夹则再执行一编
            print('\t'*n,i)   #获取路径
            fun(fd,n+1)
        else:
            print('\t'*n,i)
fun('D:\\20170506121 刘永祺\\',0)



#import os
#def fun(filepath,n):
#    file=os.listdir(filepath)
#    for i in file:
#        fd=os.path.join(filepath,i)
#        if os.path.isdir(fd):
#            print('\t'*n,i)
#            fun(fd,n+1)
#        else:
#            print('\t'*n,i)
#fun('D:/老男孩',0)

























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    