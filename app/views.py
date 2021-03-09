from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from random import randint
# Create your views here.


def Cust_RegisterPage(request):
    return render(request,"app/cust_signup.html")

def Cust_LoginPage(request):
    return render(request,"app/login.html")

def Register_Cust(request):
    if request.method == "POST":
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']

        user = Customer.objects.filter(Email=email)
        if user:
            message = "User already Exist"
            return render(request,"app/cust_signup.html",{'msg':message})

        else:
            otp = randint(10000,99999)
            newuser = Customer.objects.create(Email=email,Password=password,Mobile=contact)
            return redirect('loginpage')



def LoginCust(request):
    if request.method == "POST":
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        print(request.POST)
        try:
            user = Customer.objects.get(Email=email, Password=password, Mobile=contact)
            request.session['Email'] = user.Email
            return render(request, 'app/home.html')

        except:
            return HttpResponse('User does not exist.')
    else:
        return HttpResponse('Invalid method.')