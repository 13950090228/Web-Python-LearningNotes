#os.makedirs('dirname1/dirname2')    #可生成多层递归目录
#os.removedirs('dirname1')    #若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
#os.mkdir('dirname')    #生成单级目录；相当于shell中mkdir dirname
#os.rmdir('dirname')    #删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
#os.listdir('dirname')    #列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
#os.remove()           #删除一个文件
#os.rename("oldname","newname")  #重命名文件/目录
#os.stat('path/filename')  #获取文件/目录信息
#
#os.system("bash command")  #运行shell命令，直接显示
#os.popen("bash command").read()) #运行shell命令，获取执行结果
#os.getcwd()     #获取当前工作目录，即当前python脚本工作的目录路径
#os.chdir("dirname")      #改变当前脚本工作目录；相当于shell下cd
#
#os.path
#os.path.abspath(path) #返回path规范化的绝对路径
#os.path.split(path) #将path分割成目录和文件名二元组返回 
#os.path.dirname(path) #返回path的目录。其实就是os.path.split(path)的第一个元素 
#os.path.basename(path) #返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
#os.path.exists(path)  #如果path存在，返回True；如果path不存在，返回False
#os.path.isabs(path)  #如果path是绝对路径，返回True
#os.path.isfile(path)  #如果path是一个存在的文件，返回True。否则返回False
#os.path.isdir(path)  #如果path是一个存在的目录，则返回True。否则返回False
#os.path.join(path1[, path2[, ...]])  #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
#os.path.getatime(path)  #返回path所指向的文件或者目录的最后访问时间
#os.path.getmtime(path)  #返回path所指向的文件或者目录的最后修改时间
#os.path.getsize(path)   #返回path的大小

import time
import os
##若文件已存在会报错
#os.mkdir('n')
##os.makedirs('2/3/4')

#只能删空文件
#os.rmdir('1')      #删除单个
#os.removedirs('2/3')   #删除多个

#搜索目录下所有文件和文件夹
#lst=os.listdir('D:\老男孩')
##os.path.join  可以自动匹配不同操作系统下合适的路径
#for i in lst:
#    print(os.path.join('D:\老男孩',i))

#获取目标的结构说明
#print(os.stat(r'D:\老男孩\day8(文件操作)'))

#ret=os.popen('dir').read()   #适合做查看类操作
#print(ret)

#不是指当前文件所在目录
#而是指当前文件在哪个目录下执行
#print(os.getcwd())   #当前工作目录

#切换当前工作目录
#os.chdir('D:\老男孩\day18(random，time , os sys)')
##print(os.getcwd())
#print(os.popen('dir').read())

#规范路径，只能给找得到的相对路径改成绝对路径
#print(os.path.abspath('day19(序列化模块，json，pickle)'))

#就是把一个路径分成两段，第二段是一个文件或文件夹
#print(os.path.split('E:/QQ/文档数据/506713537/123.py'))
##只取一个就用下面这两个
print(os.path.basename('E:/QQ/文档数据/506713537/123.py'))
#print(os.path.dirname('E:/QQ/文档数据/506713537/123.py'))

#显示文件最后修改时间
#path=os.path.getatime('E:/QQ/AuI18N/2052')

#print(os.path.isabs('E:/QQ/文档数据/506713537/123.py'))

#新建文件夹大小一般都是4096字节，个别情况为0
#os.path.getsize  查看文件夹或文件大小
#print(os.path.getsize('D:/老男孩'))
        




#def fun(filepath):
#    count=0
#    #1.打开文件夹
#    file=os.listdir(filepath)
#    #2.遍历文件夹的内容
#    for i in file:
#        #3.获取文件夹里的路径
#        fd=os.path.join(filepath,i)
#        #4.判断是不是文件夹
#        if os.path.isdir(fd) is True:
#            #5.如果是文件夹则再执行一编
#            a=os.path.join(filepath,i)   #获取路径
#            sum1=fun(a)
#            count+=sum1
#        else:
#            num=os.path.getsize(fd)
#            count+=num
#    return count
#print(fun('D:\\20170506121 刘永祺'))

#l=['D:\\20170506121 刘永祺']
#count=0
#while l:
#    path=l.pop()
#    filepath=os.listdir(path)
#    for i in filepath:
#        fd=os.path.join(path,i)
#        if os.path.isdir(fd) is True:
#            l.append(fd)
#        else:
#            count+=os.path.getsize(fd)
#print(count)          




















