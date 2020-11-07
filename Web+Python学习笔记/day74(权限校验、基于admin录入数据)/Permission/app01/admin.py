from django.contrib import admin

# Register your models here.
from app01.models import *

class UserConfig(admin.ModelAdmin):
    list_display = ['pk','name']
    ordering = ["pk"]

admin.site.register(User,UserConfig)

class RoleConfig(admin.ModelAdmin):
    list_display = ['pk','title']
    ordering = ["pk"]

admin.site.register(Role,RoleConfig)

class PersissionConfig(admin.ModelAdmin):
    list_display = ['pk','title','url']
    ordering = ["pk"]

admin.site.register(Permission,PersissionConfig)