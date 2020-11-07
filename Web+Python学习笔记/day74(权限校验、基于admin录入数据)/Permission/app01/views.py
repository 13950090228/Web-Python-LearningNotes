from django.shortcuts import render,HttpResponse
from app01.models import User,Role,Permission
# Create your views here.
def customers(reqeust):
    return HttpResponse("customers....")

def orders(reqeust):
    return HttpResponse("orders....")

def addorders(request):
    return HttpResponse("addorders....")

def editorders(request,id):
    return HttpResponse("editorders....")

def delorders(request,id):
    return HttpResponse("delorders....")

def addcustomers(request):
    return HttpResponse("addcustomers....")

def editcustomers(request,id):
    return HttpResponse("editcustomers....")

def delcustomers(request,id):
    return HttpResponse("delcustomers....")

def login(request):
    if request.method == 'POST':
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        user_obj = User.objects.filter(name=user,pwd=pwd).first()

        if user_obj:
            #保存用户状态信息
            request.session['user_id']=user_obj.pk
            ret = Role.objects.filter(user__name=user).values("permissions__url").distinct()
            permissions_list = []
            for i in ret:
                permissions_list.append(i['permissions__url'])


            request.session['permissions_list']=permissions_list

            return HttpResponse("登陆成功")
        else:
            return HttpResponse("登陆失败")
    else:

        return render(request,"login.html")