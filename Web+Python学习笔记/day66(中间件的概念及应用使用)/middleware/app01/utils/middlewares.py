from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render,HttpResponse
from app01.models import IP_count

# class PrintIPMiddleWare(MiddlewareMixin):
#     def process_request(self,request):
#         print(request.META.get('REMOTE_ADDR'))
#         print('M1 process_request')

class M1(MiddlewareMixin):
    def process_request(self,request):
        print('M1 process_request')



    def process_response(self,request,response):
        print('M1 process_response')
        return response

    def process_view(self,request,callback,callback_args,callback_kwargs):
        # print('callback',callback)
        # print('callback_args',callback_args)
        # ret = callback(request)
        # print('ret:', ret)
        print('M1 process_view')
        IP = request.META.get('REMOTE_ADDR')
        obj = IP_count.objects.filter(IP=IP).first()
        if obj:
            if obj.count >= 20:
                return HttpResponse('访问次数过多拒绝访问')
            count = obj.count+1
            IP_count.objects.filter(IP=IP).update(count=count)

        else:
            IP_count.objects.create(IP=IP, count=1)


    def process_exception(self,request,response):
        print("md1 process_exception...")




class M2(MiddlewareMixin):
    def process_request(self, request):
        print('M2 process_request')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        # print('callback',callback)
        # print('callback_args',callback_args)
        print('M2 process_view')

    def process_response(self, request, response):
        print('M2 process_response')
        # print(response.content)
        return response

    def process_exception(self,request,response):
        print('M2 process_exception')
        print(response)
        return HttpResponse(response)


