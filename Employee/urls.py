from django.urls import path,include
from Employee import views


urlpatterns = [
    path('',views.Employee_base,name="index"),
    path('login/',views.Employee_login,name="login"),
    path('check/',views.Check_add,name="check_add"),
]
