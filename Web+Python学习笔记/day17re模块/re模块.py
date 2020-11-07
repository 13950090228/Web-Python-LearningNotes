import re
#永远不要起一个py文件的名字
#regex  正则表达式

#查找
#findall：匹配所有 每一项都是列表中的一个元素
#ret=re.findall('\d+','785股份76股红股65')
#ret=re.findall('\d','785股份76股红股65')
#print(ret)

#search：只匹配从左到右的第一个，得到的不是直接的结果，而是一个变量，通过这个变量的group方法来获取结果
#如果没匹配到会返回None，继续使用group会报错
#ret=re.search('\d+','785股份76股红股65')
#print(ret) #内存地址，这是一个正则匹配的结果
#print(ret.group()) #通过ret.group()获取真正的结果

#match:从头开始匹配，相当于search中的正则表达式开头加 ^ ,开头不是要寻找的对象就返回None
#ret=re.match('\d+','785股份76股红股65')
#print(ret)
#print(ret.group())


#字符串处理的扩展：替换 切割
#split
#s='alex83sdug40sdgsfg25'
#ret=re.split('\d+',s)
#print(ret)

#sub 替换 (正则，新的，替换目标，替换次数)
#ret=re.sub('\d+','H','alex83sdug40sdgsfg25',2)
#print(ret)

#subn 在sub基础上返回元组，并会写出替换了几次
#ret=re.subn('\d+','H','alex83sdug40sdgsfg25')
#print(ret)

#re模块进阶：时间/空间
#compile：节省你使用正则表达式解决问题的时间
#编译 正则表达式 编译成 字节码
#在多次使用的过程中 不会多编译
#ret=re.compile('\d+')  #提前编译完，到时候直接使用就可以了
#res=ret.findall('alex83sdug40sdgsfg25')
#res=ret.search('alex83sdug40sdgsfg25')
#res=ret.sub('H','alex83sdug40sdgsfg25')
#print(res)

#finditer：节省你使用正则表达式解决问题的空间
#ret=re.finditer('\d+','alex83sdug40sdgsfg25')  #返回的是search结果的迭代器
#for i in ret:
#    print(i.group())

#s='1lex83sdug40sdgsfg25'
#ret=re.compile('\d+')
#res=ret.finditer(s)
#for i in res:
#    print(i.group())
#ret=re.compile('\d+')
#ret=re.findall('\d+',s)
#ret=re.search('\d+',s)
#ret=re.match('\d+',s)
#ret=re.split('\d+',s)
#ret=re.sub('\d+','H',s)
#ret=re.subn('\d+','H',s)
#res=ret.findall(s)
#print(res)










