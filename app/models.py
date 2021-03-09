from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

# User_Choice=(
#     ('(SuperAdmin', 'Super User')
#     ('Admin','Admin')
#     ('Vendor','Seller')
    

# )



# class User(AbstractBaseUser):
#     # role = models.TextChoices(User_Choice,)
#     # is_superuser = models.BooleanField(default=True)
#     # is_admin = models.BooleanField(default=False)
#     # is_vendor = models.BooleanField(default=False)
#     # is_Customer = models.BooleanField(default=False)
#     # Email = models.EmailField(max_length=150)
#     # password = models.CharField(max_length=150)
#     # is_active = models.BooleanField(default=True)
#     # date_joined = models.DateTimeField(auto_now_add=True)
#     # last_login = models.DateTimeField(auto_now_add=True)

class Customer(models.Model):
    Firstname = models.CharField(max_length=150, null=True)
    Lastname = models.CharField(max_length=150, null=True)
    Gender = models.CharField(max_length=15, null=True)
    Email = models.EmailField(max_length=150)
    Mobile = models.BigIntegerField(null=True)
    Password = models.CharField(max_length=150)
    State = models.CharField(max_length=150, null=True)
    City = models.CharField(max_length=150, null=True)
    Address = models.TextField(max_length=150, null=True)
    DeviceID = models.CharField(max_length=150,default="abc")
    DateJoined = models.DateTimeField(auto_now_add=True)
    LastLogin = models.DateTimeField(auto_now=True, null=True)



# class Seller(models.Model):
#     CompanyName = models.CharField(max_lenght=150, null=True)
#     CompanyName = models.CharField(max_lenght=150, null=True)
#     CompanyName = models.CharField(max_lenght=150, null=True)
#     CompanyName = models.CharField(max_lenght=150, null=True)
#     CompanyName = models.CharField(max_lenght=150, null=True)
#     CompanyName = models.CharField(max_lenght=150, null=True)

