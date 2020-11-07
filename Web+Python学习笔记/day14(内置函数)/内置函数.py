lst=['北京','天津','上海','深圳','厦门']
#it=iter(lst)  #iter内部封装的是__iter__()
#n=next(it)    #next内部封装的是__next__()

#
#ls=(1,2,3,4,5,6)
#print(id(ls))  #查看内存地址
#print(hash(ls)) #目的是为了存储，计算后是一个数字，hash值尽量不要重复
#字典和哈希算法是用空间换时间，查找速度快，但是很占内存
#print(help(str))    #help  帮助文档 
#def a():
#    pass
#
#print(callable(a))  #callable()查看是否可以调用
#print(type(a))   #type()查看元素类型
#print(bin(5))     #查看元素的二进制   0b二进制
#print(oct(10))    #查看元素的八进制   0o八进制
#print(hex(15))    #查看元素16进制     0x十六进制
#print(abs(-19))    #查看元素的绝对值
#print(divmod(10,3))  #计算商和余
#print(round(3.45))   #四舍五入
#print(pow(5,2,4))     #求次幂，第三个数参数计算余数
#print(sum([1,2,3,4,5],3))  #第一个参数里添加列表并求，第二个参数加上前面参数的和
#ll=reversed(lst)  #reversed翻转，返回的是迭代器
#print(list(ll))
#print(lst[slice(1,6,2)])
#print(lst[1:6:2])        #两个等价，上一个用的是内置函数

#print(ord('b'))   #输入字符找到这个字符的编码位置（ascii）
#print(chr(457))    #输入位置找到字符
#print(ascii('a'))   #查询元素有没有在ascii码里，有的话返回该值，没有返回u

#s = "你好" 
#bs = s.encode("UTF-8") 
##print(bs) 
##s1 = bs.decode("UTF-8") 
##print(s1) 
##bs = bytes(s, encoding="utf-8")     # 把字符串串编码成UTF-8 print(bs)
#print(bytes(bs))

#print('刘永祺说："我很帅"')
#print('刘永祺说：\'我很帅\'')  #\" 转义，不让"成为字符串的开头和结尾
#print(repr('刘永祺说：\我很帅\t'))  #repr原样输出字符串，引号还是会有影响
#print(repr('你好\啊'))
#print(r'"刘永祺说："我很帅""')

#s='大鸡巴'
#print(s.center(20))   #拉长到20，源字符串居中
#print(format(s,'>20'))

#print(format(13,'o'))
#print(format(1.23724,'0.2f'))
#print(format(123456789,'e'))

#s={'盗墓笔记','心理罪','鬼吹灯','十宗罪'}
#s.add('鸡巴')
#print(s)
#s=frozenset({'战狼','西洪市首富'})
#print(hash(s))
#for i,j in enumerate(lst,1):
#    print(i,j)
#print(all([True,1,0]))   #all() add  所有为真才是真
#print(any([False,0,0]))  #any() or   有一个为真就是真
#zip() 压缩
#lst=['北京','天津','上海','深圳','厦门']
#lst2=['烤鸭','包子','鸡巴','肠粉','沙茶面']
#lst3=[1,2,3,4,5]
#a=zip(lst,lst2,lst3) #zip水桶效应，以最短的为最终长度
#for j in a:
#    print(j)
#s='5+ 6'
#ret=eval(s) #动态执行一个代码片段，侧重点在返回
#print(ret)
#eval #还原字典，列表,在前端有用

#eval对比exec，eval侧重返回值，执行相对简单的胆码。exec不侧重返回值，执行相对复杂的代码
#s='a=10'
#exec(s)
#b="a=input('输入你的代码：')"
#exec(b)   #测试别人的代码时能用  
#print(a)

#compile 编译    exec 执行
#s='1+2+3'
#c=compile(s,"",mode='eval')  
#a=eval(c)
#print(a)

#s='for i in range(10): print(i)'
#c=compile(s,"",mode='exec')
#exec(c)
#print(c)

#s="a=input('请输入：')"
#c=compile(s,"",mode='single')   
#exec(c)
#print(a)

a=print('你好，我是大鸡巴')  #对用户友好

#正式官方的字符串
print(repr("你好,我\'是\"大鸡巴"))  #程序中内部存储的内容，这个是给程序员看的

#原样输出
print(r"麻花疼说我：'我几把给你喊','啊手动阀',''\n\t\\'")
print("我叫%r" %"周润发") #%r 司机上调用的是repr()






