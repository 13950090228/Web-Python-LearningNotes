
Django回顾

1 web应用
   本质是基于socket实现的应用程序
   
   浏览器-----------服务器
   
2 http协议：应用层协议
    1 基于TCP协议
	2 基于请求响应
	3 短连接
	4 无状态保存（引入了cookie,session技术）
	     
                  请求协议
 		  浏览器----------->服务器
                <------------
				  响应协议
 
	请求协议
	    ''
		请求首行      GET   path?get数据   HTTP/1.1
		请求头 		
		userAgent: win Chorome/IPhone 
		contentType:json   application/x-www-form-urlencoded
		空行
		请求体(post才有请求体)
		a=1&b=2
		{"a":1,"b":2}
		''
			
		如何给服务器发送json数据
		    给服务器发送请求方式：
			      1 地址栏     get请求
				  2 form表单   get   post请求  (无法发送json数据)
				  3 a标签连接请求    get请求
				  4 Ajax请求   get(查)  post(提交数据添加记录)  put(更新)  delete(删除) ......
				        
						$.ajax({
						     url:"/index/",
							 type:"post",
							 data:{
							    a:1,
								b:2
							 },  # 默认urlencoded编码
							 success:function(res){
							 
							 
							 }
						
						})
						
						
						发送json数据
						
						$.ajax({
						     url:"/index/",
							 type:"post",
							 contentType:"json"
							 data:JSON.stringfy({
							    a:1,
								b:2
							 }), 
							 success:function(res){
							     
							 
							 }
						
						})
						
						
						
						注意：Django解析不了json数据，只能自己利用request.body解析
						
						       
			
	响应协议
	        响应首行    HTTP/1.1  200  OK
			响应头
            contentType:"json"
			...
            空行
            响应体	

            响应状态码：
			          1开头： 请求中
                      200：请求成功
                      3开头：重定向
                      4： 文件路径找不到
                      5：服务器错误					  
                     
					 
					 
					 
Django  
    
    MTV+url路由分发：
        M： model.py   		
	    T:  Template:存放模板文件
        V： 视图 逻辑
    		
    					 
	
url路由分发：

        反向解析：
		        url(r'^role/add/$', views.role, name='role_add'),
                url(r'^role/edit/(\d+)/$', views.role, name='role_edit'),
		
		       视图：
			        
			        path=reverse("role_add")  # "role/add/"
			        path=reverse("role_edit",args=(1,2))  # "role/edit/1/"
			   
			   
			   模板：
			       {% url 'role_add' %}
			       {% url 'role_edit' 2 %}
           

        名称空间：
		    re_path(r'^app01/', include(("app01.urls","app01"),namespace="app01",)),


视图函数：
        
		request对象：存储这次请求所有请求信息：
			   属性：
				 HttpRequest.GET
				 HttpRequest.POST
							---- urlencoded编码
							---- 注意：键值对的值是多个的时候,比如checkbox类型的input标签，select标签，需要用：
										request.POST.getlist("hobby")					
				 HttpRequest.body 一个字节串，代表请求报文的主体。
				 HttpRequest.path
				 ttpRequest.method
				 HttpRequest.META  请求头
				 HttpRequest.FILES
				 HttpRequest.COOKIES
				 HttpRequest.session    session中间件 源码
				 HttpRequest.user       认证中间件 源码
				 
			   方法：	 
				  HttpRequest.get_full_path()	
				  HttpRequest.is_ajax()			 
			 
        HttpResponse对象：
		        obj=HttpResponse("hello")
		        obj=render(request,"index.html")
		        obj=redircet("/index/")
				
							
		FBV与CBV ： ******源码流程
		
			views：
				  from django.views import View
				  class BookView(View):
						
						def get(self,request):
								pass

						def post(self,request):
								pass								
			urls.py:
				   url("books",BookView.as_view())		



