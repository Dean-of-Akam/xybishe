from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.re_lo, name="reg_log"),
]
