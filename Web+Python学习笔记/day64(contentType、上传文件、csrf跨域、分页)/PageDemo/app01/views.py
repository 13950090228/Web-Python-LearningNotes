from django.shortcuts import render,HttpResponse
from app01.models import Book
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def index(request):
    print(request.GET)
    #批量插入
    # book_list=[]
    # for i in range(1,101):
    #     book=Book(title='book_%s'%i,price=i*i)
    #     book_list.append(book)
    #
    # Book.objects.bulk_create(book_list)


    # #分页器的使用函数
    # # pag = Paginator(book_list,8)
    # #
    # # print(pag.count)  #计算总数
    # # print(pag.num_pages)  #分页数  13
    # # print(pag.page_range) #range(1,14)
    # # page = pag.page(5)   #第5页
    # # print(page.has_next())  #下一页
    # # print(page.has_previous())  # 上一页
    # #
    # # print(page.next_page_number())  #下一页数字
    # # print(page.previous_page_number())  # 上一页数字
    # book_list = Book.objects.all()
    # pag = Paginator(book_list,10)
    # current_page_num = request.GET.get("pag", 1)
    # current_page_num = int(current_page_num)
    #
    # try:
    #     current_page_num = request.GET.get("pag",1)
    #     current_page_num = int(current_page_num)
    #     current_page = pag.page(current_page_num)
    # except EmptyPage as e:
    #     current_page_num = 1
    #     current_page = pag.page(current_page_num)




    # 自定义分页
    from app01.page import Pagination
    book_list = Book.objects.all()
    current_page_num = request.GET.get("page",1)
    pagination = Pagination(current_page_num,book_list.count(),request)
    print(book_list.count())
    book_list = book_list[pagination.start:pagination.end]


    return render(request,'index.html',locals())

