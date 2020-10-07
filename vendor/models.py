from django.db import models
from pwn.models import CuisineModel,CityModel
# Create your models here.

class VendorRegistrationModel(models.Model):
    id = models.AutoField(primary_key=True)
    stall_name = models.CharField(max_length=100)
    contact1 = models.IntegerField(unique=True)
    contact2 = models.IntegerField(unique=True)
    cuisine_type = models.ForeignKey(CuisineModel,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='vendor_images/')
    address = models.TextField()
    vendor_city = models.ForeignKey(CityModel,on_delete=models.CASCADE)
    password = models.CharField(max_length=20)
    OTP = models.IntegerField()
    status = models.CharField(max_length=10)

class FoodTypeModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    vendor_id = models.ForeignKey(VendorRegistrationModel,on_delete=models.CASCADE)
    status = models.CharField(max_length=10,default=None) #suspend activate

class FoodItemsModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    food_type = models.ForeignKey(FoodTypeModel,on_delete=models.CASCADE)
    price = models.FloatField()
    photo = models.ImageField(upload_to='fooditems_images/')