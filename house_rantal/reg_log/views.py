from django.core.validators import RegexValidator
from django.shortcuts import render
from django.http import HttpResponse

from django import forms
from . import models


class RegisterModelForm(forms.ModelForm):
    phone_num = forms.CharField(label='手机号码', validators=[RegexValidator(r'(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误')], )
    pwd = forms.CharField(label='密码', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='重复密码', widget=forms.PasswordInput())
    code = forms.CharField(label='验证码')

    class Meta:
        model = models.UserInfo
        fields = "__all__"


def re_lo(request):
    form = RegisterModelForm()
    return render(request, 'reg_log/register.html', {'form': form})
