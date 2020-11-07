s15day25 面向对象相关

内容回顾：
	1. 昨日知识点
		- 特殊成员 
		- 组合嵌套 
		- 主动调用其他类成员
			- super
	2. 列举特殊成员
		__enter__
		__exit__
		__call__
		__getitem__,obj['xx']
		__setitem__,obj['xx'] = 1
		__delitem__,del obj['xx']
		__new__,
		__init__
		__add__
		
		__str__
			class Foo(object):
				def __init__(self):
					pass

				def func(self):
					pass

				def __str__(self):
					return "F1"

			obj = Foo()
			print(obj,type(obj))
		__doc__
			
			class Foo(object):
				"""
				asdfasdfasdfasdf
				"""
				def __init__(self):
					pass

				def func(self):
					pass

				def __str__(self):
					return "F1"

			obj = Foo()
			print(obj.__doc__)
		__dict__
			
			class Foo(object):
				def __init__(self,name,age):
					self.name = name
					self.age = age

				def func(self):
					pass

			obj1 = Foo('刘博文',99)
			obj2 = Foo('史雷',89)


			print(obj1.__dict__) # {'name': '刘博文', 'age': 99}
			print(obj2.__dict__) # {'name': '史雷', 'age': 89}
		__iter__
			# l1是list类的一个对象，可迭代对象
			l1 = [11,22,33,44]

			# l2是list类的一个对象，可迭代对象
			l2 = [1,22,3,44]


			class Foo(object):
				def __init__(self,name,age):
					self.name = name
					self.age = age

				def func(self):
					pass

				def __iter__(self):
					# return iter([11,22,33,44,55,66])

					yield 11
					yield 22
					yield 33

			# obj1是Foo类的一个对象，可迭代对象
			"""
			如果想要把不可迭代对象 -> 可迭代对象
			1. 在类中定义__iter__方法
			2. iter内部返回一个迭代器(生成器也是一种特殊迭代器)
			"""
			obj1 = Foo('刘博文',99)

			for item in obj1:
				print(item)
	3. 练习题：... 
		
今日内容：
	1. isinstance/issubclass/type
	
	2. 方法和函数
	
	3. 反射 
	
	4. 其他 
	
内容详细：
	1. issubclass/type/isinstance/
	
		issubclass
			class Base(object):
				pass

			class Foo(Base):
				pass

			class Bar(Foo):
				pass

			print(issubclass(Bar,Base)) # 检查第一个参数是否是第二个参数的 子子孙孙类
			
		type:获取当前对象是由那个类创建。
				"""
				class Foo(object):
					pass

				obj = Foo()

				print(obj,type(obj)) # 获取当前对象是由那个类创建。
				if type(obj) == Foo:
					print('obj是Foo类型')
				"""

				# #### 练习题 
				"""
				class Foo(object):
					pass

				class Bar(object):
					pass

				def func(*args):
					foo_counter =0
					bar_counter =0
					for item in args:
						if type(item) == Foo:
							foo_counter += 1
						elif type(item) == Bar:
							bar_counter += 1
					return foo_counter,bar_counter

				# result = func(Foo(),Bar(),Foo())
				# print(result)

				v1,v2 = func(Foo(),Bar(),Foo())
				print(v1,v2)
				"""
			
		isinstance,检查第一个参数（对象）是否是第二个参数（类及父类）的实例。
						
			class Base(object):
				pass

			class Foo(Base):
				pass

			obj1 = Foo()
			print(isinstance(obj1,Foo))  # 检查第一个参数（对象）是否是第二个参数（类及父类）的实例。
			print(isinstance(obj1,Base)) # 检查第一个参数（对象）是否是第二个参数（类及父类）的实例。


			obj2 = Base()
			print(isinstance(obj2,Foo))  # 检查第一个参数（对象）是否是第二个参数（类及父类）的实例。
			print(isinstance(obj2,Base)) # 检查第一个参数（对象）是否是第二个参数（类及父类）的实例。



			# #################### 练习
			"""
			给你一个参数，判断对象是不是由某一个指定类？ type                  --> type(obj) == Foo
			给你一个参数，判断对象是不是由某一个指定类或其父类？ isinstance    --> instance(obj,Foo)
			"""
		
		
	2. 方法和函数
		称谓：
			类，方法
			外，函数
		到底方法函数？
			对象.xxx  --> xxx就是方法
			类.xxx    --> xxx就是函数
			xxx       --> xxx就是函数
		打印查看：
			function 
			method 
			
		代码检查：
			from types import MethodType,FunctionType
			def check(arg):
				"""
				检查arg是方法还是函数？
				:param arg:
				:return:
				"""
				if isinstance(arg,MethodType):
					print('arg是一个方法')
				elif isinstance(arg,FunctionType):
					print('arg是一个函数')
				else:
					print('不知道是什么')
		
	
	3. 反射
		a. 需求
		
		总结：
			v = getattr(obj,"func")  # 根据字符串为参数（第二个参数），去对象（第一个参数）中寻找与之同名的成员。
			
		练习题：	
			..
			
		好记：
			getattr # 根据字符串的形式，去对象中找成员。
			hasattr # 根据字符串的形式，去判断对象中是否有成员。
			setattr # 根据字符串的形式，动态的设置一个成员（内存）
			delattr # 根据字符串的形式，动态的删除一个成员（内存）
		应用一：
			# by luffycity.com
			from types import FunctionType
			import handler

			while True:
				print("""
				系统支持的函数有：
					1. f1
					2. f2
					3. f3
					4. f4
					5. f5
				""")
				val = input("请输入要执行的函数：") # val = "f1"

				# 错误
				# handler.val()
				if hasattr(handler,val):
					func_or_val = getattr(handler,val)     # 根据字符串为参数，去模块中寻找与之同名的成员。
					if isinstance(func_or_val,FunctionType):
						func_or_val()
					else:
						print(func_or_val)
				else:
					print('handler中不存在输入的属性名')

				# 正确方式
				"""
				if val == 'f1':
					handler.f1()
				elif val == 'f2':
					handler.f2()
				elif val == 'f3':
					handler.f3()
				elif val == 'f4':
					handler.f4()
				elif val == 'f5':
					handler.f5()
				"""
		
		应用二：
			
			class Account(object):
				func_list = ['login', 'logout', 'register']

				def login(self):
					"""
					登录
					:return:
					"""
					print('登录111')

				def logout(self):
					"""
					注销
					:return:
					"""
					print('注销111')

				def register(self):
					"""
					注册
					:return:
					"""
					print('注册111')

				def run(self):
					"""
					主代码
					:return:
					"""
					print("""
						请输入要执行的功能：
							1. 登录
							2. 注销
							3. 注册
					""")

					choice = int(input('请输入要执行的序号:'))
					func_name = Account.func_list[choice-1]

					# func = getattr(Account,func_name) # Account.login
					# func(self)

					func = getattr(self, func_name)  # self.login
					func()

			obj1 = Account()
			obj1.run()

			obj2 = Account()
			obj2.run()
		
总结： 
	
	反射 *****
	issubclass/type/isinstance/ ***
	方法和函数 * 
		
	问题：你见过的什么后面可以加()? 
			- 类()
			- 对象()
			- 函数()
			- 方法()
			以上所有都可以被调用。
			
	示例：
		def func():
			pass


		class Foo(object):
			def __call__(self, *args, **kwargs):
				pass
			def func(self):
				pass
		obj = Foo()


		print(callable(func))
		print(callable(Foo))
		print(callable(obj))
		print(callable(obj.func))
			
作业：
	
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		