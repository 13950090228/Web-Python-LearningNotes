#class Base(object): 
#    pass 
#class F1(Base): 
#    pass 
#class F2(Base): 
#    pass 
#class F3(F2): 
#    pass 
#class F4(Base): 
#    pass 
#class F5(object): 
#    pass 
#class F6(F5): 
#    pass
class Course:
    def __init__ (self,name,price,period):
        self.name = name
        self.price = price
        self.period = period
        
cname,price,period=input('请输入：')
print(cname,price,period)