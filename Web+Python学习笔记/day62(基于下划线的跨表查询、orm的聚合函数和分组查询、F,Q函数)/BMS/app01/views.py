from django.shortcuts import render,HttpResponse,redirect
from app01.models import Book,Publish,Author,Emp,AuthorDetail
from django.db.models import Avg,Sum,Max,Min,Count,F,Q
import json
from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage
from django.core.exceptions import ValidationError
from django.forms import widgets
# Create your views here.
# class BookForm(forms.Form):
#     title = forms.CharField(max_length=32)
#     price = forms.IntegerField()
#     pub_date = forms.DateField(widget=widgets.TextInput(attrs={"type":"date"}))
#     publish = forms.ModelChoiceField(queryset=Publish.objects.all())
#     authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
#
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         for filed in self.fields.values():
#             filed.widget.attrs.update({"class":"form-control"})

class BookModelForm(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"
        # fields=["title","price"]

        exclude=["comment_count","poll_count"]
        labels={
            "title":"书籍名称",
            "price":"价格",
            "pub_date":"出版日期",
            "publish":"出版社",
            "authors":"作者",
        }
        # error_messages={
        #     "title":{"required":"此项不能为空"}
        # }
        widgets={
            "pub_date":widgets.TextInput(attrs={"type":"date"})
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for filed in self.fields.values():
            filed.widget.attrs.update({"class":"form-control"})
            filed.error_messages={"required":"此项不能为空"}




def addrecord(request):
    """
    添加方式
    """
    #一对多的添加方式
    # publish_obj=Publish.objects.get(nid=1)
    # book = Book.objects.create(
    #     title='Web开发',
    #     price=111,
    #     pub_date='2012-12-12',
    #     publish_id=1,   #方法一
    #     # publish=publish_obj   方法二
    # )

    #多对多的添加方式
    #方式一
    # a = Author.objects.filter(name='刘永祺').first()
    # b = Author.objects.filter(name='大鸡哥').first()
    # book.authors.add(a,b)
    # 方式2：
    # book.authors.add(1,2)
    # 方式3：
    # book.authors.add(*[1,2])
    # a = Author.objects.filter(name='刘永祺').first()
    # book = Book.objects.filter(nid=20).first()
    # book.authors.remove(a)
    # book.authors.remove(2)  #清除book_id=20,author_id=2的记录
    # book.authors.clear()  # 清除book_id=20的所有记录
    #
    # ###### 解除再绑定,效果相当于先clear再add
    # book.authors.set(1)

    return HttpResponse('成功')

def query(request):
    #基于对象的跨表查询

    #一对多的查询
    #查询python这本书的出版社和emailw
    # book = Book.objects.filter(title='python')[0]
    # print(book.publish.name)    #publish是在models中建表设置的字段
    # print(book.publish.email)

    #查询苹果出版社出版的所有书
    # pub_obj = Publish.objects.filter(name='苹果出版社')[0]
    # print(pub_obj.book_set.all().values('title','price'))  #返回queryset

    #多对多的查询
    '''
            正向查询按字段 book.authors.all()
        Book -------------------------------->Author
             <--------------------------------
            反向查询按表名小写_set.all(): alex.bok_set.all()
    '''
    #查询python这本书的作者的年龄
    # book = Book.objects.filter(title='python')[0]
    # ret = book.authors.all().values('name','age')
    # print(ret)

    #查询刘永祺出版过的所有书籍
    # author = Author.objects.filter(name='刘永祺')[0]
    # ret = author.book_set.all()
    # print(ret)

    ####### 一对一 ##########
    '''
                     正常查询安字段：alex.ad
        Author -----------------------------------------> AuthorDetail
               <------------------------------------------
                     反向查询按表名小写  ad.author
    '''
    #查询刘永祺的手机号
    # lyq = Author.objects.filter(name='刘永祺')[0]
    # print(lyq.ad.tel)

    #查询手机号为1111的人
    data = AuthorDetail.objects.filter(tel=1111)[0]
    print(data.author.name)






    return HttpResponse('成功')

def query2(request):
    #基于双下划线的跨表查询(基于join实现)

    #一对多的查询
    #查询python这本书的出版社和email
    # 正查
    # ret = Book.objects.filter(title='python').values('publish__name','publish__email')
    # print(ret)
    #反查
    # ret = Publish.objects.filter(book__title='python').values('name','email')

    #查询苹果出版社出版的所有书
    # ret = Publish.objects.filter(name='苹果出版社').values('book__title')

    # ret = Book.objects.filter(publish__name='苹果出版社').values('title')
    # print(ret)

    #查询python这本书的作者的年龄
    # ret = Book.objects.filter(title='Web开发').values('authors__age')
    # ret = Author.objects.filter(book__title='python').values('age')
    # print(ret)

    #查询刘永祺出版过的所有书籍
    # ret = Author.objects.filter(name='刘永祺').values('book__title')
    # ret = Book.objects.filter(authors__name='刘永祺').values('title')
    # print(ret)

    #查询刘永祺的手机号
    # ret = Author.objects.filter(name='刘永祺').values('ad__tel')
    # ret = AuthorDetail.objects.filter(author__name='刘永祺').values('tel')
    # print(ret)

    #查询手机号为1111的人
    # ret = AuthorDetail.objects.filter(tel=1111).values('author__name')
    # ret = Author.objects.filter(ad__tel=1111).values('name')
    # print(ret)

    #查看苹果出版社出版的所有书籍的名字和作者的姓名
    # ret = Publish.objects.filter(name='苹果出版社').values('book__title','book__authors__name')

    #查看手机号为1111开头的作者出版过的所有书籍名称以及出版社名
    # ret = AuthorDetail.objects.filter(tel__startswith=22).values('author__book__title','author__book__publish__name')
    # print(ret)

    #聚合函数
    #查所有书籍平均价格
    # ret = Book.objects.all().aggregate(Avg('price'))  #返回一个字典{'price__avg': Decimal('105.333333')}
    #aggregate(priceAvg=Avg('price')）  将键值 'price__avg'改成'priceAvg'
    #查所有书籍个数
    # ret = Book.objects.all().aggregate(Count('nid'))
    # print(ret)

    #分组
    #单表分组查询
    #key: annotate()前values哪一个字段就按拿一个字段group by
    #查询书籍表每一个出版社id以及对应的书籍个数
    # ret = Book.objects.values('publish_id').annotate(num=Count(1))
    # print(ret)

    #查询每一个部门的名称以及对应员工的平均薪水
    # ret = Emp.objects.values('dep').annotate(avg=Avg('salary'))
    # print(ret)

    #查询每一个省份的人称以及对应的员工人数
    # ret = Emp.objects.values('pro').annotate(num=Count(1))
    #查询每一个省份的人称以及对应的最大年龄
    # ret = Emp.objects.values('pro').annotate(max_age=Max('age'))
    # print(ret)

    #跨表查询
    #1 查询每一个出版社的名称和对应的的书籍平均价格
    #方式一
    # ret = Publish.objects.values('name').annotate(avg_price=Avg('book__price'))
    #方式二
    # ret = Publish.objects.all().annotate(avg_price=Avg('book__price')).values('name','avg_price')
    #方式三
    # ret = Publish.objects.annotate(avg_price=Avg('book__price')).values('name', 'avg_price','email')

    #方式二等于方式三


    #2 查询每一个作者的名字以及出版书籍的最高价格
    # ret = Author.objects.values('name').annotate(max_price=Max('book__price'))

    # 3查询每一个书籍的名称和对应作者的个数
    # ret = Book.objects.values('title').annotate(author_num=Count('authors__name'))
    # ret = Book.objects.annotate(c=Count('authors')).values('title','c')
    # ret = Book.objects.annotate(c=Count('authors')).values('title','c')

    # 4 查询作者数不止一个的书籍名称以及作者个数
    # ret = Book.objects.annotate(c=Count('authors')).filter(c__gt=1).values('title','c')

    # 5 根据一本图书作者数的多少进行排序
    # ret = Book.objects.annotate(c=Count('authors')).order_by('c').values('title','c')

    # 6 统计以‘py’开头的书籍的作者的个数
    # ret = Book.objects.annotate(c=Count('authors')).filter(title__startswith='py').values('title', 'c')
    # print(ret)

    ##### F与Q查询 ############
    # 查询评论数大于点赞数的书的名字
    # ret = Book.objects.filter(comment_count__gt=F('poll_count'))

    # 查询评论数大于点赞数的书的名字
    # ret = Book.objects.filter(comment_count__gt=F('poll_count')*2)

    # 给每一本书价格多100块
    # ret = Book.objects.all().update(price=F('price')+100)

    # 查询价格大于205或者评论数小于等于3000的所有书籍
    # &与  |或   ~非   Q可以嵌套
    # ret = Book.objects.filter(Q(Q(price__gt=205)|Q(comment_count__gt=3000)) & Q(price__gt=200) )
    # print(ret)






    return HttpResponse('成功')
############图书管理系统##############3
def book_view(request):
    book_list = Book.objects.all()

    pag = Paginator(book_list,10)
    try:
        current_page_num = request.GET.get("pag",1)
        current_page_num = int(current_page_num)
        current_page = pag.page(current_page_num)
        val = (current_page_num - 1) * 10
    except EmptyPage as e:
        current_page = pag.page(1)
    user = request.user

    return render(request,'book_view.html',locals())


def book_add(request):
    if request.method == "GET":
        form = BookModelForm()
        return render(request,"book_add.html",locals())
    else:
        form = BookModelForm(request.POST)
        if form.is_valid():
            # authors = form.cleaned_data.pop("authors")
            # book = Book.objects.create(**form.cleaned_data)
            # book.authors.add(*authors)
            form.save()   #create
            return redirect("/book/")
        else:
            return render(request,"book_add.html",locals())
    # user = request.user
    # if request.method=='GET':
    #     publish_list = Publish.objects.all()
    #     author_list = Author.objects.all()
    #     return render(request,'book_add.html',locals())
    # else:
    #     title = request.POST.get('title')
    #     price = request.POST.get('price')
    #     pub_date = request.POST.get('pub_date')
    #     publish_id = request.POST.get('publish_id')
    #     author = request.POST.getlist('author')
    #
    #     book = Book.objects.create(title=title,price=price,pub_date=pub_date,publish_id=publish_id)
    #     book.authors.add(*author)
    #     return redirect('/book/')

def book_delete(request,del_book_id):
    Book.objects.filter(nid=del_book_id).delete()

    return redirect('/book/')


def book_edit(request,edit_book_id):
    # user = request.user
    edit_book = Book.objects.filter(pk=edit_book_id).first()
    if request.method == 'GET':
        # publish_list = Publish.objects.all()
        # author_list = Author.objects.all()
        form = BookModelForm(instance=edit_book)
        return render(request,'book_edit.html',locals())
    else:
        # title = request.POST.get('title')
        # price = request.POST.get('price')
        # pub_date = request.POST.get('pub_date')
        # publish_id = request.POST.get('publish_id')
        # author = request.POST.getlist('author')
        # Book.objects.filter(pk=edit_book_id).update(title=title, price=price, pub_date=pub_date, publish_id=publish_id)
        # edit_book.authors.set(author)
        form = BookModelForm(request.POST,instance=edit_book)
        if form.is_valid():
            form.save()
        else:
            return render(request,"book_edit.html",locals())

        return redirect('/book/')

def book_ajax_del(request,del_book_id):
    response = {"state":True}
    try:
        Book.objects.filter(nid=del_book_id).delete()
    except Exception as e:
        response = {"state": False}

    return HttpResponse(json.dumps(response))




def book_ajax_add(request):
    response = {"state": '添加成功'}
    title = request.POST.get('title')
    price = request.POST.get('price')
    pub_date = request.POST.get('pub_date')
    author = request.POST.get('author')
    publish = request.POST.get('publish')

    p_res = Publish.objects.filter(name=publish).values('pid').first()
    a_res = Author.objects.filter(name=author).values('nid').first()

    if p_res == None:
        response = {"state": '没有这个出版社',"obj":'publish'}
        return HttpResponse(json.dumps(response))

    if a_res == None:
        response = {"state": '没有这个作者',"obj":'author'}
        return HttpResponse(json.dumps(response))

    book = Book.objects.create(title=title, price=price, pub_date=pub_date, publish_id=p_res.get("pid"))
    book.authors.add(a_res.get("nid"))

    return HttpResponse(json.dumps(response))

def login(request):
    if request.method == 'GET':
        return render(request,"login.html")
    else:
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")


        user_obj = auth.authenticate(username=user,password=pwd)
        auth.login(request,user_obj)
        if user_obj:
            #设置cookie
            obj = redirect('/book/')

            return obj
        else:
            return HttpResponse('fail')

def logout(request):
    '''
       1 request.COOKIE.get("sessionid")  :afgfwetewftqfqeg
       2 在django-session表过滤session-key=afgfwetewftqfqeg的记录删除
       3 response.delete_cookie("sessionid")
    '''
    # auth.logout(request)
    request.session.flush()
    return redirect('/login/')