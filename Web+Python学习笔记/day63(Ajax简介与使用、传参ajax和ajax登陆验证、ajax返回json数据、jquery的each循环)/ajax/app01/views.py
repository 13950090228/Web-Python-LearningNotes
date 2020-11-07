from django.shortcuts import render,HttpResponse
from app01.models import UserIngo,Class,Student,Teacher,Course,Scoree,Class_grade,Teach_class
from django.db.models import Avg,Sum,Max,Min,Count,F,Q
import os
from ajax import settings
# Create your views here.
import json
def handle_ajax(request):
    return HttpResponse('刘永祺')

def index(reqeust):
    return render(reqeust,'index.html')

def cal(reqeust):
    # print(reqeust.GET)
    # num1 = reqeust.GET.get("num1")
    # num2 = reqeust.GET.get("num2")
    # num1 = reqeust.POST.get("num1")
    # num2 = reqeust.POST.get("num2")
    # res = int(num1)+int(num2)
    # return HttpResponse(json.dumps(res))
    res = reqeust.body.decode('utf8')

    res = json.loads(res)
    ret = int(res['num1']) + int(res['num2'])
    return HttpResponse(ret)
def login(request):
    if request.method == 'POST':
        res={"user":None,"error":""}
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        ret = UserIngo.objects.filter(user=user,pwd=pwd).first()
        print(ret)
        if ret:
            res["user"]=user
            res["error"] = "用户名或密码正确!"
        else:
            res["error"]="用户名或密码错误!"

        return HttpResponse(json.dumps(res))
    else:
        return render(request,'login.html')

def query(request):
    ret = Scoree.objects.values('course_id').annotate(max=Max('score'),min=Min('score'))
    print(ret)

    return HttpResponse('ok')

def name(request):
    return HttpResponse('ok')

def file_put(request):
    print(request.POST)
    print(request.FILES)
    try:
        file_obj = request.FILES.get('file_obj')
        path = file_obj.name
        path = os.path.join(settings.BASE_DIR,"media","img",path)
        with open(path,'wb') as f:
            for line in file_obj:
                f.write(line)
        return HttpResponse('ok')
    except Exception as e:
        return HttpResponse('error')