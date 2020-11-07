import re
s='<a>wahaha</a>'
#ret=re.search('<(\w+)>(\w+)</(\w+)>',s)
#print(ret.group())   #所有的结果
#print(ret.group(1))  #数字参数代表的是分组的顺序
#print(ret.group(2))
#print(ret.group(3))

#为了findall也可以顺利取到分组中的内容，有一个特殊语法，就是优先显示分组中的内容
#ret=re.findall('>(\w+)<',s)
#print(ret)

#取消分组优先在括号中加 (?:正则表达式) 
#python 和 正则表达式 之间的特殊约定
#只能在findall里面使用
#ret=re.findall('\d(?:\.\d+)','1.234*4.3')
#print(ret)

#正则加了括号会把切掉的显示出来
#ret=re.split('(\d+)','alex83sdug40sdgsfg25')
#print(ret)

#分组命名（?P<这个组的名字>正则表达式）
#ret=re.search('>(?P<con>\w+)<',s)
#print(ret.group('con'))

#使用前面的分组，要求使用这个名i的分组和前面同名愤怒中的内容相同
pattern='<(?P<tab>\w+)>(\w+)</(?P=tab)>'
ret=re.search(pattern,s)
print(ret.group(2))

#import re
#ret=re.findall("\d+\.\d+|(\d+)","1-2*(60+(-40.35/5)-(-4*3))")
#ret.remove('')
#print(ret)
##正则表达式如果写得好可以最大程度简化我们的操作



