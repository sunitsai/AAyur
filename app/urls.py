from django.urls import path,include
from . import views
urlpatterns = [
   path("",views.Cust_RegisterPage,name="cust_registepage"),
   path("loginoage",views.Cust_LoginPage,name="loginpage"),
   path("register/",views.Register_Cust,name="register"),
   path("loginuser/",views.LoginCust,name="login"),
]
