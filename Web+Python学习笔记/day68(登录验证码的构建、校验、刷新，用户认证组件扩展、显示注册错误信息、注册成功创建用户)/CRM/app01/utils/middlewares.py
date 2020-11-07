from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render,HttpResponse,redirect
from django.conf import settings
class LoginMiddleWaer(MiddlewareMixin):

    def process_request(self,request):
        if request.path in ['/login/','/reg/','/get_valid_img/','/admin/']:
            return None

        if not request.user.id:

            return redirect('/login/')

# class CurrentUserMiddleWaer(MiddlewareMixin):
#
#     def process_request(self,request):
#         settings.CURRENT_USER_pk=request.user.pk