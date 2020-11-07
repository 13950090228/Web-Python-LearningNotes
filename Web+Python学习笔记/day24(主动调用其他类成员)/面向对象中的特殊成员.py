class Foo:
    def __init__(self,a1,a2):
        self.a1=a1
        self.a2=a2
        
    def __call__(self,*args,**kwargs):
        print(1111,*args,*kwargs)
        
    def __getitem__(self,item):
        print(item)
    
    def __setitem__(self,key,vaule):
        print(key,vaule)
        
    def __delitem__(self,key):
        print(key)
        
    def __add__(self,other):
        return self.a2+other.a2
    
    def __enter__(self):
        print('enter')
        return 666
        
    def __exit__(self,a,b,c):
        print('exit')
#1.类名（） 自动执行 __init__
obj = Foo(1,2)

#2.对象（） 自动执行 __call__
#obj(4,5,6)

#3.对象[] 自动执行 __getitem__
#obj['鸡巴']

#4.对象['xx']=xx 自动执行 __setitem__
#obj['啊']=11

#5.del 对象['xx'] 自动执行 __delitem__
#del obj['懒趴']

#6.对象 + 对象 自动执行 __add__
#obj1=Foo(1,2)
#obj2=Foo(3,4)
#print(obj1+obj2)

#7.with 对象
#with obj:
#    print('a a ')
#    
#with obj as f:
#    print(f)

#8.真正的额构造方法
class Foo:
    def __init__(self,a1,a2):   #初始化方法
        #对空对象进行数据初始化
        self.a1=a1
        self.a2=a2
        print(1)
    def __new__(cls,*args,**kwargs):   #构造方法
        print(2)
        return object.__new__(cls)   #python内部创建一个当前类的对象，初创时时空的

obj=Foo(1,2)


