模板层：
        
		含有模板语法的html文件成为模板文件
		render方法渲染引擎
		模板语法：
		     
			{{}}：渲染变量
			      ---- 深度查询 句点符. 注意:  .无参方法
                  ---- 过滤器 date,safe,add,slice,
            {% %}：渲染标签			
			     {%for i in [111,222,333]%}
					   {%if i!= 222%}
						   <p>i</p>
					   {%endif%}
				 {%endfor%}	

            自定义标签和过滤器 
                  1、在settings中的INSTALLED_APPS配置当前app，不然django无法找到自定义的simple_tag.			
                  2、 在app中创建templatetags模块(模块名只能是templatetags)
                  3、 创建任意 .py 文件，如：my_tags.py
				            from django import template			 
							register = template.Library()   #register的名字是固定的,不可改变
							 							 
							@register.filter
							def filter_multi(v1,v2):
								return  v1 * v2
								
							@register.simple_tag
							def simple_tag_multi(v1,v2):
								return  v1 * v2


                   4、模板中使用：
				            {% load my_tags %}  
      
							# num=12
							{{ num|filter_multi:2 }} #24
							 
							{{ num|filter_multi:"[22,333,4444]" }}



            继承 extend：
			        创建base.html:
					    构建钩子
						{%block css%}
						    
						{%endblock css%}
						
						{%block content%}
						    <p>123</p>
						{%endblock%}
						
						{%block js%}
						    
						{%endblock js%}
                    子模板继承：
					     {%extends 'base.html' %}
						 
						 {%block content%}
						    <p>111</p>
						 {%endblock%}

