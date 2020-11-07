s15day24

内容回顾:
	1. 成员
		- 变量
			- 类变量(静态字段)  类.字段/对象.字段 
			- 示例变量(字段)	对象.字段
		- 方法
			- 实例方法			对象.方法名
			- 静态方法			类.方法名/对象.方法名 
			- 类方法			类.方法名/对象.方法名 
		- 属性
			- 属性 				对象.属性名 
	2. 修饰符 
		
	3. 组合(嵌套)


今日内容:
	1. 组合补充
	
	2. 主动调用其他类的成员
	
	3. 特殊成员 
	
	4. isinstance/issubclass/type 
	
	
	
	
内容详细:
	1. 组合补充 
	
	
	2. 主动调用其他类的成员
		方式一: 
			
			class Base(object):

				def f1(self):
					print('5个功能')

			class Foo(object):

				def f1(self):
					print('3个功能')
					Base.f1(self)

			obj = Foo()
			obj.f1()
			
			总结:
				Base.实例方法(自己传self)
				与继承无关
				
	
		# ########### 方式二:按照类的继承顺序,找下一个.
			class Foo(object):
				def f1(self):
					super().f1()
					print('3个功能')

			class Bar(object):
				def f1(self):
					print('6个功能')

			class Info(Foo,Bar):
				pass

			# obj = Foo()
			# obj.f1()

			obj = Info()
			obj.f1()

	
	3. 特殊成员 	
	
重点:
	1. 组合练习题 *****
	2. 主动调用其他类的成员 ***
	3. 特殊成员 ***
	
作业:
	






































	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	


