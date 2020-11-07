1.函数式编程和面向对象的对比

	a.开发一个消息提醒的功能（邮件/短信/微信）
	
	对比：
		函数：定义简单/调用简单
		面向对象：定义复杂/使用复杂  好处：归类，将某些类似函数写一起
		
	总结：
		1.函数式编程可能会比面向对象好
		2.python支持两种编程方式
		3.面向对象方式格式：
			定义：
				class 
    面向对象
		class Message:
			def email(self,mail):
				print(mail)
			
			def tel(self,num):
				print(num)
				
			def msg(self):
				print('短信')
        
			obj=Message()
			obj.email('506713537')
			obj.tel('13950090228')
			obj.msg()

   函数式
		def email(mail):
				print(mail)
			
		def tel(num):
			print(num)
			
		def msg():
			print('短信')

		email('506713537')
		tel('13950090228')
		msg()