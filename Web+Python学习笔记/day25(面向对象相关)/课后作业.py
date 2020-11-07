#1.类变量和实例变量的区别？
#   实例变量(字段)访问时,使用对象访问,即: obj1.name
#   类变量(静态字段)访问时,使用类方法,即: Foo.country  (实在不方便时,才使用对象)

#2.super的作用？
#获取了父类，并调用父类的方法。
#3.isinstance和type的区别并用代码举例说明？
#type('参数')  #获取当前对象由哪个类创建
#isinstance(obj,Foo)  ##判断第一个参数（对象）是不是第二个参数（类以及父类）的实例

#4.补全代码
#    def func(arg):
#        """
#        判断arg是否可以被调用，如果可以则可以执行并打印其返回值，否则直接打印结果
#        ：param args：传入参数
#        """
#        result=callable(arg)
#        return result

#5.补全代码
#from types import FunctionType,MethodType
#class Foo:
##    def __call__(self,*args,**kwargs):
##        pass
#    def func(self):
#        pass
#obj=Foo()
#def func(*args):
#    Function=0
#    Method=0
#    Fooson=0
#    other=0
#    """
#    计算args中的函数、方法、Foo类的个数，并返回给调用者
#    :param args: 传入参数
#    """
#    for i in args:
#        if isinstance(i,MethodType):
#            Method+=1
#        elif isinstance(i,FunctionType):
#            Function+=1
#        elif isinstance(i,Foo):
#            Fooson+=1
#        else:
#           other+=1 
#    print(f"args中函数有{Function}个,方法有{Method}个,Foo子类个数有{Fooson}个,其他{other}个")
#            
#func(obj.func,obj,3,4,5)

#6.看代码写结果并画图表示对象和类的关系以及执行流程
#class StarkConfig(object):
#    list_display = []
#    
#    def get_list_display(self):
#        self.list_display.insert(0,33)
#        return self.list_display
#
#class RoleConfig(StarkConfig):
#    list_display = [11,22]
#
#s1 = StarkConfig() 
#s2 = StarkConfig()
#
#result1 = s1.get_list_display()
#print(result1) 
#result2 = s2.get_list_display() 
#print(result2)
#[33],[33,33]

#7.看代码写结果并画图表示对象和类的关系以及执行流程
#class StarkConfig(object): 
#    list_display = []
#    
#    def get_list_display(self): 
#        self.list_display.insert(0,33) 
#        return self.list_display
#
#class RoleConfig(StarkConfig):
#    list_display = [11,22]
#
#s1 = StarkConfig() 
#s2 = RoleConfig()
#
#result1 = s1.get_list_display()
#print(result1)   #[33]
#result2 = s2.get_list_display() 
#print(result2)   #[33,11,22]

##8.看代码写结果画图表示对象和类的关系以及执行流程
#class StarkConfig(object): 
#    list_display = []
#    
#    def get_list_display(self): 
#        self.list_display.insert(0,33) 
#        return self.list_display
#
#class RoleConfig(StarkConfig):
#    list_display = [11,22]
#
#s1 = RoleConfig() 
#s2 = RoleConfig()
#
#result1 = s1.get_list_display()
#print(result1)   #[33,11,22]
#result2 = s2.get_list_display() 
#print(result2)   #[33,33,11,22]
#
##9.看代码写结果
#class Base(object): 
#    pass 
#class Foo(Base): 
#    pass 
#print(issubclass(Base, Foo))
#
##10.背写你了解的所有特殊方法并附示例

##11.如果有以下handler.py文件，请在run.py中补充代码实现：
#
##12.补充代码
#class Foo(object): 
#    def __init__(self): 
#        self.name = '鸡吧' 
#        self.age = 100 
#obj = Foo() 
#setattr(obj, 'email', 'wupeiqi@xx.com')
#
##一行代码实现获取obj中所有成员(字典类型)
#
##13看代码写结果
#class Foo(object): 
#    def __init__(self): 
#        self.name = '鸡吧' 
#        self.age = 100 
#obj = Foo() 
#setattr(Foo, 'email', 'wupeiqi@xx.com')
#
#v1=getattr(obj,'email')   #'wupeiqi@xx.com'
#v2=getattr(Foo,'email')   #'wupeiqi@xx.com'
#
#print(v1,v2) 
#
##14.什么是可迭代对象？如何将一个对象编程可迭代对象？
#def __iter__(self):
#    return iter([1,2,3,4,5,6])
'''
如果想要把不可迭代对象 ——> 可迭代对象
1.在类中定义__iter__方法
2.iter内部返回一个迭代器（生成器也是一种特殊的迭代器）
'''
##15.如何让一个对象可以被执行？ 即：后面加()
#
#16.补充选课系统（必须用反射）
class Course: 
    def __init__(self,cname,price,period): 
        self.cname = cname 
        self.price = price 
        self.period = period 
        
c1=Course('法理课',11,'星期一')
c2=Course('茶艺',12,'星期二')
c3=Course('C语言',13,'星期三')
c4=Course('python',14,'星期四')
c5=Course('Java',15,'星期五')
c6=Course('排球',16,'星期一')
c7=Course('游泳',17,'星期二')
c8=Course('人工智能',18,'星期三')
c9=Course('近代史',19,'星期四')
c10=Course('数学建模',20,'星期五')
course_list=[]  


class Student(Course): 
    def __init__(self,name): 
        self.name = name 
        self.courses = [] 
        self.lname=[]
    def select_course(self): 
        """ 
        选择课程，已选的不能再选
        """ 
        for i in course_list:
            self.lname.append(i.cname)
        cur=input('请输入你要选择的课程：')
        if cur in self.courses:
            print("课程已存在！")
        elif cur not in self.lname:
            print('没有此课程!')
        elif cur not in self.courses:
            self.courses.append(cur)
        elif cur not in self.lname:
            print('没有此课程!')
            
    def show_selected_course(self): 
        """ 
        查看所有课程
        """ 
        for i in course_list:
            print(i.cname)
    def show_my_course(self):
        """
        查看自己所选课程
        """
        print(self.courses)
    def show_del_course(self): 
        """ 
        删除已选课程
        """ 
        remove=input('请输入你要删除的课程：')
        self.courses.remove(remove) 
def run(): 
    """ 
    主程序
        1.根据Course类创建10个课程10 
        2.用户输入学生姓名，动态创建学生对象。
        3.查看所有课程
        4.为学生选课
        5. 查看学生已选课程
        6.删除已选课程
    """ 
    
    for i in range(1,11):
        course_list.append(eval('c'+str(i)))
        
    Name=input('请输入姓名:')
    Obj=Student(Name)

    while True:
        num=input("""
  请输入序号：
  1.选择课程
  2.所有课程
  3.查看自己所选课程
  4.删除已选课程
  5.退出
          """)
        if num == '1':
            func=getattr(Obj, 'select_course')
            func()
        elif num == '2':
            func=getattr(Obj,'show_selected_course')
            func()
        elif num == '3':
            func =getattr(Obj,'show_my_course')
            func()
        elif num == '4':
            func =getattr(Obj,'show_del_course')
            func()
        elif num == '5':
            break
        else:
            print('输入不正确请重新输入！')
run()    
    

    
 













