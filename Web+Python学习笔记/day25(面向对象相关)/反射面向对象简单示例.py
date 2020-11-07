class Foo:
    name='刘永祺'
    def func(self):
        print('啊啊啊')
obj=Foo()
func=getattr(obj,'func')   #obj.func 
func1=getattr(Foo,'name')  #Foo.func
print(func()) 
print(Foo.func(1)) 
#根据字符串为参数（第二个参数），去对象（第一个参数）中寻找与之同名的成员