回顾jquery


1 选择器
    基本选择器 ：  $("#c1")   $(".c1")   $("p")   $("*")
	组合选择器 ：  $(".c1 p") $(".c1>p") $("div,p")  $("div[alex='123']")
    属性选择器 ：  $("[alex='123']")   $("[name='123']")
	表单选择器 ：  $(":radio")
	筛选器：
	         $(".c1").eq(索引)
	         $(".c1").first()
	         $(".c1").last()
	         $(".c1").even()
	         $(".c1").odd()
			 
			 $("#c1").hasclass("c1")
			 
2 绑定事件
    dom.on事件=function(){
	   //  this ： 当前事件触发标签
	}
	
	jquery对象.事件(function(){
	   //   $(this):当前事件触发标签
	})


forms组件：

 
    1 校验数据
	2 页面显示错误信息
	3 渲染页面和重置数据
	
	
	from django import forms

	class BookForm(forms.Form):
		title=forms.CharField(max_length=32)
		price=forms.IntegerField()
		email=forms.EmailField()
	
	应用语法：
		fm=BookForm({"titles":"yuan","price":123,"email":"123@qq.com"})
		fm.is_valid()    #判断是否符合规定返回布尔值
		False
		fm=BookForm({"price":123,"email":"123@qq.com"})
		fm.is_valid()
		False
		fm.errors    #返回错误的字段和错误原因
		{'title': ['This field is required.']}
		fm=BookForm({"titles":"yuan","price":123,"email":"123@qq.com","abd":123})
		fm=BookForm({"title":"yuan","price":123,"email":"123@qq.com","abc":123})
		fm.is_valid()
		True
		fm.errors
		{}
		fm.cleaned_data    #显示符合规格的字段
		{'title': 'yuan', 'price': 123, 'email': '123@qq.com'}
		fm=BookForm({"titles":"yuanhsgdgfsdjfsdsdlkjlksjdfjllksdflksdfsdfhlkjlksjdflkjlks","price":123,"email":"123@qq.com","abd":123})
		fm=BookForm({"title":"yuanhsgdgfsdjfsdsdlkjlksjdfjllksdflksdfsdfhlkjlksjdflkjlks","price":123,"email":"123@qq.com","abd":123})
		fm.is_valid()
		False
		fm.errors
		{'title': ['Ensure this value has at most 32 characters (it has 58).']}
		fm=BookForm({"title":"yuan","price":"123","email":"123"})
		fm.is_valid()
		False
		fm.errors
		{'email': ['Enter a valid email address.']}
		fm=BookForm({"title":"yuan","price":"123abc","email":"123"})
		fm.is_valid()
		False
		fm.errors
		{'price': ['Enter a whole number.'], 'email': ['Enter a valid email address.']}
		fm=BookForm({"title":"yuan","price":123,"email":"123"})
		fm.is_valid()
		False
		fm.errors
		{'email': ['Enter a valid email address.']}
		fm.cleaned_data
		{'title': 'yuan', 'price': 123}
		fm=BookForm({"titles":"yuan","price":123,"email":"123"})
		fm.is_valid()
		False
		fm.errors
		{'title': ['This field is required.'], 'email': ['Enter a valid email address.']}
		fm=BookForm({"title":"yuan","price":123,"email":"123@163.com","abc":123})
		fm.is_valid()
		True
		fm.errors
		{}
    


登录示例：
    用户名长度不能低于5位
    密码必须是纯数字
	邮箱必须符合邮箱格式
	如果输入数据格式有问题，显示给用户

	
	
    











	

	
作业：
    1 图书管理系统的添加基于Ajax实现
    




