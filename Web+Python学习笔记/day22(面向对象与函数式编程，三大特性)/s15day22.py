s15day22 面向对象 

接下来内容:
	第一部分:面向对象
	第二部分:网络编程
	第三部分:并发编程

内容回顾:
	1. 面向过程
	
	2. 函数式编程 
		
		def func(arg):
			pass
			
		func(1)
		func(2)
		
	3. 为什么要将某些函数写在指定文件中?
		对函数进行归类
	
今日内容:
	1. 函数式编程和面向对象的对比

	2. 面向对象代码如何编写
	
	3. 面向对象三大特性:封装/继承/多态
	
内容详细:
	1. 函数式编程和面向对象的对比
		
		a. round 1 请开发一个消息提醒的功能(邮件/短信/微信)   
			
			函数:
				def email(em,text):
					"""
					发送邮件
					:return:
					"""
					print(em,text)

				def msg(tel,text):
					"""
					发送短信
					:return:
					"""
					print(tel,text)

				def wechat(num,text):
					"""
					发送微信
					:return:
					"""
					print(num,text)


				# 编写功能:假设用户购买课程,然后给alex发送提醒;
				if 1==1:
					msg('188888888','张进购买了一个学位课')
					email('alex@sb.com','张进购买了一个学位课')
					wechat('xxxx','张进购买了一个学位课')

			面向对象:
				class Message:
					def email(self, em, text):
						"""
						发送邮件
						:return:
						"""
						print(em,text)

					def msg(self, tel, text):
						"""
						发送短信
						:return:
						"""
						print(tel,text)

					def wechat(self, num, text):
						"""
						发送微信
						:return:
						"""
						print(num,text)


				# 编写功能:假设用户购买课程,然后给alex发送提醒;
				if 1==1:
					obj = Message()
					obj.email('alex@sb.com', '张进购买了一个学位课')
					obj.msg('188888888','张进购买了一个学位课')
					obj.wechat('xxxx','张进购买了一个学位课')

			
			对比:
				函数:定义简单/调用简单
				面向对象:定义复杂/调用复杂   好处:归类,将某些类似的函数写在一起
				
			总结:
				1. 函数式编程可能会比面向对象好.
				2. Python中支持两种编程方式.
				3. 面向对象方式格式:
					定义:
						class 类名:					- 定义了一个类
							
							def 函数名(self):		- 在类中编写了一个"方法"
								pass 
					调用:
						x1 = 类名()					- 创建了一个对象/实例化一个对象
						x1.函数名()					- 通过对象调用其中一个方法.
						
				4. 示例:
					class Account:
						def login(self):
							user = input('请输入用户名:')
							pwd = input('请输入密码:')
							if user == 'alex' and pwd == 'sb':
								print('登录成功')
							else:
								print('登录失败')

					obj = Account()
					obj.login()
									
				
		b. round 2 打印 
			"""
			完成以下功能:
				老狗/20岁/男/上山去砍柴
				老狗/20岁/男/开车去东北
				老狗/20岁/男/喜欢大宝剑
			"""

			# ##################### 函数版本 #########################
			"""
			def kc(name,age,gender):
				data = "%s,性别%s,今年%s岁,喜欢上山砍柴" %(name,gender,age)
				print(data)

			def db(name,age,gender):
				data = "%s,性别%s,今年%s岁,喜欢开车去东北" %(name,gender,age)
				print(data)

			def bj(name,age,gender):
				data = "%s,性别%s,今年%s岁,喜欢大宝剑" %(name,gender,age)
				print(data)


			kc('老狗',20,'男')
			kc('老狗',20,'男')
			db('老狗',20,'男')
			bj('老狗',20,'男')
			"""
			# ##################### 面向对象 #########################
			class LaoGou:

				def __init__(self,name,age,gender): # 特殊的方法,如果 类名() ,则该方法会被自动执行 (构造方法)
					self.n1 = name
					self.n2 = age
					self.n3 = gender

				def kc(self):
					data = "%s,性别%s,今年%s岁,喜欢上山砍柴" %(self.n1,self.n3,self.n2)
					print(data)

				def db(self):
					data = "%s,性别%s,今年%s岁,喜欢开车去东北" %(self.n1,self.n3,self.n2)
					print(data)

				def bj(self):
					data = "%s,性别%s,今年%s岁,喜欢大宝剑" %(self.n1,self.n3,self.n2)
					print(data)

			obj = LaoGou('老狗',20,'男')
			obj.kc()
			obj.db()
			obj.bj()
	
			
			总结:
				1. 构造方法
					示例一:
						class Foo:
							
							def __init__(self,name):     构造方法,目的进行数据初始化.
								self.name = name 
								self.age = 18 
						
						obj = Foo('侯明魏')
						
						通过构造方法,可以将数据进行打包,以后使用时,去其中获取即可.
					
					示例二:	
						class Bar:
							pass 
						obj = Bar()
					
				2. 应用
					a. 将数据封装到对象中,以供自己在方法中调用
						class FileHandler:
							def __init__(self,file_path):
								self.file_path = file_path
								self.f = open(self.file_path, 'rb')

							def read_first(self):
								# self.f.read()
								# ...
								pass

							def read_last(self):
								# self.f.read()
								# ...
								pass

							def read_second(self):
								# self.f...
								# ...
								pass
							
						obj = FileHandler('C:/xx/xx.log')
						obj.read_first()
						obj.read_last()
						obj.read_second()
						obj.f.close()
					
					b. 将数据封装到对象中,以供其他函数调用 
						def new_func(arg):
							arg.k1
							arg.k2
							arg.k6

						class Foo:
							def __init__(self,k1,k2,k6):
								self.k1 = k1
								self.k2 = k2
								self.k6 = k6

						obj = Foo(111,22,333)
						new_func(obj)

					
		练习: 信息管理系统
			1. 用户登录
			2. 显示当前用户信息
			3. 查看当前用户所有的账单
			4. 购买姑娘形状的抱枕 
			
			示例:
				class UserInfo:

					def __init__(self):
						self.name = None

					def info(self):
						print('当前用户名称:%s' %(self.name,))

					def account(self):
						print('当前用户%s的账单是:....' %(self.name,))

					def shopping(self):
						print('%s购买了一个人形抱枕' %(self.name,))

					def login(self):
						user = input('请输入用户名:')
						pwd = input('请输入密码:')
						if pwd == 'sb':
							self.name = user
							while True:
								print("""
									1. 查看用户信息
									2. 查看用户账单
									3. 购买抱枕
								""")
								num = int(input('请输入选择的序号:'))
								if num == 1:
									self.info()
								elif num ==2:
									self.account()
								elif num == 3:
									self.shopping()
								else:
									print('序号不存在,请重新输入')
						else:
							print('登录失败')

				obj = UserInfo()
				obj.login()
			
			总结:
				class Foo:
					def func2(self):
						print('func2')
					
					def func1(self):
						self.fun2()
						print('func1')
						
						
				obj = Foo()
				obj.func1()
	
		
	2. 面向对象代码如何编写
		a. 规则 
			
			class Foo:
				
				def __init__(self,name):
					self.name = name 
					
					
				def detail(self,msg):
					print(self.name,msg)
					
			obj = Foo()
			obj.detail()
			
			
		b. 什么时候写?如何写?
			
			方式一:归类+提取公共值
				归类:
					class File:
						def file_read(self,file_path):
							pass

						def file_update(self,file_path):
							pass

						def file_delete(self,file_path):
							pass

						def file_add(self,file_path):
							pass

					class Excel:
						def excel_read(self,file_path):
							pass

						def excel_update(self,file_path):
							pass

						def excel_delete(self,file_path):
							pass

						def excel_add(self,file_path):
							pass
			
				提取公共值:
					class File:
						def __init__(self,file_path):
							self.file_path = file_path
							
						def file_read(self):
							pass

						def file_update(self):
							pass

						def file_delete(self):
							pass

						def file_add(self):
							pass

					class Excel:
						def __init__(self,file_path):
							self.file_path = file_path
							
						def excel_read(self):
							pass

						def excel_update(self):
							pass

						def excel_delete(self):
							pass

						def excel_add(self):
							pass
			
			方式二:在指定类中编写和当前类相关的所有代码 + 提取公共值
				
				class Message:
					def email(self):	
						pass 
				
				class Person:
					def __init__(self,na, gen, age, fig)
						self.name = na
						self.gender = gen
						self.age = age
						self.fight =fig
						
					def grassland(self):	
						self.fight = self.fight - 10  
						
					def practice(self):
						self.fight = self.fight + 90   
						
					def incest(self):
						self.fight = self.fight - 666
						
				
				cang = Person('苍井井', '女', 18, 1000)    # 创建苍井井角色
				dong = Person('东尼木木', '男', 20, 1800)  # 创建东尼木木角色
				bo = Person('波多多', '女', 19, 2500)      # 创建波多多角色
			
				dong.grassland()
			
			
	3. 面向对象的三大特性:封装/继承/多态 
		
		封装:
			将相关功能封装到一个类中:
				class Message:
					def email(self):pass
					def msg(self):pass
					def wechat(self):pass
			将数据封装到一个对象中:
				
				class Person:
					def __init__(self,name,age,gender):
						self.name = name
						self.age = age
						self.gender = gender
						
				obj = Person('孙福来',18,'女')
		继承:
			class SuperBase:
					def f3(self):
						print('f3')

				class Base(SuperBase):  # 父类,基类
					def f2(self):
						print('f2')

				class Foo(Base):        # 子类,派生类
					
					def f1(self):
						print('f1')
						
				obj = Foo()
				obj.f1()
				obj.f2()
				obj.f3()
				# 原则:现在自己类中找,么有就去父类
							
			总结:
				1. 继承编写 
					
					class Foo(父类):
						pass 
						
				2. 支持多继承(先找左/再找右)
				
				
				3. 为什么要有多继承? 提供代码重用性
				
				
				练习: 找self到底是谁的对象?从谁开始找.
				
		多态: 
			多种形态或多种状态
			鸭子模型,只要可以嘎嘎叫就是鸭子.
			
			Python
				#  由于python原生支持多态,所以没有特殊性.
				"""
				class Foo1:
					def f1(self):
						pass 
				
				class Foo2:
					def f1(self):
						pass 
				
				class Foo3:
					def f1(self):
						pass 
						
						
				def func(arg):
					arg.f1()
					
				obj = Foo1() # obj= Foo2()   obj = Foo3()
				func(obj)
				"""
			
			java
				class Son(list):
					pass 
				
				class Son1(list):
					pass 
				
				# 以后传参时,arg可以是:list类的对象/list任何子类的对象
				public void func(list arg){
					print(arg)
				}
				
				# obj = list()
				# obj = Son()
				obj = Son1()
				func(obj)
			
重点:
	1. 编写方式执行流程
	
	2. 如何归类?
		反向:归类+提取公共值
		正向:类相关的功能+提取公共值
		
	3. 三大特性
		
作业:练习题 
		
			
			
			
			
			
			
			
			
			
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	