from django.shortcuts import render,redirect
from vendor.models import VendorRegistrationModel
from pwn.models import CuisineModel,CityModel
from django.contrib import messages

# Create your views here.

def openLogin(request):
    return render(request,"vendor/login.html")


def vendor_login_check(request):
    if request.method == "POST":
        try:
            vendor = VendorRegistrationModel.objects.get(contact1=request.POST.get("contact1"),
                                                password=request.POST.get("vendor_pass"),status='approved')
            request.session["vendor_status"] = True
            return redirect('vendor_welcome')
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


def vendor_welcome(request):

    return render(request,"vendor/welcome.html")