ORM:
    class  Book(model.Model):
	     title=models.CharFiled(max_length=32)
		 


        类-----------------表    #  Book------- app01_book
        属性变量-----------字段  #  title------ title
        属性对象-----------约束	 #  models.CharFiled(max_length=32)
        类实例对象---------表记录 


    单表操作
	
	        model的元类信息：
			     Book._meta.verbose_name
				 '书籍'
				 Book
				 <class 'app01.models.Book'>
				 Book._meta.model_name
				 'book'
				 Book._meta.app_label
				 'app01'
                class Book(models.Model):
					title=models.CharField(max_length=32,verbose_name="书籍名称")


					 def __str__(self):
						return self.title
					 class Meta:
							app_label="APP01"
							db_table="app01book"
							unique_together=["title","price"]
							verbose_name="书籍"
							ordering=["price"]    
           
		   
		   class Book(models.Model):
					 id=models.AutoField(primary_key=True)
					 title=models.CharField(max_length=32)
					 state=models.BooleanField()
					 pub_date=models.DateField()
					 price=models.DecimalField(max_digits=8,decimal_places=2)
					 publish=models.CharField(max_length=32)
						   
		   
		   更多参数：
		            (1)null
 
					如果为True，Django 将用NULL 来在数据库中存储空值。 默认值是 False.
					 
					    blank
					 
					如果为True，该字段允许不填。默认为False。
					要注意，这与 null 不同。null纯粹是数据库范畴的，而 blank 是数据验证范畴的。
					如果一个字段的blank=True，表单的验证将允许该字段是空值。如果字段的blank=False，该字段就是必填的。
					 
					(2)default
					 
					字段的默认值。可以是一个值或者可调用对象。如果可调用 ，每有新对象被创建它都会被调用。
					 
					(3)primary_key
					 
					如果为True，那么这个字段就是模型的主键。如果你没有指定任何一个字段的primary_key=True，
					Django 就会自动添加一个IntegerField字段做为主键，所以除非你想覆盖默认的主键行为，
					否则没必要设置任何一个字段的primary_key=True。
					 
					(4)unique
					 
					如果该值设置为 True, 这个数据字段的值在整张表中必须是唯一的
					 
					(5)choices
					由二元组组成的一个可迭代对象（例如，列表或元组），用来给字段提供选择项。 如果设置了choices ，默认的表单将是一个选择框而不是标准的文本框，<br>而且这个选择框的选项就是choices 中的选项。
			

            数据库配置：
			    DATABASES = {
					'default': {
						'ENGINE': 'django.db.backends.mysql',
						'NAME':'bms',     　　 　  # 要连接的数据库，连接前需要创建好
						'USER':'root',　　　　　　  # 连接数据库的用户名
						'PASSWORD':'',　　　　　　  # 连接数据库的密码
						'HOST':'127.0.0.1',       # 连接主机，默认本级
						'PORT'：3306    　　　     #  端口 默认3306
					}，
					
					'app01': {
						'ENGINE': 'django.db.backends.mysql',
						'NAME':'bms',     　　 　  # 要连接的数据库，连接前需要创建好
						'USER':'root',　　　　　　  # 连接数据库的用户名
						'PASSWORD':'',　　　　　　  # 连接数据库的密码
						'HOST':'127.0.0.1',       # 连接主机，默认本级
						'PORT'：3306    　　　     #  端口 默认3306
					}，
					
				}
			
            针对每一个注册app下的models.py创建对应的表结构			
				python manage.py makemigrations
				python manage.py migrate
		   
		   添加记录：
		        book_obj=Book.objects.create(title="python葵花宝典",state=True,price=100,publish="苹果出版社",pub_date="2012-12-12")
		        
				book_obj=Book(title="python葵花宝典",state=True,price=100,publish="苹果出版社",pub_date="2012-12-12")
                book_obj.save()
		     
		   查询表纪录：
                <1> all():                  查询所有结果
  
				<2> filter(**kwargs):       它包含了与所给筛选条件相匹配的对象
				  
				<3> get(**kwargs):          返回与所给筛选条件相匹配的对象，返回结果有且只有一个，
											如果符合筛选条件的对象超过一个或者没有都会抛出错误。
				  
				<4> exclude(**kwargs):      它包含了与所给筛选条件不匹配的对象
				 
				<5> order_by(*field):       对查询结果排序
				  
				<6> reverse():              对查询结果反向排序
				  
				<8> count():                返回数据库中匹配查询(QuerySet)的对象数量。
				  
				<9> first():                返回第一条记录
				  
				<10> last():                返回最后一条记录
				  
				<11> exists():              如果QuerySet包含数据，就返回True，否则返回False
				 
				<12> values(*field):        返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列
											model的实例化对象，而是一个可迭代的字典序列
											
											
											Book.objects.filter(price__gt=100).values("title","price")
											'''
											queryset=[]
											for obj in Book.objects.filter(price__gt=100):
											    queryset.append({
												    "title":obj.title,
													"price":obj.price
												
												})
											
											'''
											
				<13> values_list(*field):   它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列
				                            
												Book.objects.filter(price__gt=100).values("title","price")
											'''
											queryset=[]
											for obj in Book.objects.filter(price__gt=100):
											    queryset.append((
												    obj.title,
													obj.price
												
												))
											
											'''
											
											
											
				<14> distinct():            从返回结果中剔除重复纪录		   

            基于双下划线的模糊查询
			    Book.objects.filter(price__in=[100,200,300])
				Book.objects.filter(price__gt=100)
				Book.objects.filter(price__lt=100)
				Book.objects.filter(price__range=[100,200])
				Book.objects.filter(title__contains="python")
				Book.objects.filter(title__icontains="python")
				Book.objects.filter(title__startswith="py")
				Book.objects.filter(pub_date__year=2012)
				Book.objects.filter(pub_date__year__gt=2012)
			
			
			
			删除表纪录
			    Book.objects.filter(price__in=[100,200,300]).delete()
			    Book.objects.get(pk=1).delete()
			     
			
			修改表纪录
			    # 方式1
			    Book.objects.filter(title__startswith="py").update(price=120)
				# 方式2
				book=Book.objects.filter(title__startswith="py").first()
			    book.price=1000
				book.save()
				
				
	多表操作
            from django.db import models

			# Create your models here.


			class Author(models.Model):
				nid = models.AutoField(primary_key=True)
				name=models.CharField( max_length=32)
				age=models.IntegerField()

				# 与AuthorDetail建立一对一的关系
				authorDetail=models.OneToOneField(to="AuthorDetail",on_delete=models.CASCADE)

			class AuthorDetail(models.Model):

				nid = models.AutoField(primary_key=True)
				birthday=models.DateField()
				telephone=models.BigIntegerField()
				addr=models.CharField( max_length=64)

			class Publish(models.Model):
				nid = models.AutoField(primary_key=True)
				name=models.CharField( max_length=32)
				city=models.CharField( max_length=32)
				email=models.EmailField()
				'''
				    create table app01_publish（
					   nid   INT auto_increment primary key
					   name  varchar(32)
					   city  varchar(32)
					   email varchar(32)
					
					）
				
				'''


			class Book(models.Model):

				nid = models.AutoField(primary_key=True)
				title = models.CharField( max_length=32)
				publishDate=models.DateField()
				price=models.DecimalField(max_digits=5,decimal_places=2)

				# 与Publish建立一对多的关系,外键字段建立在多的一方
				publish=models.ForeignKey(to="Publish",to_field="nid",on_delete=models.CASCADE)
				# 与Author表建立多对多的关系,ManyToManyField可以建在两个模型中的任意一个，自动创建第三张表
				authors=models.ManyToManyField(to='Author',)
	            '''
				    create table app01_book（
						   nid   INT auto_increment primary key
						   title  varchar(32)
						   publishDate  date
						   price decimal(5,2)
					       publish_id  INT
						   ForeignKey publish_id references Publish(nid)
					）
					
					
					create book_authors(
					     id   INT auto_increment primary key
					     book_id INT
                         ForeignKey book_id references app01_book(nid)

                         author_id INT
                         ForeignKey author_id references app01_author(nid)							 
					)
				
				'''


            1 添加记录
			   
			    针对一对多：
				       
                   book_obj=Book.objects.create(title="python葵花宝典",price=100,publishDate="2012-12-12"，publish_id=1)
				   
				   pub_obj=Publish.objects.get(pk=1)
                   book_obj=Book.objects.create(title="python葵花宝典",price=100,publishDate="2012-12-12"，publish=pub_obj)

      
                针对多对多：
				    
                          book_authors
						  
						      id  book_id    author_id
							  
							   4    2           3
							   5    1           4

                         book=Book.objects.get(pk=1)
                         book.authors.add(1,2,3)
						 
						 book=Book.objects.get(pk=2)
                         book.authors.add(3)
						 
						 book=Book.objects.get(pk=1)
						 book.authors.remove(2,3)
                        
						 book=Book.objects.get(pk=1)
						 book.authors.clear()
						
						 book=Book.objects.get(pk=1)
						 book.authors.set([4,5]) # 列表不打散


            2   补充中介模型
			
			
			    场景：
				    student
					   id   name
					    1    A
					    1    B
					   
					course
                        id   name					 
					     1    python
						 2    linux
				   
				
				    score
					
					     id      student_id        course_id    score
			              1            1                1         78
			              2            1                2         67
						  
						  
						  
					class  Score(models.Model):
					       student=ForeignKey("Student")
					       course=ForeignKey("Course")
						   score=models.IntegerField()
						   
						   
						   
					   
					# 中介模型方式：
					        
							
							class Student(models.Model):
							    name = models.CharField( max_length=32)
								courses=models.ManyToManyField("Courses",through="Score")
								
							class Course(models.Model):
							    name = models.CharField( max_length=32)	
																
							class Score(models.Model):
							     student=models.ForeignKey("Student")
							     course=models.ForeignKey("Course")
							     score=models.IntegerField()
								 
								 
			3 跨表查询
                    class Book(models.Model):

						nid = models.AutoField(primary_key=True)
						title = models.CharField( max_length=32)
			
						# 与Publish建立一对多的关系,外键字段建立在多的一方
						publish=models.ForeignKey(to="Publish",to_field="nid",relate_name="xxx",on_delete=models.CASCADE)
						# 与Author表建立多对多的关系,ManyToManyField可以建在两个模型中的任意一个，自动创建第三张表
						authors=models.ManyToManyField(to='Author',)
                    ####################   基于对象（子查询）
                    
                    正向查询按字段，反向查询relate_name,如果没有设置，按表名小写_set
                    
						book=Book.objects.get(pk=1)
						book.publish
						book.authors.all()
						
						
						pub=Publish.objects.get(pk=1)
						pub.xxx.all()
						
						
						author=Author.objects.get(pk=1)
						author.book_set.all()
						
						author.authordetail
						authordetail.author
					
				
                    ####################   基于双下划线（join查询）

                        id  title  pub_id
						 1     A      1
						 2     B      1
						 
						 
						 Publish
						 id   name
						  1   人民
						  2   北京

						 innerjoin

							1     A      1   1   人民
							2     B      1   1   人民

						 rightjoin
							1   人民      1     A      1
							1   人民      2     B      1
							2   北京      null  null   null
                         
						 
						 
						    book_authors
						  
						      id  book_id    author_id
							  
							   1    1           1
							   2    2           1 
							   2    3           1 
							   3    3           2
					  
					正向查询安字段，反向查询按表名小写  

                    # 查询python出版社的名字
                    Book.objects.filter(title="python").values("publish__name")	
                    Publish.objects.filter(book__title="python").values("name")					

                    # 查询alex出版过的书籍的名称
					
					Author.objects.filter(name__startswith="a").values("book__title")
					Book.objects.filter(authors__name__startswith="a")
            
			
			4 分组查询（基于双下划线（join查询））
			        聚合
					# 计算所有图书的平均价格
						Book.objects.all().aggregate(AVG("price"))
						Book.objects.all().aggregate(MAX("price"))
					分组：
					    id  name age   salary    dep
						1   alex  12   2000     销售部
						2   egon  22   3000     人事部
						3   wen   22   5000     人事部
						
						
						sql:select dep,AVG(salary)  from  emp  group by  dep
						
						orm:Emp.objects.values("dep").annotate(avg=AVG("salary")) # [{"dep":"销售","avg":5000},{}]	 					
					
			    
	                跨表分组查询
					    
						book
						
						id   title     pub_id
						 1   python       1
						 2   linux        1
						 3   go           2
						 
						 
						 publish
						 
						 id   name
						  1   沙河
						  2   北京
						  
						 
						
						
						查询每一个出版社的名称以及出版书籍的个数
						
						id   title     pub_id      id   name
						 1   python       1        1    沙河
						 2   linux        1        1    沙河
						 3   go           2        2    北京
						 
						 
				        Publish.objects.values(pk).annotate(c=Count("book")) # [{pk:1,c:2},{pk:2,c:1}]
				        Publish.objects.all.annotate(c=Count("book")).values("c","name") # [publish_obj,publish_obj]
			            
						
						# 查询每一个作者的名字以及出版书籍的最高价格
						Author.objects.annotate(max_price=Max("book__price")).values("name","max_price")
						
						# 查询96年以后出生的每一个作者的名字以及出版书籍的最高价格
						Author.objects.filter(birthday__year__gt=1996).annotate(max_price=Max("book__price")).values("name","max_price")
						
						# 查询不止一个作者的书籍名称以及关联的作者个数
						Book.objects.all().annotate(c=Count("authors"))# [book1,book2,.....]
						Book.objects.all().annotate(c=Count("authors")).filter(c__gt=1).values("title","c")
						
						# 查询每一个销售的名字以及今天对应的成单量
						userinfo
						   id   name
						    1   sanjiang
							2   jinjin
							3   bingbing
							
						customer
                            id    name  deal_date       consultant
							 1     A    2018-11-23          1
							 1     B    2018-11-22          1
							 1     C    2018-11-23          2
							 1     D    2018-11-18          1
							 1     E    2018-11-23          1
							 1     F    2018-11-23          1
							 1     Q    2018-11-23          1
                           							
						customer
                            id    name  deal_date       consultant      id    name
							 1     A    2018-11-23          1            1   sanjiang
							
							 1     C    2018-11-23          2            2   jinjin
							
							 1     E    2018-11-23          3            3   bingbing
							 1     F    2018-11-23          3            3   bingbing
							 1     Q    2018-11-23          1            1   sanjiang
						
						
						
						# Userinfo.objects.filter(depart_id=1).filter(customer__deal_date=now).annotate(c=Count("customers")).values("name","c")
						
		    F与Q
			
				 Book.objects.filter(commnetNum__lt=F('keepNum'))
				 Book.objects.filter(commnetNum__lt=F('keepNum')*2)   			
				 Book.objects.all().update(price=F("price")+30)　			
				 
				 Book.objects.filter(Q(title__startswith="py")|Q(price__gt=100))
				 
				 q=Q()
				 q.conector="or"
				 q.children.append(("title__startswith","py"))
				 q.children.append(("price__gt",100))
				 
				 
				 
				 
