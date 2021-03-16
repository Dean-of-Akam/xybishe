from django.db import models


class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32)
    pwd = models.CharField(verbose_name='密码', max_length=32)
    phone_num = models.CharField(verbose_name='手机号码', max_length=32)
    email = models.EmailField(verbose_name='邮箱', max_length=32)
