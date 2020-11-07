# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 22:00:03 2019

@author: 50671
"""
#方式一
#class Foo:
#    def f1(self):
#        print('foo.f1')
#        Base.f1(self)   #与继承无关
#        
#class Base:
#    def f1(self):
#        print('base.f1')
#        
#        
#obj=Foo()
#obj.f1()

#方式二   按照类的继承顺序找下一个
class Base:
    def f1(self):
        print('base.f1')
        
class Foo(Base):
    def f1(self):
        print('foo.f1')
        super().f1()
        

        
obj=Foo()
obj.f1()





      