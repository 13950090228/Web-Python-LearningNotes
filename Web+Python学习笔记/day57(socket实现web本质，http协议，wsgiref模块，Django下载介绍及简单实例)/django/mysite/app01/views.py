from django.shortcuts import render
import datetime
# Create your views here.
def timer(request):
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    
    return HttpResponse("liu 123")