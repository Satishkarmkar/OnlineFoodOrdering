from django.contrib import admin
from django.urls import path
from pwn import views
#admin urls.py
urlpatterns = [
    path('',views.showIndex,name='index'),
    path('pwn_login_check/',views.pwn_login_check,name="pwn_login_check"),
    path('welcome/',views.welcome,name="welcome")
]