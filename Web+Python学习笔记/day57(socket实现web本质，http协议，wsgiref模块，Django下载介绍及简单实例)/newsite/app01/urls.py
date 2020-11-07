from django.contrib import admin
from django.urls import path,re_path,include
from app01 import views
import re

urlpatterns = [
    path('admin/', admin.site.urls),
    path('timer/', views.timer),
    path('login/', views.login),
    path('auth/', views.auth),
    path('atr/2000/', views.year),
    re_path('^atr/(\d{4})/$', views.year),
    # 有名分组
    re_path('^atr/(?P<year>\d{4})/(?P<month>\d{2})/$',views.year_month) #有名分组 ?P<名字>


]