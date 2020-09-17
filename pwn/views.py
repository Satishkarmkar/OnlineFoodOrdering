from django.shortcuts import render,redirect
from pwn.models import AdminLoginModel,StateModel,CityModel,CuisineModel
from django.contrib import messages
# Create your views here.

def showIndex(request):
    return render(request,"pwn/login.html")


def pwn_login_check(request):
    if request.method == "POST":
        try:
            admin = AdminLoginModel.objects.get(username=request.POST.get("pwn_username"),password=request.POST.get("pwn_password"))
            request.session["admin_status"]=True
            return redirect('welcome')
        except:
            return render(request,"pwn/login.html",{"error":"Invalid Credentials"})
    else:
        request.session["admin_status"]=False
        return render(request,"pwn/login.html",{"error":"Admin Logout Successfully"})


def welcome(request):
    return render(request,"pwn/home.html")


def openState(request):
    statedetails = StateModel.objects.all()
    return render(request,"pwn/openstate.html",{"sd":statedetails})

def saveState(request):
    statename = request.POST.get('statename')
    statephoto = request.FILES['stateimage']
    StateModel(name=statename,photo=statephoto).save()
    messages.success(request,"State Saved Successfully")
    return openState(request)

def updateState(request):
    sid = request.GET.get('id')
    sm = StateModel.objects.get(id=sid)
    sm_all = StateModel.objects.all()
    return render(request,'pwn/openstate.html',{'udata':sm,'data':sm_all})

def updateStateid(request):
    StateModel.objects.filter(id=request.GET.get('sid')).update(name=request.POST.get('statename'),photo=request.FILES.get('stateimage'))
    return redirect('state')

def deleteState(request):
    StateModel.objects.filter(id=request.GET.get('sid')).delete()
    messages.success(request,'state deleted')
    return redirect('state')


def openCity(request):
    return render(request,"pwn/opencity.html",{"s_data":StateModel.objects.all(),"c_data":CityModel.objects.all()})

def saveCity(request):
    CityModel(name=request.POST.get("cityname"),photo=request.FILES['city_image'],city_state_id=request.POST.get("statename")).save()
    return openCity(request)

def updateCity(request):
    sm = StateModel.objects.all()
    cid = request.GET.get('id')
    cm = CityModel.objects.get(id=cid)
    return render(request,"pwn/opencity.html",{"cudata":cm,"s_data":sm})

def saveUpdateCity(request):
    CityModel.objects.filter(id=request.GET.get("cid")).update(name = request.POST.get("cityname"),photo = request.FILES("city_image"),city_state_id = request.POST.get("statename"))
    return redirect('city')

def deleteCity(request):
    CityModel.objects.filter(id=request.GET.get('cid')).delete()
    messages.success(request,'city deleted')
    return redirect('city')


def openCuisine(request):
    return render(request,"pwn/opencuisine.html",{"cuisine_data":CuisineModel.objects.all()})

def saveCuisine(request):
    CuisineModel(type = request.POST.get('cuisinetype'),photo = request.FILES['cuisineimage']).save()
    return openCuisine(request)

def updateCuisine(request):
    cuim = CuisineModel.objects.all()
    cuid = request.GET.get("id")
    csnm = CuisineModel.objects.get(id=cuid)
    return render(request,"pwn/opencuisine.html",{"cuisdata":csnm,"cusdata":cuim})

def saveUpdateCuisine(request):
    CuisineModel.objects.filter(id=request.GET.get("cuid")).update(type = request.POST.get('cuisinetype'),photo = request.FILES['cuisineimage'])
    return openCuisine(request)

def deleteCuisine(request):
    CuisineModel.objects.filter(id=request.GET.get('cuid')).delete()
    messages.success(request, 'cuisine type deleted')
    return redirect('cuisine')

def openVendor(request):
    return render(request,"pwn/openvendor.html")



def openReports(request):
    return render(request,"pwn/openreports.html")


