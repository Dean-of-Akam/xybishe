from django.contrib import admin
from .models import UserInfo


class UserinfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'pwd', 'phone_num', 'email')


admin.site.register(UserInfo, UserinfoAdmin)
