from django.shortcuts import render,redirect
from pwn.models import AdminLoginModel
# Create your views here.

def showIndex(request):
    return render(request,"pwn/login.html")
def pwn_login_check(request):
        try:
            admin = AdminLoginModel.objects.get(username=request.POST.get("pwn_username"),password=request.POST.get("pwn_password"))
            request.session["admin_status"]=True
            return redirect('welcome')
        except:
            return render(request,"pwn/login.html",{"error":"Invalid Credentials"})

def welcome(request):
    request.session["admin_status"] = True
    return render(request,"pwn/welcome.html")

