from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render,HttpResponse,redirect
import re

class PermissionMiddleware(MiddlewareMixin):

    def process_request(self,request):
        path = request.path
        user = request.session.get("user_id")

        for j in ['/login/','/admin/*']:
            ret = re.search(j,path)
            if ret:
                return None

        user = request.session.get("user_id")
        print(user)
        if not user:
            return redirect('/login/')

        permissions_list = request.session.get('permissions_list')

        for i in permissions_list:
            i = "^%s$"%(i)
            ret = re.search(i,path)
            if ret:
                return None

        return HttpResponse("您无权限访问")