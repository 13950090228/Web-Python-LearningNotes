#read(1) 读取一个字符
#seek(3) #3byte >= 1个中文，移动的单位是byte，如果是utf-8的中文部分，是三的倍数
#seek(0,0) seek的第二个参数表示的是从哪个位置进行偏移
#默认是0，表示开头。1表示当前，2表示结尾
#seek(0,0)
#f=open('鸡巴给你含.txt',mode='r', encoding='utf-8')
#f.seek(16) #3byte >= 1个中文，移动的单位是byte，如果是utf-8的中文部分，是三的倍数
##f.seek(3,1)
#s=f.read()
##print(f.tell())  #查询光标当前所在位置
#print(s)
#f.close()

#f=open('鸡巴给你含.txt',mode='w+', encoding='utf-8')
#f.write('温柔台湾人有我也问 4以为英文')
#f.seek(6)
#f.seek(3.1)
#f.seek(0)
#s=f.read()
#print(s)
##print(s)
#print(f.tell())
##截断，从光标位置开始删除到结尾
##f.truncate()    #如果给参数，就是从头截断到当前位置
#import os
#import time
#with open('鸡巴给你含.txt',mode='r',encoding='utf-8') as f, \
#    open('鸡巴给你含_副本.txt',mode='w',encoding='utf-8') as f2:
#        for line in f:
#            line=line.replace('刘永祺','sb')
#            f2.write(line)
#time.sleep(3)
#os.remove('鸡巴给你含.txt')
#time.sleep(3)
#os.rename('鸡巴给你含_副本.txt','鸡巴给你含.txt')   









