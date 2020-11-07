class School:
    def __init__(self,school,address):
        self.school=school
        self.address=address
        
    def speech(self):
        print('讲课')
        
class Teacher:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        self.school=None

obj1=School('翔一','翔安')
obj2=School('同一','同安')
obj3=School('宁师','宁德')

t1=Teacher('刘永祺','20','15000')
t2=Teacher('刘永','21','10000')
t3=Teacher('刘祺','19','5000')

t1.school=obj1
t2.school=obj2
t3.school=obj3
print(t1.school.address)
print(t2.school.address)
print(t3.school.address)