from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):

    return render(request,"index.html")

def order(request):

    order_list = ['订单一','订单二','订单三']
    return render(request,"order.html",locals())


def shop_list(request):
    Shop_list = ['苹果', '香蕉', '桃子']
    return render(request, "shop_list.html",locals())
