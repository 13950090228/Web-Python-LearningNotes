from django.shortcuts import render,HttpResponse
from app01.models import UserInfo
from django.forms import widgets
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'formsDemo.settings'
django.setup()
# Create your views here.
from django import forms
class UserForm(forms.Form):
    user = forms.CharField(min_length=5,
                           label='用户名',
                           error_messages={"required":"该字段不能为空"},
                           widget=widgets.TextInput(attrs={"class":"form-control"}),
                           )
    pwd = forms.CharField(
                            min_length=5,
                            label='密码',
                            widget=widgets.PasswordInput(attrs={"class":"form-control"}),
                            )
    r_pwd = forms.CharField(
                            min_length=5,
                            label='确认密码',
                            widget=widgets.PasswordInput(attrs={"class": "form-control"}),
    )

    email = forms.EmailField(
                            label='邮箱',
                            error_messages={"invalid": "输入正确的邮箱格式！"},
                            widget=widgets.EmailInput(attrs={"class":"form-control"}),
                            )

    def clean_user(self):
        val = self.cleaned_data.get("user")
        ret = UserInfo.objects.filter(user=val).first()
        if not ret:
            return val
        else:
            raise ValidationError("用户名已存在！")

    def clean_pwd(self):
        val = self.cleaned_data.get("pwd")
        if not val.isdigit():
            return val
        else:
            raise ValidationError("密码不能是纯数字！")

    def clean(self):
        pwd = self.cleaned_data.get("pwd")
        r_pwd = self.cleaned_data.get("r_pwd")
        if pwd and r_pwd:
            if pwd==r_pwd:
                return self.cleaned_data
            else:
                raise ValidationError("两次密码不一致")
        else:
            return self.cleaned_data



def reg(reqeust):
    if reqeust.method == 'POST':
        print(reqeust.POST)
        form=UserForm(reqeust.POST)
        if form.is_valid():
            print(form.cleaned_data)
            del form.cleaned_data['r_pwd']
            UserInfo.objects.create(**form.cleaned_data)
            return HttpResponse('成功')
        else:
            # print(form.errors)
            errors=form.errors
            # print(form.errors.get("__all__"))
            if form.errors.get("__all__"):
                g_error=form.errors.get("__all__")[0]
            return render(reqeust,'reg.html',locals())
    else:
        form = UserForm()
        return render(reqeust,'reg.html',locals())

