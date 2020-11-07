# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 17:14:03 2019

@author: 50671
"""

#如何使用from import
#需要从一个文件中使用哪个名字，就把这个名字导入进来
#from my_module import name

#from import 的过程中仍然执行了这个被导入的文件

#当前文件命名空间和模块命名空间的问题
#from my_module import read
#import谁，就只能用谁
#def read():
#    print('这是我的函数')
    
#read()
#若函数命名相同，先导入的模块会被后导入的模块覆盖

#from import 导入过程中发生了什么事？
#1.找到要被导入的模块
#2.判断这个模块是否被导入
#3.如果这个模块没被导入过
    #创建一个属于这个模块的命名空间
    #执行这个文件
    #找到你要导入的变量
    #给你要导入的变量创建一个引用，指向要导入的变量
    
#导入多个名字
#from my_module import read1,read2
#给导入的模块起别名
#from my_module import read1 as r1,read2 as r2
#from my_module import read as r
#r()

#from my_module import *   #在导入过程中 内存的引用变化
#name='鸡巴'
#print(name)
#read()
#read2()

    
    
    
    
    
    
    
    

