#文件路径
#   1.绝对路径，从磁盘根目录寻找 或 从互联网寻找
#   2.相对路径，相对于文件所在的文件夹  ../返回上级目录
#常用操作 r ,w ,a ,r+ ,w+ ,a+ ,rb ,wb ab
# seek() #移动光标
## 
#f=open('幼齿.txt', mode='a',encoding='utf-8')
#f.write('bvbbbbbbbbbbbbbbbbbb')
#f.close()
#print(s)

#f=open('幼齿.txt', mode='r',encoding='utf-8')
##s=f.readline().strip() #一次读一行，strip去末尾空格符
#for i in f: #文件是一个可迭代对象
#    print(i.strip())
#f.close()

#带 W 的，只要你操作了，都会清空源文件
# a模式 的是追加模式，换行需要手动换行
#如果文件不存在会自动创建文件
#f=open('鸡巴给你含.txt',mode='a',encoding='utf-8')
#f.write('\n大鸡巴给你含')
#f.flush()
#f.close()

#rb,wb,ab,bytes如果处理的是非文本文件
#图片从另一个路径复制到另一个路径，先读取后写入
#f=open('../a.png',mode='rb')  #非文本不能用encoding,需要复制的文件路径
#e=open('abc.png',mode='wb')   #要复制到的路径和图片命名
#for i in f:
#    e.write(i)
#f.flush()
#f.close()
#e.close()

#不论你读取了多少内容，光标在哪里，写入的时候都是在结尾写入
#最好用的读写同时存在模式 r+,但是有坑 ↑
# r+ 读写模式 先读后写

#f=open('鸡巴给你含.txt',mode='r+',encoding='utf-8')
#s=f.read()
#f.write('123456')
#
#print(s)
#f.close()

# w+ 写读模式 先写后读(少用，会清空文件内容)
#f=open('鸡巴给你含.txt',mode='w+',encoding='utf-8')
#f.write('123456') #写完后光标在最后，读取无内容
#f.seek(0) #移动光标
#s=f.read()
#print(s)
#f.flush()
#f.close()

# a+
#f=open('鸡巴给你含.txt',mode='a+',encoding='utf-8')
#f.seek(0)
#f.write('啊啊啊啊')
#f.seek(0)
#s=f.read()
#print(s)
#f.close()



