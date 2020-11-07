from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import auth
from django.contrib.auth.models import User
class M1(MiddlewareMixin):

    def process_request(self,request):
        if request.path in ['/login/']:
            return None

        print(request.user.is_authenticated)
        if not request.user.is_authenticated:
            return redirect('/login/')