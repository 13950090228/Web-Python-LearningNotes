# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 17:18:14 2019

@author: 50671
"""
#__dict__ 将传入的值以字典形式打印出来
class Foo:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __iter__(self):
        return iter([1,2,3,4,5,6])

#obj1=Foo('刘永祺',20)
#print(obj1.__dict__)     #{'name': '刘永祺', 'age': 20}

'''
如果想要把不可迭代对象 ——> 可迭代对象
1.在类中定义__iter__方法
2.iter内部返回一个迭代器（生成器也是一种特殊的迭代器）
'''
obj = Foo('刘永祺',99)
for i in obj:
    print(i)