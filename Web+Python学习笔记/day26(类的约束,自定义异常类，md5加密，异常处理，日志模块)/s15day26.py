s15day26 

内容回顾：
	1. 成员
		- 变量
			- 静态字段，类变量
		- 方法
			- 类方法
			- 静态方法
			- 实例方法 
		- 属性
	2. 对象的嵌套
	3. 特殊方法
		__init__
		new
		call 
		getitem...
		add 
		enter
		exit
		iter
		str
		dict 
		doc
	4. 反射
		- getattr
		- has 
		- set 
		- del 
	5. issubclass/isinstance/type/callable  ——> 内置函数
	6. 公有和私有（修饰符）
	7. 三大特性：继承、封装、多态
	8. super
	9. 函数和方法的区别？
	10. self到底是谁？
	11. 继承、多继承 
	
	12. 关于类变量的改变


	面向对象
		- 三大特性
			- 继承 
				- 单继承，示例：
				- 多继承，示例：
				- super 
			- 封装 
				- 数据封装
				- 方法封装
			- 多态 
				- 鸭子模型
		- 成员 
			- 变量
				- 实例
				- 类 
			- 方法
				- 示例方法 
				- 类方法 
				- 静态方法
				- 特殊方法 
					...
			- 属性 
				- @property，分页 
				
		- 修饰符 
			- 私有
				- 编写 
				- 派生类
			- 公有 
			
		- 易错点
			- self 
	
	内置函数：
		- issubclass
		- isinstance
		- type
		- callable
	函数和方法的区别？ 
	
	反射 
			
	问题：匿名函数是否可以在类中？
		
		class Foo:
			
			v = lambda self,x: x+1
			
			def v(self,x):
				return x + 1
	
今日内容：
	1. 约束 
	
	2. 自定义异常
	
	3. hashlib 
	
	4. logging 
	
内容详细：
	1. 约束 
		建议使用：
			class BaseMessage(object):
				def send(self):
					"""
					必须继承BaseMessage，然后其中必须编写send方法。用于完成具体业务逻辑。
					"""
					raise NotImplementedError(".send() 必须被重写.")
					# raise Exception(".send() 必须被重写.")
					
					
					
			BaseMessage类用于约束，约束其派生类：保证派生类中必须编写send方法，不然执行可能就会报错。
		
			
			class BaseMessage(object):
				def send(self):
					"""
					必须继承BaseMessage，然后其中必须编写send方法。用于完成具体业务逻辑。
					"""
					raise Exception()
			
			class Email(BaseMessage):
				def send(self):
					pass # 发送邮件
					
				def f1(self):
					pass 
				
				def f2(self):
					pass 
			class Wechat(BaseMessage):
				def send(self):
					pass # 发送微信
				
				def f1(self):
					pass 
				
				def f2(self):
					pass 
			class Msg(BaseMessage):
				def send(self):
					pass # 发送短信
					
				def f1(self):
					pass 
				
				def f2(self):
					pass 
					
					
			def func(arg):
				"""
				报警通知的功能
				"""
				arg.send()
				
			
			obj = Msg()
			func(obj)
		
		Python：
			类 
				类：
					class Foo:
						pass 
				抽象类和抽象方法：
					
		Java、C#:
			类 
				类 
					class Foo:
						def f1(self):
							pass 
							
						def f2(self):
							pass # 可人为抛出异常。 
							
					class Bar(Foo):
						def f1(self):
							pass 
				
				抽象类，约束，约束继承它的派生类必须实现它其中的抽象方法。
					abstact class Foo:
						def f1(self):
							print(1,3,4) 
							
						abstact def f2(self):pass
					
					class Bar(Foo):
						def f2(self):
							print('111')
							
					
					
			接口，接口中不允许在方法内部写代码，只能约束继承它的类必须实现接口中定义的所有方法。
				interface IFoo:
					
					def f1(self,x1):pass 
					
					def f2(self,x1):pass 
					
				interface IBar:
					
					def f3(self,x1):pass 
					
					def f4(self,x1):pass 
				
				class Foo(IFoo,IBar):# 实现了2个接口
					
					def f1(self,x1):pass 
					
					def f2(self,x1):pass 
					
					def f3(self,x1):pass 
					
					def f4(self,x1):pass 
	
		总结：
			1. 什么是接口以及作用？
				接口时一种数据类型，主要用于约束派生类中必须实现指定的方法。
				Python中不存在，Java和C# 中是存在的。
			2. Python中使用过什么来约束呢？
				- 抽象类+抽象方法，编写上麻烦。
				- 人为主动抛出异常 
			
			3. 约束时，抛出的异常是否可以用其他的？
				不专业：raise Exception(".send() 必须被重写.")
				专业：raise NotImplementedError(".send() 必须被重写.")
				
			4. 以后看代码，揣摩心思
				
			5. 写代码：
				class BaseMessage(object):
					def send(self,x1):
						"""
						必须继承BaseMessage，然后其中必须编写send方法。用于完成具体业务逻辑。
						"""
						raise NotImplementedError(".send() 必须被重写.")

				class Email(BaseMessage):
					def send(self,x1):
						"""
						必须继承BaseMessage，然后其中必须编写send方法。用于完成具体业务逻辑。
						"""
						print('发送邮件')


				obj = Email()
				obj.send(1)
				
	
			6. 应用场景：
				多个类，内部都必须有某些方法时，需要使用基类+异常进行约束。
				学员管理程序：
					
					class IBase:
						def login():
							raise NotImplementedError(".send() 必须被重写.")
					
					class Student:
						def login(self):
							pass 
							
						def score(self):
							pass 
							
					class Teacher:
						def login(self):
							pass 
							
						def exam(self):
							pass 
							
					class Manager(self):
						def login(self):
							pass 
							
						....
	
	
	2. 自定义异常
	
		# 知识点：如何自定义异常类？
		class MyException(Exception):
			def __init__(self,code,msg):
				self.code = code
				self.msg = msg
		try:
			# 知识点：主动抛出异常 
			raise MyException(1000,'操作异常')

		except KeyError as obj:
			print(obj,1111)
		except MyException as obj: # 知识点：捕获异常 
			print(obj,2222)
		except Exception as obj:
			print(obj,3333)
			
	
	3. 加密 
		
		
		关键词：撞库 
			
		加盐
	
	
	4. 日志 logging
	
		为什么要有日志？
			给开发人员看，用于排查错误。
		
	
	总结：
		1. 约束 		***
			
		2. md5 			*****
		
		3. 自定义异常   *** 
		
		4. 日志处理     ****
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	