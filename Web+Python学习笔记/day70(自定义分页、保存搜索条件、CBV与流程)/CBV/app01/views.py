from django.shortcuts import render,HttpResponse

# Create your views here.
from django.views import View
class LoginView(View):
    def dispatch(self, request, *args, **kwargs):
        print('dispatch')

    def get(self,request):

        return render(request,"login.html")

    def post(self,request):

        return HttpResponse('ok')

    def delete(self,request):
        pass

    def put(self,request):
        pass