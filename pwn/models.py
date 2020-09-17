from django.db import models

# Create your models here.

class StateModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,unique=True)
    photo = models.ImageField(upload_to='state_images/')

class CityModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,unique=True)
    photo = models.ImageField(upload_to='city_images/')
    city_state = models.ForeignKey(StateModel,on_delete=models.CASCADE)

class CuisineModel(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100,unique=True)
    photo = models.ImageField(upload_to='cuisine_images/')

class AdminLoginModel(models.Model):
    username = models.CharField(primary_key=True,max_length=50)
    password = models.CharField(max_length=20)
    OTP = models.IntegerField(default=1234)