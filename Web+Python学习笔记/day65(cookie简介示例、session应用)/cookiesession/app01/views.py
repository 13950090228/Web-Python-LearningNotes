from django.shortcuts import render,redirect,HttpResponse
from app01.models import UserInfo
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request,"login.html")
    else:
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        # print(user,pwd)
        user_obj = UserInfo.objects.filter(user=user,pwd=pwd)[0]
        # user_obj = auth.authenticate(username=user,password=pwd)
        # auth.login(request,user_obj)
        if user_obj:
            #设置cookie
            obj = redirect('/index/')
            obj.set_cookie("username",user)
            obj.set_cookie("is_login",True)

            # return HttpResponse('ok')
            return obj
        else:
            return HttpResponse('fail')

def index(request):

    #获取cookie
    # print(request.user.is_authenticated)  #判断用户是登陆还是匿名状态，返回布尔值
    # print(request.user.username)
    # print(request)
    # print(request.COOKIES)
    is_login = request.COOKIES.get('is_login')
    username = request.COOKIES.get('username')
    if not is_login:
        return redirect('/login/')
    book_list = ["西游记","肉蒲团","金瓶梅"]
    sp = ['苹果','荔枝','榴莲']

    name = username

    return render(request,"index.html",locals())

def login_session(request):
    if request.method == 'GET':
        return render(request, "login.html")
    else:
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        user_obj = UserInfo.objects.filter(user=user, pwd=pwd)[0]
        if user_obj:
            #用户认证存储
            request.session['username']=user
            request.session['slogin']=True
            '''
            1 生成一个随机字符串   例如：afgfwetewftqfqeg
            2 向django-sessio表中插入记录
                session-key              session-data
               afgfwetewftqfqeg         {"username":"lyq","slogin":True}
            3 响应set_cookie: {"sessionid":afgfwetewftqfqeg}
            '''
            return redirect('/index_session/')

        else:
            return HttpResponse('fail')

def index_session(request):
    '''
    1 request.COOKIE.get("sessionid")  :afgfwetewftqfqeg
    2 在django-session表过滤session-key=afgfwetewftqfqeg的记录
    3 取出过滤记录的session-data反序列化成数据字典）{"usernaem:"lyq","slogin":True}
    '''
    slogin = request.session.get('slogin')
    if not slogin:
        return redirect('/login_session/')

    username = request.session.get('username')
    book_list = ["西游记","肉蒲团","金瓶梅"]
    sp = ['苹果','荔枝','榴莲']
    name = username

    return render(request,"index.html",locals())

def logout(request):
    '''
       1 request.COOKIE.get("sessionid")  :afgfwetewftqfqeg
       2 在django-session表过滤session-key=afgfwetewftqfqeg的记录删除
       3 response.delete_cookie("sessionid")
    '''
    # auth.logout(request)
    request.session.flush()
    return redirect('/login/')

def register(request):
    # User.objects.create(username='djg',password='djg123')   #不用这个
    # user = User.objects.create_user(username='djb',password='123')
    ret = request.user.check_password('djg123')
    if ret:
        request.user.set_password('666')
        request.user.save()
        return HttpResponse('ok')
    else:
        return HttpResponse('worry')