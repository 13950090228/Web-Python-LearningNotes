from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render,HttpResponse,redirect

class M1(MiddlewareMixin):
    def process_request(self,request):
        if request.path in ['/login/']:
            return None
        is_login = request.COOKIES.get('is_login')
        if not is_login:
            return redirect('/login/')

