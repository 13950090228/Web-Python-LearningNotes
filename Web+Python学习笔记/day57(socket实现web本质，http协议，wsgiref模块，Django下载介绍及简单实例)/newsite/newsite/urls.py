"""newsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from app01 import views
import re

urlpatterns = [
    path('admin/', admin.site.urls),
    path('timer/', views.timer),
    # path('login/', views.login),
    # path('auth/', views.auth),
    path('atr/2000/', views.year),
    path('index/', views.index),
    # 反向解析
    path('login/', views.login, name="xxx"),

    re_path('^atr/(\d{4})/$', views.year),
    # 有名分组
    re_path('^atr/(?P<year>\d{4})/(?P<month>\d{2})/$',views.year_month) #有名分组 ?P<名字>
    # 分发include
    # re_path('^app01/',include('app01.urls')),  #先找到app01，再到里面找路径


]