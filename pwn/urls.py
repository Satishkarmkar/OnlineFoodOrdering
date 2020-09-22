
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
    path('savecity/',views.saveCity,name="savecity"),
    path('updatecity/',views.updateCity,name="updatecity"),
    path('saveupdatecity/',views.saveUpdateCity,name="saveupdatecity"),
    path('deletecity/',views.deleteCity,name="deletecity"),




    path('cuisine/',views.openCuisine,name="cuisine"),
    path('savecuisine/',views.saveCuisine,name="savecuisine"),
    path('updatecuisine/',views.updateCuisine,name="updatecuisine"),
    path('saveupdatecuisine/',views.saveUpdateCuisine,name="saveupdatecuisine"),
    path('deletecuisine/',views.deleteCuisine,name="deletecuisine"),

    path('vendor/',views.openVendor,name="vendor"),
    path('pwn_vendor_approve/',views.pwn_vendor_approve,name="pwn_vendor_approve"),
    path('pwn_vendor_cancel/',views.pwn_vendor_cancel,name="pwn_vendor_cancel"),
    path('pwn_vendor_delete/',views.pwn_vendor_delete,name="pwn_vendor_delete"),
    path('reports/',views.openReports,name="reports"),
    path('logout/',views.pwn_login_check,name="logout"),


]