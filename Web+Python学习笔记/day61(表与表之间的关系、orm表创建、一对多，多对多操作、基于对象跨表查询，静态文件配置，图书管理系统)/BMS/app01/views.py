from django.shortcuts import render,HttpResponse,redirect
from app01.models import Book,Publish,Author,AuthorDetail

# Create your views here.

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
    # data = AuthorDetail.objects.filter(tel=1111)[0]
    # print(data.author.name)
    # return HttpResponse('成功')




############图书管理系统##############3
def book_view(request):
    book_list = Book.objects.all()
    return render(request,'book_view.html',locals())

def book_add(request):
    if request.method=='GET':
        publish_list = Publish.objects.all()
        author_list = Author.objects.all()
        return render(request,'book_add.html',locals())
    else:
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish_id = request.POST.get('publish_id')
        author = request.POST.getlist('author')

        book = Book.objects.create(title=title,price=price,pub_date=pub_date,publish_id=publish_id)
        book.authors.add(*author)
        return redirect('/book/')

def book_delete(request,del_book_id):
    Book.objects.filter(nid=del_book_id).delete()

    return redirect('/book/')

def book_edit(request,edit_book_id):
    edit_book = Book.objects.filter(pk=edit_book_id).first()
    if request.method == 'GET':
        publish_list = Publish.objects.all()
        author_list = Author.objects.all()
        return render(request,'book_edit.html',locals())
    else:
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish_id = request.POST.get('publish_id')
        author = request.POST.getlist('author')
        Book.objects.filter(pk=edit_book_id).update(title=title, price=price, pub_date=pub_date, publish_id=publish_id)
        edit_book.authors.set(author)

        return redirect('/book/')
