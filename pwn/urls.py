
from django.contrib import admin
from django.urls import path
from pwn import views
#admin urls.py
urlpatterns = [
    path('',views.showIndex,name='index'),
    path('pwn_login_check/',views.pwn_login_check,name="pwn_login_check"),
    path('welcome/',views.welcome,name="welcome"),

    path('state/',views.openState,name="state"),
    path('savestate/',views.saveState,name="savestate"),
    path('updatestate/',views.updateState,name="updatestate"),
    path('updatestateid/',views.updateStateid,name="updatestateid"),
    path('deletestate/',views.deleteState,name="deletestate"),




    path('city/',views.openCity,name="city"),
    path('cuisine/',views.openCuisine,name="cuisine"),
    path('vendor/',views.openVendor,name="vendor"),
    path('reports/',views.openReports,name="reports"),
    path('logout/',views.pwn_login_check,name="logout"),


]