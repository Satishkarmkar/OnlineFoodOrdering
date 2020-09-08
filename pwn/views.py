from django.shortcuts import render,redirect
from pwn.models import AdminLoginModel,StateModel
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
    return render(request,'pwn/openstate.html',{'udata':sm})

def updateStateid(request):
    StateModel.objects.filter(id=request.GET.get('sid')).update(name=request.POST.get('statename'),photo=request.FILES.get('stateimage'))
    return redirect('state')

def deleteState(request):
    StateModel.objects.filter(id=request.GET.get('sid')).delete()
    messages.success(request,'state deleted')
    return redirect('state')


def openCity(request):
    return render(request,"pwn/opencity.html")


def openCuisine(request):
    return render(request,"pwn/opencuisine.html")


def openVendor(request):
    return render(request,"pwn/openvendor.html")


def openReports(request):
    return render(request,"pwn/openreports.html")

