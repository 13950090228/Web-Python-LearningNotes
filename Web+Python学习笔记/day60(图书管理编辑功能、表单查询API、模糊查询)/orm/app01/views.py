from django.shortcuts import render,HttpResponse,redirect
import datetime
from app01.models import Book
from django.urls import reverse
# Create your views here.
def addbook(request):
    """
    添加表记录

    """

    now = datetime.datetime.now()
    # 方式1
    # book = Book(title="西游记",price=50,pub_date=now,publish="人民出版社")
    # book.save()

    #方式2
    # Book.objects.create(title="Web开发",price=250,pub_date=now,publish="清华大学出版社")
    if request.method == "POST":
        # title = request.POST.get("title")
        # price = request.POST.get("price")
        # pub_date = request.POST.get("pub_date")
        # publish = request.POST.get("publish")
        # book = Book.objects.create(title=title,price=price,pub_date=pub_date,publish=publish)

        data = request.POST.dict()   #把request.POST转成字典
        del data["csrfmiddlewaretoken"]
        book = Book.objects.create(**data)  #把data打散传入

        return redirect(reverse("books"))
    else:
        return render(request,"addbook.html")

def showbooks(request):
    book_list = Book.objects.all()
    # print(book_list)  #[obj1,obj2,obj3...]
    # print(book_list[0].title)
    return render(request, "books.html",locals())

def delbook(request,del_book_id):
    Book.objects.filter(id=del_book_id).delete()

    return redirect(reverse('books'))

def editbook(request,edit_book_id):
    if request.method == "GET":
        editbook = Book.objects.filter(id=edit_book_id)[0]
        return render(request,"editbook.html",locals())

    else:

        title = request.POST.get("title")
        price = request.POST.get("price")
        pub_date = request.POST.get("pub_date")
        publish = request.POST.get("publish")
        Book.objects.filter(id=edit_book_id).update(title=title,
                                                     price=price,
                                                     pub_date=pub_date,
                                                     publish=publish)
        print(Book.objects.filter(id=edit_book_id))
        return redirect(reverse("books",args=()))  #若地址含动态参数则往args填值

def query(request):
    """
    注意：querySet和model的区别
    """
    #===================单表查询=======================
    #1 all() 方法
    # ret = Book.objects.all()
    # print(ret)  #<QuerySet [<Book: python语言程序设计>, <Book: GO语言入门>, ....

    #2 filter() 方法
    # ret = Book.objects.filter(price=100)
    # print(ret)

    #3 get方法：返回查询到的model对象  只能查询到一个
    # ret = Book.objects.get(title='金瓶梅')
    # print(ret)

    #4 first() last() 方法 queryset调用，返回的是model对象
    # fbook = Book.objects.all()[0]
    # fbook = Book.objects.all().first()   #上等同于下
    # lbook = Book.objects.all().last()

    #5 exclude() 方法 返回一个queryset
    # ret = Book.objects.exclude(publish="北京出版社")
    # print(ret)

    #6 order_by:排序  由queryset调用 返回queryset
    # ret = Book.objects.all().order_by('price','id')  #第二个参数是对第一个相同的排序
    # ret = Book.objects.all().order_by('-price').first()  #加 - 代表降序
    # print(ret)

    #7 count:数数  由queryset对象调用 返回int类型
    # ret = Book.objects.all().count()
    # print(ret)
    # return HttpResponse('ok')

    #8 reverse():翻转  由queryset调用 返回queryset
    # ret = Book.objects.all().reverse()

    #9 exists() :判断是否有记录
    # ret = Book.objects.all().exists()

    #10  value() 方法  queryset:[{title:'xxx'},{title:'xxx'}]
    # ret = Book.objects.all().values("title")  #queryset:[{title:'xxx'},{title:'xxx'}]
    """
    ret=[]
    for obj in Book.object.all():
        temp={
            "title":obj.title
        }
        ret.append(temp)
    """

    #11 value_list() 方法  queryset:[('xxx'),('xxx'),('xxx')]
    # ret = Book.objects.values_list('title','price')
    # print(ret)

    #12 distinct() 方法 不能对对象去重所以不能直接用在all()后面
    # ret = Book.objects.all().values('publish').distinct()
    # print(ret)

    # ===================模糊查询=======================
    #查询价格大于100的书籍  #<QuerySet [<Book: 金瓶梅>, <Book: 肉蒲团>]>
    # ret = Book.objects.filter(price__gt=100)  # 大于
    # ret = Book.objects.filter(price__lt=100)  # 小于
    # ret = Book.objects.filter(price__gte=100)  # 大于等于
    # ret = Book.objects.filter(price__lte=100)  # 小于等于

    #查询以py开头的书籍名称  #<QuerySet [{'title': 'python语言程序设计'}, {'title': 'python爬虫实战'}]>
    # ret = Book.objects.filter(title__startswith='py').values('title')  #istartswith 不区分大小写

    # 查询包含p的书籍名称
    # ret = Book.objects.filter(title__contains='p').values('title') #icontains不区分大小写

    # 查询年份为2019 月份为11的数据
    # ret = Book.objects.filter(pub_date__year=2019,pub_date__month=11)
    # print(ret)
    return HttpResponse('ok')



