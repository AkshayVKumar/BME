from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/employee/login/')
def Employee_base(request):
    return render(request,"Employee/index.html")

def Employee_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("pwd")
        user=authenticate(request,username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return render(request,"Employee/index.html")
            else:
                raise ValueError("User is not active")
        else:
            raise ValueError("Username and password is not found")
    return render(request,"Employee/Employee_login.html")
@login_required(login_url='/employee/login/')
def Check_add(request):
    return render(request,"Employee/check_add.html")

@login_required(login_url='/employee/login/')
def Employee_logout(request):
    logout(request)
    return redirect('login')
    