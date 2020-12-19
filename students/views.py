from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"students/index.html")

def aboutus(request):
    return render(request,"students/aboutus.html")

def contact_us(request):
    return render(request,"students/contactus.html")

def services(request):
    return render(request,"students/services.html")

def colleges(request):
    return render(request,"students/colleges.html")