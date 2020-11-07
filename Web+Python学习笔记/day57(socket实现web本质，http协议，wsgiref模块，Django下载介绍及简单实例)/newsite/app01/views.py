from django.shortcuts import render,HttpResponse,redirect
import datetime
# Create your views here.
def timer(reqeust):
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    return HttpResponse(now)

def login(request):
    if request.method == 'GET':
        return render(request,"login.html")
    else:
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if user == 'lyq' and pwd == '123':
            # return HttpResponse('success')
            return redirect("/index/")
        return HttpResponse('fail')
# def auth(request):
#     print(request.POST) #<QueryDict: {'user': ['lyq'], 'pwd': ['123']}>
#     user = request.POST.get("user")
#     pwd = request.POST.get("pwd")
#     if user == 'lyq' and pwd == '123':
#         return HttpResponse('success')
#     return HttpResponse('fail')

def year(request,data):
    return HttpResponse(data)

def year_month(request,year,month):
    
    return HttpResponse("year:%s month:%s"%(year,month))

def index(request):
    """
    Django对于一定最后相应一个HttpResponse的实例对象

    三种形式：
        1 HttpResponse('字符串')
        2 render("页面")
            --读取文件字符串
            --嵌入变量
        3 redirect()  #重定向

    模板语法:
        {%%}
        {{}}
    """
    class Human(object):
        def __init__(self,name,age):
            self.name = name
            self.age = age
        def running(self):
            return "running"
    #过滤器
    import datetime
    now = datetime.datetime.now()
    link = "<a href='#'>点我</a>"
    tag = "<script>alert(123)</script>"
    book_list = ["西游记","肉蒲团","金瓶梅"]
    sp = ['苹果','荔枝','榴莲']
    num = 111
    name = 'lyq'
    student = [{'name':'lyq'},{'age':18}]
    lyq = Human('lyq','age')
    return render(request,"index.html",locals())
    # return render(request, "index.html", {"sp": shangpin_list, "name": name})
    # print(request.method)  # 请求方式
    # print(request.path)  # 请求路径
    # print(request.POST)  # POST的请求数据  字典格式
    # print(request.GET)  # GET的请求数据  字典格式
    # print(request.META)  # 请求头
    # print(request.get_full_path())
    # print(request.is_ajax())
    #
    # return HttpResponse('ok')

