


from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect
import re
class PermissionMiddleWare(MiddlewareMixin):

    def process_request(self,request):
        print("permission_list",request.session.get("permission_list"))
        current_path = request.path

        # 设置白名单放行
        for reg in  ["/login/","/admin/*"]:
            ret=re.search(reg,current_path)
            if ret:
                return None
        # /customers/edit/1

        # 校验是否登录

        user_id=request.session.get("user_id")
        if not user_id:
            return redirect("/login/")

        # 校验权限
        permission_list=request.session.get("permission_list")

        for reg in permission_list:
             reg="^%s$"%reg
             ret=re.search(reg,current_path)
             if ret:
                 return None

        return HttpResponse("无访问权限！")

