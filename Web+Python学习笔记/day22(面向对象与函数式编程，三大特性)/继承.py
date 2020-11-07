##################1.基本写法###################
#class Super:
#    def f3(self):
#        print('f3')
#class Base(Super):             #父类，基类
#    def f2(self):
#        print('f2')
#class Foo(Base):        #子类，派生类
#    def f1(self):
#        print('f1')
#
#a=Foo()
#a.f1()

###################2.多继承#########################
#class Base1:
#    def f2(self):
#        print('base1')
#class Base2:            
#    def f2(self):
#        print('base2')
#class Foo(Base1,Base2):    #有=优先查找左边的    
#    pass
#
#a=Foo()
#a.f2()
####################################################

#易错题
#class Base:
#    def f1(self):
#        print('Base.f1')
#        
#    def f3(self):
#        self.f1()    
#        print('Base.f3')
#class Foo(Base):
#    def f1(self):
#        print('Foo.f1')
#        
#    def f2(self):
#        print('Foo.f2')
#        self.f3()
#obj=Foo()
#obj.f2()   #obj是哪一个类(Foo)，那么执行方法时，就从该类开始找。
#
#obj2=Base()
#obj2.f3()
'''
总结：self是哪个类的对象，那么就从该类开始找。
'''
class Base1:
    def f1(self):
        print('base1.f1')
    def f2(self):
        print('base1.f2')
        
class Base2:
    def f1(self):
        print('base2.f1')
    def f2(self):
        print('base2.f2')
    def f3(self):
        print('base2.f3')
        self.f1()
class Foo(Base1,Base2):    #有=优先查找左边的    
    def f0(self):
        print('foo.f0')
        self.f3()

a=Foo()
a.f0()


