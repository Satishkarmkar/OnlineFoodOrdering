from django.shortcuts import render,redirect
from vendor.models import VendorRegistrationModel,FoodTypeModel,FoodItemsModel
from pwn.models import CuisineModel,CityModel
from django.contrib import messages

# Create your views here.

def openLogin(request):
    return render(request,"vendor/login.html")


def vendor_login_check(request):
    if request.method == "POST":
        try:
            vendor_res = VendorRegistrationModel.objects.get(contact1=request.POST.get("contact1"),password=request.POST.get("vendor_pass"),status='approved')
            request.session["vendor_status"] = True
            return redirect('vendor_welcome',pk=vendor_res.id)
        except:
            return render(request, "vendor/login.html", {"error": "Invalid Credentials"})
    else:
        request.session["vendor_status"] = False
        return render(request, "vendor/login.html", {"error": "Vendor Logout Successfully"})


def vendor_register(request):
    return render(request,"vendor/vendor_register.html",{"cuisine":CuisineModel.objects.all(),"city":CityModel.objects.all()})

def vendor_save(request):
    sn = request.POST.get("stall_name")
    contact1 = request.POST.get("contact1")
    contact2 = request.POST.get("contact2")
    cuisinetype = request.POST.get("cuisinetype")
    cuisineimg = request.FILES["cuisineimage"]
    venaddrs = request.POST.get("vendor_address")
    cityname = request.POST.get("cityname")
    venpswd = request.POST.get("vendor_pass")
    otp = 0000
    status = "pending"
    VendorRegistrationModel(stall_name=sn,contact1=contact1,contact2=contact2,cuisine_type_id=cuisinetype,photo=cuisineimg,address=venaddrs,vendor_city_id=cityname,password=venpswd,OTP=otp,status=status).save()
    messages.success(request,"Registration Done, Wait for Admin Approval")
    return redirect('vendor_main')


def vendor_welcome(request,pk):
    request.session["vendor_id"]=pk
    vendor_details = VendorRegistrationModel.objects.get(id=pk)

    return render(request,"vendor/home.html",{"vendor_details":vendor_details})



def vendor_foodtype(request):
    vendor_details = VendorRegistrationModel.objects.get(id=request.session["vendor_id"])
    return render(request,"vendor/foodtype.html",{"vendor_details":vendor_details,"food_type":FoodTypeModel.objects.filter(vendor_id_id=request.session["vendor_id"])})


def vendor_logout(request):
    return vendor_login_check(request)


def vendor_save_foodtype(request):
    FoodTypeModel(name=request.POST.get("foodtype"),status=request.POST.get("foodstatus"),vendor_id_id=request.session["vendor_id"]).save()
    return vendor_foodtype(request)


def vendor_update_foodtype(request):
    vendor_details = VendorRegistrationModel.objects.get(id=request.session["vendor_id"])
    ftd = FoodTypeModel.objects.all()
    fid = request.GET.get("id")
    fdid = FoodTypeModel.objects.get(id=fid)
    return render(request, "vendor/foodtype.html", {"vendor_details":vendor_details, "foodtype_data": fdid, "fooddata": ftd})


def vendor_save_update_foodtype(request):
    FoodTypeModel.objects.filter(id=request.GET.get("fid")).update(name=request.POST.get("foodtype"),status=request.POST.get("foodstatus"),vendor_id_id=request.session["vendor_id"])
    return redirect('vendor_foodtype')

def vendor_delete_foodtype(request):
    FoodTypeModel.objects.filter(id=request.GET.get('fid')).delete()
    messages.success(request, 'Food type deleted')
    return redirect('vendor_foodtype')


def vendor_food(request):
    vendor_details = VendorRegistrationModel.objects.get(id=request.session["vendor_id"])
    return render(request,"vendor/food.html",{"vendor_details":vendor_details,"food_type":FoodTypeModel.objects.filter(vendor_id_id=request.session["vendor_id"]),"food":FoodItemsModel.objects.filter(food_type__vendor_id=request.session["vendor_id"])})


def vendor_save_food(request):
    FoodItemsModel(name=request.POST.get("foodname"),food_type_id=request.POST.get("foodtype"),price=request.POST.get("foodprice"),photo=request.FILES['foodimage']).save()
    return vendor_food(request)


def vendor_update_food(request):
    vendor_details = VendorRegistrationModel.objects.get(id=request.session['vendor_id'])
    fooddt = FoodItemsModel.objects.all()
    foodid = request.GET.get("id")
    fooduid = FoodItemsModel.objects.get(id=foodid)
    return render(request,"vendor/food.html",{"vendor_details":vendor_details,"fooditems":fooddt,"foodupdateid":fooduid,"food_type":FoodTypeModel.objects.filter(vendor_id_id=request.session["vendor_id"])})

def vendor_save_update_food(request):
    FoodItemsModel.objects.filter(id=request.GET.get("foodid")).update(name=request.POST.get("foodname"),food_type_id=request.POST.get("foodtype"),price=request.POST.get("foodprice"),photo=request.FILES['foodimage'])
    return redirect('vendor_food')


def vendor_delete_food(request):
    FoodItemsModel.objects.filter(id=request.GET.get("foodid")).delete()
    messages.success(request, 'Food type deleted')
    return vendor_food(request)