#-*- encoding:utf-8 -*-
s='\ue415'
#print(s.encode('gbk')) #编码指定编码成什么样的编码类型
#print(s.encode('utf-8'))
print(s.decode('unicode'))
#编码和解码
#    ascii 码
#        不支持 中文
#        支持   英文 数字 符号
#        8位 一字节
#        
#    gbk   国际：
#        支持中文，英文，数字，符号
#        英文 两个字节 16位
#        中文 两个字节 16位
#        
#    unicode 万国码：(不做文件传输)
#        支持   英文 数字 符号
#        英文 32位 四个字节
#        中文 32位 四个字节
#        
#    utf-8 长度可变的万国码，最少用8位：
#        英文 8位  一个字节
#        中文 24位 三个字节
     #python3中 程序运行阶段 使用的是unicode
     #bytes 类型（传输和储存都是使用bytes）