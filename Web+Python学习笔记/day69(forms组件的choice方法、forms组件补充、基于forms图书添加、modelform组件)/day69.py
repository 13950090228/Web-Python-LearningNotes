
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

3 循环
        // 1 循环序列

		var arr=[12,34,5667];
		$.each(arr,function (i,j) {
			console.log(i,j)
		});

		var obj={"name":"alex","age":123}
		$.each(obj,function (i,j) {
			console.log(i,j)
		});

		// 2 循环标签

		$("ul li").each(function (i,j) {
			console.log(i,j);
			console.log($(this).html())
		})
  
	
3 操作标签

   1 文本控制
         $("#p3").html()	
		 $("#p3").text()
		 $("#p3").html("<a href>1111</a>")	
		 $("#p3").text("<a href>1111</a>")
	
   2 属性控制
		 attr(属性名称)   
		 attr(属性名称，属性值) 
         removeAttr()	
		  
         $("#p3").addClass("c3")
	     $("#p3").removeClass("c1")	

         三个标签有val方法
         input  
         textarea
         select

		 
		 
		 
crm

1 注册，登录
2 表结构，客户关系页面
    预备知识点：
	    1 modelForm
		2 CBV
		3 自定义分页
		
		
		
		
一 modelForm
    
	(1)  model的知识点：
			 class UserInfo(AbstractUser):
					tel=models.CharField(max_length=32)
					gender=models.IntegerField(choices=((1,"男"),(2,"女")),default=1)
			 
			 yuan=UserInfo.objects.get(pk=1)
			 yuan.get_gender_display()

    (2) modelform使用
	    model.py:
			class Book(models.Model):
				nid=models.AutoField(primary_key=True)
				title=models.CharField(max_length=32)
				price=models.DecimalField(max_digits=8,decimal_places=2) # 999999.99
				pub_date=models.DateTimeField()  # "2012-12-12"

				# comment_count=models.IntegerField(default=100)
				# poll_count=models.IntegerField(default=100)

				publish=models.ForeignKey(to="Publish",on_delete=models.CASCADE)  # 级联删除
				authors=models.ManyToManyField(to="Author")
				def __str__(self):
					return self.title
        form.py:
		       # 构建modelform
			   class BookModelForm(forms.ModelForm):
					class Meta:
						model=Book
						fields="__all__"
						
			   '''
			   BookModelForm等同于：
			        class BookForm(forms.Form):
							title=forms.CharField(max_length=32)
							price=forms.IntegerField()
							pub_date=forms.DateField(widget=widgets.TextInput(attrs={"type":"date"}))
							#publish=forms.ChoiceField(choices=[(1,"AAA"),(2,"BBB")])
							publish=forms.ModelChoiceField(queryset=Publish.objects.all())
							authors=forms.ModelMultipleChoiceField(queryset=Author.objects.all())
	  
			   '''
		        

        逻辑：
		    添加书籍：
			    def add(reqeust):
				     if GET请求：
					      form=BookModelForm()
						  return render(reqeust,{"form":form})
						  '''
						  渲染页面
						      <form action="" method="post" novalidate>
									{% csrf_token %}
									  {% for field in form %}
											<div class="form-group">
												 <label for="title">{{ field.label }}</label>
												 {{ field }}
												 <span>{{ field.errors.0 }}</span>
											</div>
									 {% endfor %}
									<input type="submit" value="提交" class="btn btn-default pull-right">
							  </form>
						  '''
					else POST请求：
					      form=BookModelForm(request.POST)
                          if form.is_valid():
						      form.save() # Book.objects.create(clean_data)
							  return redirect("/")
						  else:
						     return render(reqeust,{"form":form})
						       
      						  
				
			编辑书籍： 
               			
				def edit(request,id):
				        edit_obj=Book.objects.get(pk=id)
				        if GET请求：
					      form=BookModelForm(instance=edit_obj)
						  return render(reqeust,{"form":form})
						  '''
						  渲染页面同添加页面
						      
						  '''
					else POST请求：
					      form=BookModelForm(request.POST,instance=edit_obj)
                          if form.is_valid():
						      form.save() #  edit_obj.update(clean_data)
							  return redirect("/")
						  else:
						     return render(reqeust,{"form":form})


今天博客：
https://www.cnblogs.com/yuanchenqi/articles/7614921.html
https://www.cnblogs.com/yuanchenqi/articles/8034442.html#_label1		 
  

今日作业：
    基于modelForm实现crm的注册功能
	
	
预习分页：
    https://www.cnblogs.com/yuanchenqi/articles/7652353.html