Django组件：
        1 文件上传
		        form表单
				        <form action="/file_put/" method="post" enctype="multipart/form-data">
							姓名<input type="text" name="user">
							文件<input type="file" name="file_obj">
							<input type="submit">
						</form>
				    
				
				ajax形式
				
				        <div>
							姓名<input type="text" id="user">
							文件<input type="file" name="file_obj" id="file">
							<input type="button" class="filebtn" value="提交">
							<p class="msg"></p>
						</div>
						
						
						// 发送文件
						  $(".filebtn").click(function () {


							  var formdata=new FormData();
							  formdata.append("file_obj",$("#file")[0].files[0]);
							  formdata.append("user",$("#user").val());

							  $.ajax({
								  url:"/file_put/",
								  type:"post",

								  // Ajax上传文件必备参数
								  processData: false ,    // 不处理数据
								  contentType: false,    // 不设置内容类型

								  data:formdata,
								  success:function (response) {
									  console.log(response);
									  if (response=="OK"){
										  $(".msg").html("提交成功！")
									  }
								  }
							  })
							  
						  })
										
				
				
				视图： 
				     def file_put(request):

							print(request.POST)
							print(request.FILES)
							file_obj=request.FILES.get("file_obj")
							# 文件对象有一个name属性，获取文件名称字符串
							print(file_obj.name)
							path=file_obj.name

							path=os.path.join(settings.BASE_DIR,"media","img",path)
							with open(path,"wb") as f:
								for line in file_obj:
									f.write(line)


							return HttpResponse("OK")
					
		2 cookie session auth
		        cookie概念：
				       针对每一个服务器，保存在客户端（浏览器）的一个key-value结构数据，可以理解成一个字典结构
	        	cookie语法：
				       obj=HttpResponse()
					   obj=render()
					   obj=redirect()
				       # 设置cookie
				       obj.set_cookie("key","value",3600*24)
		               # 获取cookie
					   request.COOKIES
					   # 删除cookie
					   obj.delete_cookie("key","value")
		
		
		        应用：
				    登录认证
					验证码
					保存上次访问时间
					浏览过的商品
				
                session语法：
				    
					  
					  # 设置session
					  
					  request.session["key"]="value"
					       '''
						    if request.cookie("session_id"):
							    1 获取随机字符串session_id：21342saidf92349
								2 去django-seeson表中过滤session-key=21342saidf92349的记录
									session-key         session-data
									21342saidf92349    {"key":"value"}
								3 更新：
                            else:							
						   
						   
								1 生成一个随机字符串：21342saidf92349
								2 去django-seeson表中创建一条记录
									session-key         session-data
									21342saidf92349    {"key":"value"}
								3 响应setcookie("session_id",21342saidf92349)
						   '''
					  # 获取session
					       request.seesion["key"]
						   '''
						     1 获取cookie中key为session_id的对应值：21342saidf92349
							 2 去django-session表中过滤session-key=21342saidf92349的记录对象obj
							 3 obj.session-data.get("key"")
						   
						   '''
				
				       
              	
		
		3 form  modelform   modelformset
        4 中间件
			 
类装饰器
	imageField
	FileField
	media
	
数据库备份命令


https://www.cnblogs.com/yuanchenqi/articles/6755717.html				   