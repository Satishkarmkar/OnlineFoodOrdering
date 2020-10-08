from django.contrib import admin
from django.urls import path
#customer urls.py
from customer import views

urlpatterns = [

    path('',views.showIndex,name="index")

]